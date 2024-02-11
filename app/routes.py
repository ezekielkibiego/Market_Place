from flask import render_template, redirect, url_for,flash
from app import app
from app.models import Product, db
from .forms import ProductForm



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        # Access form data
        name = form.name.data
        description = form.description.data
        price = form.price.data
        
        # Create a new product
        new_product = Product(name=name, description=description, price=price)
        
        # Add the new product to the database
        db.session.add(new_product)
        db.session.commit()
        
        flash('Product added successfully!', 'success')  # Flash message
        return redirect(url_for('products'))  # Redirect to product list page after adding product
    return render_template('add_product.html', form=form)
