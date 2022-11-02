from flask import render_template, request
from saleapp import app, dao



@app.route('/')
def index():
    categories = dao.load_categories()
    product = dao.load_product(category_id=request.args.get('category_id'),
                               kw=request.args.get('keyword'))
    return render_template('index.html', categories=categories, product=product)


@app.route('/products/<int:product_id>')
def details(product_id):
    p = dao.get_product_id(product_id)
    return render_template('details.html', product=p)



if(__name__ == "__main__"):
    app.run(debug=True)