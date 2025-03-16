from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    sales1 = float(data.get('sales1', 0))
    sales2 = float(data.get('sales2', 0))

    average_sales = (sales1 + sales2) / 2

    return jsonify({'average': average_sales})

if __name__ == '__main__':
    app.run(debug=True)