from suds.client import Client
client = Client('http://localhost:8181/soap/helloservice?wsdl', username='bob', password='catbob')
result = client.service.sayHello('bob')