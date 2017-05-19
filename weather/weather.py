import yweather

client = yweather.Client()
data = client.fetch_woeid("Bangkok")
weather = client.fetch_weather(data, metric=True)
forecasth = weather["forecast"][0]["high"]
atmosz = weather["atmosphere"]["humidity"]
print "Bangkok Thailand : %s" % forecasth
print "Atmosphere : %s" % atmosz
print weather["forecast"][0]["text"]

print weather["forecast"][0]

print weather["title"]
print weather["location"]