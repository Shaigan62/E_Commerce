from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from products.models import Product,Category,Brand
from rest_framework.views import APIView
from .models import user_activity
from django.http import JsonResponse
from products.serializers import ProductDetailsSerializer
from rest_framework.response import Response

def create_soup(row):
    return row['category_name']+' '+row['brand_name']+' '+row['name']

def get_category(row):
    query = Category.objects.filter(id=row["category_id"])
    return str(query[0].title)


def get_brand(row):
    try:
        query = Brand.objects.filter(id=row["brand_id"])
        return query[0].brand_name
    except Exception:
        return ""

def get_dataframe():
    product_queryset = Product.objects.all().values()
    pro_dataframe = pd.DataFrame(list(product_queryset))
    pro_dataframe['category_name'] = pro_dataframe.apply(get_category, axis=1)
    pro_dataframe['brand_name'] = pro_dataframe.apply(get_brand, axis=1)
    pro_dataframe['soup'] = pro_dataframe.apply(create_soup, axis=1)
    return pro_dataframe

def get_recommendations(title):
    df = get_dataframe()
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df['soup'])
    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
    df = df.reset_index()
    indices = pd.Series(df.index, index=df['name'])

    idx = indices[title]
    idx = idx.iloc[0]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    product_indices = [i[0] for i in sim_scores]
    return df['name'].iloc[product_indices]


class RecommendProduct(APIView):
    def get(self,request,*args,**kwargs):
        current_user = request.user
        if current_user.is_authenticated:
            activity = user_activity.objects.filter(user_id=current_user.id)
            product_list = [x.id for x in activity]
            product_data = Product.objects.filter(id__in=product_list)
            product_name = [x.name for x in product_data]
            result = get_recommendations(product_name[0]).tolist()
            recommended_products = Product.objects.filter(name__in=result)
            final_data = ProductDetailsSerializer(recommended_products,many=True)
            return Response(final_data.data)
            # return JsonResponse({"message": "Logged In"})
        else:
            return JsonResponse({"message":"Not Logged In"})

class RegisterActivityViewSet(APIView):
    def get(self,request,*args,**kwargs):
        proid = kwargs.get('proid')
        current_user = request.user
        if current_user.is_authenticated:
            pro = Product.objects.filter(id=proid)[0]
            activity = user_activity(product_id=pro,user_id=current_user)
            activity.save()
            return JsonResponse({"message": "Activity Saved"})
        else:
            return JsonResponse({"message":"Not Logged In"})