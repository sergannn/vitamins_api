import requests
from requests.structures import CaseInsensitiveDict

url = "https://store.tildacdn.com/api/getproductslist/?storepartuid=328080061611&recid=616600488&c=1695901425189&getparts=true&getoptions=true&slice=1&size=36"

headers = CaseInsensitiveDict()
headers["authority"] = "store.tildacdn.com"
headers["accept"] = "*/*"
headers["accept-language"] = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,tg;q=0.6"
headers["origin"] = "https://nmd-vitamins.ru"
headers["referer"] = "https://nmd-vitamins.ru/"
#headers["sec-ch-ua"] = ""Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117""
headers["sec-ch-ua-mobile"] = "?0"
#headers["sec-ch-ua-platform"] = ""macOS""
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "cross-site"
headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"


resp = requests.get(url, headers=headers)
print(resp.content)
#print(resp.status_code)

