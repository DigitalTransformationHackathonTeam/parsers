import json

url_beginning = "https://cian.ru/map/?deal_type=sale&engine_version=2&in_polygon%5B1%5D="
url_end = "&offer_type=flat&polygon_name%5B1%5D=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BF%D0%BE%D0%B8%D1%81" \
          "%D0%BA%D0%B0&room1=1&room2=1"

with open("polygon.json", "r") as read_file:
    data = json.load(read_file)

coordinates = data["geometry"]["coordinates"]

for polygon in coordinates:
    url = ''
    for x, y in polygon:
        cord_block = str(x) + "_" + str(y) + "%2C"
        url += cord_block

    url = url[:-3]
    url = url_beginning + url
    url += url_end
    print(url)
