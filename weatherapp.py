def window():
	ui = tkinter.Tk()
	ui.geometry('300x250+550+200')
	L1 = tkinter.Label(text = "Locate City")
	L1.pack()
	E1 = tkinter.Entry(width=45)
	E1.pack()
	go = tkinter.Button(master = ui, text = "Search", command = lambda: yahooweather(E1.get()))
	go.pack()
	ui.mainloop()
def yahooweather(name):
	baseurl = "https://query.yahooapis.com/v1/public/yql?"
	yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\""+ name +"\")"
	yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
	result = urllib.request.urlopen(yql_url).read()
	data = json.loads(result)
	print (data['query']['results'])
	city = data['query']['results']['channel']["location"]["city"]
	country = data['query']['results']['channel']["location"]["country"]
	temp = data['query']['results']['channel']["item"]["condition"]["temp"] + "º F"
	tex = data['query']['results']['channel']["item"]["condition"]["text"]
	datentime = data['query']['results']['channel']["lastBuildDate"]

	print (data['query']['results']['channel']["location"]["city"])
	print (data['query']['results']['channel']["location"]["country"])
	print (data['query']['results']['channel']["item"]["condition"]["temp"] + "F")
	print (data['query']['results']['channel']["item"]["condition"]["text"])
	print (data['query']['results']['channel']["lastBuildDate"])
	details(city, country, temp, tex, datentime)

def details(city, country, temp, tex, time):
	c = tkinter.Label(text = city + ", "+ country)
	tem = tkinter.Label(text = temp)
	txt = tkinter.Label(text = tex)
	datentime = tkinter.Label(text = time)
	c.pack()
	tem.pack()
	txt.pack()
	datentime.pack()



import tkinter
import urllib.parse, urllib.request, json
city = "No city Selected yet!"

window()
