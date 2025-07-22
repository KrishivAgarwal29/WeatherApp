from flask import Flask, render_template, request
import requests
# initialising flask
app=Flask(__name__)
#directing the web page to perform function
@app.route("/")

def visitors():
	#load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file_close = counter_read_file.close()
	#increment count
	visitors_count = visitors_count + 1
	#overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()
	#render htlml with count variable
	return render_template("Index.html", count=visitors_count)

@app.route("/", methods=['POST'])

def weather_stats():
	#load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file_close = counter_read_file.close()
	latitude = request.form['latitude']
	longitude = request.form['longitude'] 
	api_url = 'https://weather-l6tl.onrender.com/api/getCurrentWeather/' + latitude + '/' + longitude
	response = requests.get(api_url)
	weather_data=response.json()
	print(weather_data)
	return render_template("Index.html", weather=weather_data, count=visitors_count)

if __name__ == "__main__":
	app.run()
