import requests

url = "https://shaisachs-mortgage-payments-v1.p.rapidapi.com/payments"

querystring = {"interestRate":"0.04","downPayment":"30000","price":"300000"}

headers = {
    'x-rapidapi-host': "shaisachs-mortgage-payments-v1.p.rapidapi.com",
    'x-rapidapi-key': "cba65cdf61msh4c69a4a815aef5cp176ea1jsn49d720f1edc2"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
