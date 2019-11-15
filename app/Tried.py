import requests
url='[REQUEST URL]'
headers = {'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': 'uri:FlexForce/wsdlGetEmployees'}
body = """<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:uri="uri:FlexForce">
<soapenv:Header/>
   <soapenv:Body>
      <uri:wsdlGetEmployees soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <apiKey xsi:type="xsd:string">xxxx-xxxx-xxxx-xxxx</apiKey>
      </uri:wsdlGetEmployees>
   </soapenv:Body>
</soapenv:Envelope>"""
response = requests.post(url,data=body,headers=headers)
content=response.content

import pandas as pd
import xml.etree.ElementTree as ET
#parses the raw response into an ElementTree object
etree = ET.fromstring(content)

def iter_employees(xml_etree):
    #this selects elements in the xml until we get to the return node
    #which contains the items, then we iterate over the items
    for each in xml_etree[0][0][0].iter('item'):
        #for each item, we add to a dictionary the tag and text as a key:value pair
        #while iterating over all tags present
        my_dict={}
        for info in list(each):
            my_dict[info.tag]=info.text
        #yielding the dictionary allows this function to provide a list of dictionaries
        yield my_dict

#we create the dataframe using the above function to pass a list of the dictionaries
#to the initialising function. The keys become the column names and the values the content
df=pd.DataFrame(list(iter_employees(etree)))