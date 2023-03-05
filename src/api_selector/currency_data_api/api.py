""" 
this is logic with request module consumer api 
:tokens request 100
:access_key default (MdWi6mnaCJhCjlVZigIfiKqThnKKYq2f)
"""

from requests import request
access_key = "MdWi6mnaCJhCjlVZigIfiKqThnKKYq2f"
from_convert = "COP"
to_convert = "USD"
amount = 1

url = f"https://api.apilayer.com/currency_data/convert?to={from_convert}&from={to_convert}&amount={amount}"

payload = {}
headers= {
  "apikey": access_key
}

response = request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if status_code == 200:
    result = response.json()
    print(type(result))
    result = result['result']
    print(result)
else:
    print("algo salio mal")