# Product Service
# Import framework
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
from json2xml import json2xml, readfromurl, readfromstring, readfromjson

# Instantiate the app
app = Flask(__name__)
api = Api(app)

PRODUCTS = [
  'Ice cream',
  'Chocolate',
  'Fruit',
  'Eggs'
]

class Products(Resource):
  def get(self):
    format = request.args.get('format')
    if (format == 'xml'):
      return json2xml.Json2xml(PRODUCTS, wrapper="custom").to_xml()
    
    return PRODUCTS

producto=Products()  
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
api.add_resource(Products, '/productos')




# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)