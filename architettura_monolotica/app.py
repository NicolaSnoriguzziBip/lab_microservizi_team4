from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
  if request.method == 'POST':
    #UPDATE Users
    return jsonify(request.json), 201
  return jsonify(users)

@app.route('/products', methods=['GET', 'POST'])
def manage_products():
  if request.method == 'POST':
  #UPDATE Products
    return jsonify(request.json), 201
  return jsonify(products)

@app.route('/orders', methods=['GET', 'POST'])
def manage_orders():
  if request.method == 'POST':
  #UPDATE Orders
    return jsonify(request.json), 201
  return jsonify(orders)

if __name__ == '__main__':
  app.run(debug=True)
