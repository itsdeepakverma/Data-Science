"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
stringjson="""
            {
	"Faculty": {
		"Faculty 1": {
			"First Name": "Deepak",
			"Last Name": "Verma",
			"Photo": "https://jsonlint.com",
			"Department": "Computer",
			"Research area": "Image",
			"contact Details": {
				"Email": "xyz@gmail.com",
				"Phone": ["9123456780", "123456789"]
			}
		},
		"Faculty 2": {
			"First Name": "Vijay",
			"Last Name": "Sharma",
			"Photo": "https://jsonlint.com",
			"Department": "Computer",
			"Research Area": "ECE",
			"contact Details": {
				"Email": "abc@gmail.com",
				"phone": ["9214077791", "9214077781"]
			}

		}
	}
}
"""
import json
mydata=json.loads(stringjson)

print(mydata['Faculty']['Faculty 2']['contact Details']['phone'][0])

stringjson="""
            {
	"Student": {
		"Student 1": {
			"First Name": "Deepak",
			"Last Name": "Verma",
			"Photo": "https://jsonlint.com",
			"Department": "Computer",
			"Year": "First year",
			"contact Details": {
				"Email": "xyz@gmail.com",
				"Phone": ["9123456780", "123456789"]
			}
		},
		"Student 2": {
			"First Name": "Vijay",
			"Last Name": "Sharma",
			"Photo": "https://jsonlint.com",
			"Department": "Computer",
			"Year": "Second Year",
			"contact Details": {
				"Email": "abc@gmail.com",
				"phone": ["9214077791", "9214077781"]
			}

		}
	}
}
"""
mydata=json.loads(stringjson)

print(mydata['Student']['Student 2']['contact Details'])

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
url="http://api.openweathermap.org/data/2.5/weather?q=jaipur&APPID=e9185b28e9969fb7a300801eb026de9c"
import requests

responce=requests.get(url)

responce.content
print(type(responce.content))

print("Content :" + str(responce.content))

jsondata=responce.json()

print(jsondata,indent=2)

print(jsondata['coord'])
print(jsondata['weather'][0]['main'])
print(jsondata['wind'])
print(jsondata['sys']['sunrise'])
print(jsondata['sys']['sunset'])

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
url='https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=3cfce8edd3f670ee5c37'
import requests    
res=requests.get(url)
jsondata=res.json()
print(type(jsondata['USD_INR']))

usd=float(input("enter usd to convert in INR"))

print("INR={}".format(jsondata['USD_INR'] * usd))


# Code Challenge

"""
Research the below wesbite and post some data on it
https://requestbin.com
"""
import json
import requests

Host = "https://requestbin.com/post"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )

def get_method():
    response = requests.get("http://requestbin/get?firstname=Dev&language=English")
    return response

print (get_method().text)




# Code Challenge

"""
Create a client REST API that sends and receives some information from the Server by calling server's REST API.
You are expected to create two functions each for Sending and Receiving data.

    You need to make two api calls, one with POST method for sending data and the other with GET method to receive data

    All the communication i.e. sending and receiving of data with the server has to be in JSON format

    First send the data to cloud using the "http://13.127.155.43/api_v0.1/sending" api with the following fields (Field names should be same as shown ):
            Phone_Number (pass phone number as string and not as integer)
            Name
            College_Name
            Branch

    Now receive the data from cloud using the "http://13.127.155.43/api_v0.1/receiving" api with     
    “Phone_Number” along with the number you are looking for as query parameter
    Print the server responses from both the cases. 
   
    The first one will give response-code : 200 and response-message : "Data added Successfully", if all goes well. 
    The second one will give all the details stored with the phone number you provided as query parameter. 
    Both the responses will be in JSON format.
    
"""