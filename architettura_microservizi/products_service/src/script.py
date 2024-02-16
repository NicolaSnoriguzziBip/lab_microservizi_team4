# products_service.py

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/products', methods=['GET', 'POST'])
def manage_products():
    """
    This function handles the management of products.
    
    If the request method is POST, it updates the products and returns the updated products as a JSON response.
    
    If the request method is GET, it returns the list of products as a JSON response.
    """
    if request.method == 'POST':
        # UPDATE Products
        return jsonify(request.json), 201
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
