from flask import render_template, request
from saleapp import app, dao


@app.route('/')
def index():
    categories = dao.load_categories()
    product = dao.load_product(category_id=request.args.get('category_id'))
    return render_template('index.html', categories=categories, product=product)


if(__name__ == "__main__"):
    app.run(debug=True)