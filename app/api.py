# Product Service
# Import framework
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import xmltodict

# Instantiate the app
app = Flask(__name__)
api = Api(app)

print("api running")


class Product(Resource):
    def get(self):
        return {
            'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs']
        }

@app.route('/Loco', methods=['GET', 'POST'])
def Loco():

    if request.method == 'GET':
        content_dict = xmltodict.parse(Product)
        print(Product)
        print(content_dict)
        return jsonify(Product)
    else:
        if request.method == 'POST':
            xml_data = request.form['SomeKey']
            content_dict = xmltodict.parse(xml_data)
            print(Product)
            print(content_dict)
            return jsonify(content_dict)
        else:
            print ('La manquie')

# Create routes
api.add_resource(Product, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

