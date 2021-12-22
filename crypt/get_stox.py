from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'BTC,NU,OGN',
  'convert':'EUR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'NO!',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

data = json.loads(response.text)

print("<html><head><style>body {font-family: \"Open Sans\";}</style> <title>Swans Crypto Züg</title></head><body>")
print("<table style=\"text-align:left;margin:10px\" cellpadding=\"5\">")
print("<tr><th>Name</th><th>Value</th><th colsapn=\"6\">Changes</th></tr>")
for key in data["data"]:
    #print("this key: " + key)
    name = data["data"][key]["name"]
    price = data["data"][key]["quote"]["EUR"]["price"]
    change1h = data["data"][key]["quote"]["EUR"]["percent_change_1h"]
    change24h = data["data"][key]["quote"]["EUR"]["percent_change_24h"]
    change7d = data["data"][key]["quote"]["EUR"]["percent_change_7d"]
    change30d = data["data"][key]["quote"]["EUR"]["percent_change_30d"]
    change60d = data["data"][key]["quote"]["EUR"]["percent_change_60d"]
    change90d = data["data"][key]["quote"]["EUR"]["percent_change_90d"]
    print("<tr><td>{}</td><td>{:0.2f}€</td><td>last 1h: {:0.2f}%</td><td>last 24h: {:0.2f}%</td><td>last 7d: {:0.2f}%</td><td>last 30d: {:0.2f}%</td><td>last 60d: {:0.2f}%</td><td>last 90d: {:0.2f}%</td></tr>".format(name, price, change1h, change24h, change7d, change30d, change60d, change90d))
print("</table>")
print("Updated: " + str(data["data"]["BTC"]["last_updated"]))
print("</body></html>")
