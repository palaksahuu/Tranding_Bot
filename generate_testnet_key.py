import requests

url = "https://testnet.binancefuture.com/fapi/v1/listenKey"

response = requests.post(url)

print(response.text)