import requests
import json

url = "https://api.thecatapi.com/v1/images/search"

querystring = {"format":"json"}

headers = {
    'Content-Type': "application/json",
    'x-api-key': "03348381-7b4a-451d-a0cc-6828625a9c55"
    }

data = requests.request("GET", url, headers=headers, params=querystring).text
jsonObj = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)
datas=[]

numOfCats = int(op("NumOfImage").text)
for i in range(numOfCats):
	datas.append(json.loads(requests.request("GET", url, headers=headers, params=querystring).text)[0])

myDict = {"Cat":datas}

op("JsonFormatter_Cat").text = json.dumps(myDict,sort_keys=True, indent = 4)
jsonObj = json.loads(op("JsonFormatter_Cat").text)

titles = ["Cat","Url"]

jsonObjLength = len(jsonObj["Cat"])

op("CatTable").setSize(jsonObjLength+1,len(titles))

for i in range(len(titles)):
	op("CatTable")[0,i] = titles[i]

for i in range(jsonObjLength):
	op("CatTable")[i+1,0] = i+1
	op("CatTable")[i+1,1] = jsonObj["Cat"][i]["url"]