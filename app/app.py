# File path: app/app.py
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Model: Simple Product class for demonstration
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

# Controller: Handling form submissions
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        
        # Server-side validation (in addition to client-side JavaScript validation)
        if not name or not price or not description:
            flash('All fields are required!')
            return redirect(url_for('index'))
        
        try:
            price = float(price)
        except ValueError:
            flash('Price must be a valid number!')
            return redirect(url_for('index'))

        # Save the product (In real-world, this would involve saving to a database)
        product = Product(name, price, description)
        flash(f'Product {product.name} added successfully!')
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
