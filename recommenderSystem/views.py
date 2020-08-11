from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from products.models import Product,Category,Brand



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

