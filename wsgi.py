from flask import Flask, jsonify, render_template
import requests


app = Flask(__name__)

@app.route ('/', methods=['GET'])
def home():
	return "Hello" 

@app.route ('/get_weather', methods=['GET'])
def get_weather():
	baseurl = "https://query.yahooapis.com/v1/public/yql?"
	yql_query = "q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%2214228%22)"
	yql_url =  baseurl + yql_query + "&format=json"
	current = requests.get(yql_url).json()
	condition = current.get('query').get('results').get('channel').get('item').get('condition')
	temp = condition.get('temp')
	desc = condition.get('text')
	
	yql_query = 'q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%2214086%22)'
	yql_url = baseurl + yql_query + '&format=json'
	forecast = requests.get(yql_url).json()
	todays_forecast = forecast.get('query').get('results').get('channel').get('item').get('forecast')[0]
	low = todays_forecast.get('low')
	high = todays_forecast.get('high')

	return jsonify({"temp" : temp, "desc" : desc, "low" : low, "high" : high})	


if __name__ == '__main__':
	app.run()
