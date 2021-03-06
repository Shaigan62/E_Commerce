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
    product_indices = []
    for pro in title:
        try:
            idx = indices[pro]
            idx = idx.iloc[0]
        except Exception:
            idx = indices[pro]
        sim_scores = list(enumerate(cosine_sim2[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:int(10/len(title))+1]
        ind = [i[0] for i in sim_scores]
        product_indices.extend(ind)

    return df['name'].iloc[product_indices]


class RecommendProduct(APIView):
    def get(self,request,*args,**kwargs):
        current_user = request.user
        if current_user.is_authenticated:
            activity = user_activity.objects.filter(user_id=current_user.id).order_by('-activity_time')[:3]
            if activity:
                product_name = [x.product_id.name for x in activity]
                result = get_recommendations(product_name).tolist()
                recommended_products = Product.objects.filter(name__in=result)
                final_data = ProductDetailsSerializer(recommended_products,many=True)
                return Response(final_data.data)
                # return JsonResponse({"message": "Logged In"})
            else:
                product_top = (Product.objects
                               .order_by('-user_clicks')
                               )[:5]
                final_data = ProductDetailsSerializer(product_top, many=True)
                return Response(final_data.data)

        else:
            product_top = (Product.objects
                           .order_by('-user_clicks')
                           )[:5]
            final_data = ProductDetailsSerializer(product_top,many=True)
            return Response(final_data.data)

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