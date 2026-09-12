from tkinter import *
import requests
import json


root = Tk()
root.title("Weather App")
root.geometry("600x100")
root.resizable(width=False, height=False)

def zipLookup():
  zip.get()

#How to connect to API Using tkinter. Go to AirNow API Account Request Page. [1] (https://docs.airnowapi.org/account/request/)

try:
  #Connect to API
  api_request = requests.get("https://www.airnowapi.org/aq/observation/current/racode/?format=application/json&reportingAreaCode=ga009&API_KEY=83171183-DB4E-495D-A8BA-C3AA0F23344A")
  
  api = json.loads(api_request.content)
  city = api[0]['reportingAreaName']
  quality = api[0]['nowcastAQI']
  category = api[0]['reportingAreaAgency']
  
  if category == "Good":
    weather_color = "green"
  elif category == "Moderate":
    weather_color = "brown"
  elif category == "Unhealthy for Sensitive Groups":
    weather_color = "yellow"
  elif category == "Unhealthy":
    weather_color = "blue"
  elif category == "Very Unhealthy":
      weather_color = "green"
  elif category == "Harzardous":
    weather_color = "red"

  root.configure(background=weather_color)

  myLabel = Label(root,text=city + " " + "Air Quality" + str(quality) + category,font=("Helvetica" , 20),background=weather_color)
  myLabel.pack()
except Exception as e:
  api = "Error..."

zip = Entry(root)
zip.pack()

zipButton = Button(root, text="Lookup Zipcode",command=zipLookup)
zipButton.pack()


root.mainloop()