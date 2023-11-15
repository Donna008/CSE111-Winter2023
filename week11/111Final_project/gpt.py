from tkinter import *
import requests
from PIL import Image, ImageTk
import json
from datetime import datetime
import urllib.request
from io import BytesIO
from tkinter import messagebox

# Initialize Window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Weather App')

city_value = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def get_weather_icon(icon_code):
    with open('weather icon.txt','r') as f:
        for line in f:
            values= line.strip().split(',')
            if values[0] == icon_code:
                url = values[1]
                response = requests.get(url)
                img_data = response.content
                img = Image.open(BytesIO(img_data))
                return ImageTk.PhotoImage(img.resize((80,80)))
    return None

def showWeather():

    # Enter your API key.
    api_key = "f34690199ee5de4a0cf25cee69142cb3" # API

    # Get city name from user from the input field
    city_name = city_value.get()

    # API url
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    # Get the response from fetched url
    response = requests.get(weather_url)

    # changing response from json to python readable
    weather_info = response.json()
    try:
        icon_code = weather_info['weather'][0]['icon']
    
        icon = get_weather_icon(icon_code)
    
        tfield.delete('1.0', 'end') # to clear the text field for every new output

    # as per API documentation, if the code is 200, it means that weather data was successfully fetched
        if weather_info['cod'] == 200:
            kelvin = 273 # value of kelvin

            # storing the fetched values of weather of a city
            temp = int(weather_info['main']['temp'] - kelvin)
            feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            wind_speed = weather_info['wind']['speed'] * 3.6
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']

            sunrise_time = time_format_for_location(sunrise + timezone)
            sunset_time = time_format_for_location(sunset + timezone)

            # assigning Values to our weather variable, to display as output
            weather = f'\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHunmidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}'
            # tfield.insert('end', weather)
        
            if icon:
                # display weather icon
                icon_label = Label(root, image=icon)
                icon_label.image = icon  # prevent image from being garbage collected
                icon_label.place(relx=0.7, rely=0.2, anchor=NW, y=-8)
                icon_label.lift()  # move label to front

        else:
            messagebox.showerror('Error', f'Weather for "{city_name}" not found!\nKindly enter a valid city name.')
            city_value.set('')
            weather = f'\n\tWeather for "{city_name}" not found!\n\tKindly valid City Name !!'
    
    
        tfield.insert(INSERT,weather) # to insert or send value in our Text Filed to display output
    except KeyError:
        # if there is any KeyError (weather information not found), delete input field, show error message
        tfield.delete('1.0', END)
        message = f"Error: City not found. Please enter a valid city name."
        city_value.set("")
        tfield.insert(END, message)

# Frontend part of code - interface
city_head = Label(root,text='Enter City Name',font='Arial 12 bold').pack(pady=10) # to generate label heading
inp_city = Entry(root,textvariable=city_value, width=24, font='Arial 14 bold').pack()

Button(root,command=showWeather,text='Check Weather', width=10,font='Arial 10', bg='lightblue', fg='black', activebackground='teal',padx=5,pady=5).pack(pady=20)

# to show output
weather_now = Label(root,text='The Weather is:', font='Arial 12 bold').pack(pady=10)
tfield=Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()
