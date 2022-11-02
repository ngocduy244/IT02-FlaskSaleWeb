# import json
# from saleapp import app
from saleapp.models import Category, Product


def load_categories():
    # with open(f"{app.root_path}/data/category.json", encoding="UTF-8") as f:
    #     return json.load(f)
    return Category.query.all()

def load_product(category_id = None, kw=None):
    # with open(f"{app.root_path}/data/product.json", encoding="UTF-8") as f:
    #     products = json.load(f)
    # if category_id:
    #     products = [p for p in products if p['category_id'] == int(category_id)]
    # return products
    query = Product.query.filter(Product.active.__eq__(True))

    if(category_id):
        query = query.filter(Product.category_id.__eq__(category_id))

    if(kw):
        query = query.filter(Product.name.contains(kw))

    return query.all();

def get_product_id(product_id):
    return Product.query.get(product_id)