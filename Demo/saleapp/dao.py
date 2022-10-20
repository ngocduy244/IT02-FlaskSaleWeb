import json
from saleapp import app


def load_categories():
    with open(f"{app.root_path}/data/category.json", encoding="UTF-8") as f:
        return json.load(f)

def load_product(category_id = None):
    with open(f"{app.root_path}/data/product.json", encoding="UTF-8") as f:
        products = json.load(f)
    if category_id:
        products = [p for p in products if p['category_id'] == int(category_id)]
    return products
