import requests

endpoint= "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
headers ={
         'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
         'x-rapidapi-key': "aa346f947dmsh9d5969225d14912p11e3e2jsn60dafdc1e4de"
         }
response = requests.request("GET", endpoint, headers=headers)
print(response.text)
# g=pandas.DataFrame(file)
# g.to_csv(index=False)

