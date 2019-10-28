# Product Service
# Import framework
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
from json2xml import json2xml, readfromurl, readfromstring, readfromjson

# Instantiate the app
app = Flask(__name__)
api = Api(app)

print("api running")


class Product(Resource):
    def get(self):
        return {
            'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs']
        }
producto=Product()
data = json.loads(
    '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
)
@app.route('/XML', methods=['GET', 'POST'])
def XML():
    if request.method == 'GET':
        return(json2xml.Json2xml(producto.get(), wrapper="custom").to_xml())
    elif request.method == 'POST':
        return (json2xml.Json2xml(producto.get()).to_xml())

# Create routes
api.add_resource(Product, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)