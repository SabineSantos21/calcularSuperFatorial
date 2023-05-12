from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"*": {"origins": "*"}})

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def super_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result


@app.route('/superfactorial/<int:n>', methods=['GET'])
def calculate_super_factorial(n):
    result = super_factorial(n)
    return jsonify({'number': n, 'superfactorial': result})


if __name__ == '__main__':
    app.run()