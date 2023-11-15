import time
import random
import string
# flower import
import turtle as T
import random
import time
# weather import
from tkinter import *
import requests
from PIL import Image, ImageTk
import json
from datetime import datetime
import urllib.request
from io import BytesIO
from tkinter import messagebox

def main():
    """
    The main function that drives the program.
    """
    try:
        while True:
            game_menu()
            number = input('Please enter an action: ')
            if number == "1":
                print("Welcome to the Word Guessing Game!")
                print("The goal of the game is to guess the secret 5-letter word, one letter at a time.")
                print("You have a maximum of 5 guesses. After each guess, the game will give you a hint to help you guess the next letter.")
                print("If you want to quit the game at any time, type 'quit' or 'exit'.")
                guess_fiveth_word()
            
            elif number == "2":
                adventure_game()
            elif number == "3":
                print("Welcome to the Weather tools! You can tyoe anywhere of the city name, and I will show you the weather information of the city.")
                weather()
            elif number == "4":
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
    except Exception as error:
        print(f'An error occured: {error}')
     

def game_menu():
    """
    Display the game menu to the user.
    """
    menu = [
        "\nWelcome to the games list, there have three game you can choice, just type the number of the menu, have fun!"
        "\nIf you want to quit the game at any time, type 4.",
        "1. Guess word",
        "2. Adventure game",
        "3. Weather tool",
        "4. Quit"
    ]
    for k in menu:
        print(k)    
def get_hint(word, guess_word):
    hint = ''
    for i in range(len(word)):
        if guess_word[i] == word[i]:
            hint += guess_word[i].upper() + ' '
        elif guess_word[i] in word:
            hint += guess_word[i].lower() + ' '
        else:
            hint += '_ '
    return hint

def get_guess_word(word, time_limit):
    start_time = time.time()
    while True:
        guess_word = input("Please enter a word: ").lower()
        if guess_word in ['quit', 'exit']:
            return None
        if (time.time()-start_time) > time_limit:
            print("Sorry, you ran out of time.")
            return None
        if len(guess_word) != len(word):
            print(f"Hint: The word should be {len(word)} letters long.")
            continue
        return guess_word

def generate_word(length, complexity):
    # Open the file 'word.txt' and read all lines from it, stripping the newline characters and creating a list of words.
    with open('word.txt', 'r') as f:
        words = [w.strip() for w in f.readlines()]
    # Check if there are any words in the list of words. If there are no words, return None.
    if words:
    # Filter the list of words to only include words that have the desired length.
        words = [w for w in words if len(w) == length]
    # Filter the list of words to only include words that have enough unique characters to meet the desired complexity.
        words = [w for w in words if len(set(w)) >= length * complexity]
    # Check if there are any words left in the list of words after filtering. If there are no words, return None.   
        if words:
        # Choose a random word from the filtered list of words and return it.
            return random.choice(words)    
    return None
# limit the word length 
def guess_fiveth_word(word_length=5, complexity=0.5, max_guesses=5, time_limit=10):
    guess_count = 0
    
    word = generate_word(word_length, complexity)
    if word is None:
        return
    print("Your hint is:", "_ "*len(word))
    start_time = time.time()
    while True:
        guess_word = get_guess_word(word, time_limit)
        if guess_word is None:
            print(f"Sorry to see you go! The word was '{word}'.")
            return
        guess_count += 1
        if guess_word == word:
            print(f"Congratulations! It took you {guess_count} guess(es).")
            break
        if guess_count >= max_guesses:
            print(f"Sorry, you ran out of guesses. The word was '{word}'.")
            break
        print("Your hint is:", get_hint(word, guess_word))


def show_word_by_word(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1) # adjust the words speed, 1 is very quickly


def adventure_game():
    show_word_by_word("\nWelcome to the adventure game!\nThis game have different end which depend your choice, maybe you will meet a picture, maybe not, goodluck!\n")
    item = select_item()
    if item == "match":
        handle_match_choice()
    elif item == "flashlight":
        handle_flashlight_choice()
    return
def select_item():
    while True:
        show_word_by_word("\nYou are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")
        item = input().lower()
        if item == "match" or item == "flashlight":
            return item
        else:
            show_word_by_word("\nSorry, that's not a valid choice. Please try again.")

def handle_match_choice():
    show_word_by_word("\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ")
    choice = input().lower()
    if choice == "run":
        handle_run_choice()
        # if choice == "check it out":
        #     handle_check_it_out_choice
        # elif choice == "keep running":
        #     handle_keep_running_choice()
        # else:
        #     print("Sorry, that's not a valid choice. Please try again.")
    elif choice == "hide":
        handle_hide_choice()
    else:
        show_word_by_word("\nSorry, that's not a valid choice. Please try again.")
    return

def handle_run_choice():
    show_word_by_word("\nYou've been running for a long time, you're out of breath, and suddenly you find yourself in a forest, when you suddenly hear a strange noise in the grass ahead.")
    show_word_by_word("\nDo you want to go up and CHECK it out or KEEP running? ")
    choice = input().lower()
    if choice == "check":
        handle_check_it_out_choice()
    elif choice == "keep":
        handle_keep_running_choice()
    else:
        show_word_by_word("\nSorry, that's not a valid choice. Please try again.")
    return 

def handle_check_it_out_choice():
    show_word_by_word("\nYou decide to go up to investigate the situation, and find that it is a wild boar sound, when the boar found you, the boar suddenly ran forward. ")
    show_word_by_word("\nYou decide to STAY where you are or FOLLOW the direction of the boar running? ")
    choice = input().lower() # notice is correct or not the choice.
    if choice == "stay":
        ignore_it_choice()
    elif choice == "follow":
        go_up_and_see_choice()
    else:
        show_word_by_word("\nSorry, that's not a valid choice. Please try again.") 
    return 

def handle_keep_running_choice():
    show_word_by_word("\nYou hear the noise and are afraid that it is a wild animal, so you continue to run away. When you really can't run, you decide to stop and rest for a while. At this point you seem to hear the sound of singing not far away, ")
    show_word_by_word("\nyou decide to GO up to see where the song is coming from or IGNORE it. ")
    choice = input().lower()
    if choice == "go":
        go_up_and_see_choice()
    elif choice == "ignore":
        ignore_it_choice()
    else:
        show_word_by_word("\nSorry, that's not a valid choice. Please try again.")
    return 

def go_up_and_see_choice():
    show_word_by_word("\nYou boldly go up to know how this wilderness singing, while wondering while going forward, over the hill and found a piece of paradise, ")
    show_word_by_word("\nyou decided to ENTER the peach garden or RETURN to the original place.")
    choice = input().lower()
    if choice == "enter":
        enter_the_paradise()
    elif choice == "return":
        return_to_original_place_choice()
    else:
        show_word_by_word("\nSorry, that's not a valid choice. Please try again.")
    return 

def ignore_it_choice():
    show_word_by_word("\nYou think you are too tired, in case this song is something bad such as from a ghost, you don't have the strength to run away anymore, so you plan to rest first to recover your strength. But because of this you miss the things you are curious about.")
    return 

def enter_the_paradise():
    get_flower() # call turtle

def return_to_original_place_choice():
    show_word_by_word("\nyou are very worried about what you see is not the truth, do not dare to walk into, back to the place just rested for a while, you intend to get out of the forest. You see two forks in the road ahead,")
    show_word_by_word("\nyou choose a road looks INTERESTING, the road is full of flowers, or you choose looks very EERIE, dark road? ")
    choice = input().lower()
    if choice == "interesting":
        interesting_road_choice()
    elif choice == "eerie":
        the_path_that_looks_eerie_choice()
    else:
        show_word_by_word("\nSorry, that's not a valid choice. Please try again.")
    return
    # return choice

def interesting_road_choice():
    show_word_by_word("\nYou do not want to be afraid again, so you choose a relatively safe road, but when you walk in high spirits on the road, suddenly ah ~ fell into a trap, the trap is too high to cause you to climb out, you let out a cry for help but the place is sparsely populated, many days have passed, you have nothing to eat no water to drink and finally starved to death.")
    return 

def the_path_that_looks_eerie_choice():
    show_word_by_word("\nYou think in this forest is so strange, in the previous life never seen such a situation, maybe this can stumble upon the treasure. You are thinking while moving forward, but did not expect to be followed behind you, you walked and walked and found that the end of the road is a cliff, there is no road ahead to go, you feel cheated, decided to return, when you turned around and found a tiger behind you, has been following you.")
    return 


def handle_hide_choice():
    show_word_by_word("\nYou are too afraid of the bear, you decide to hide, wait for the bear to go away and then come out, you wait and wait, 2 hours have passed, the bear finally intends to go, you watch the bear slowly disappear, you exhale deeply, in these two hours you think a lot, you think you do not have the ability to go alone to adventure, and decided to return home.")
    return 

def handle_flashlight_choice():
    show_word_by_word("\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ").lower()
    choice = input().lower()
    if choice == "follow":
        handle_follow_choice()
        # if choice == "knock on the door":
        #     handle_knock_on_the_door_choice()
        # elif choice == "push the door and enter":
        #     handle_push_the_door_and_enter_choice()
        # else:
        #     print("Sorry, that's not a valid choice. Please try again.")
    elif choice == "look":
        handle_look_choice()
    else:
        show_word_by_word("\nSorry, that's not a valid choice. Please try again.")
    return

def handle_follow_choice():
    show_word_by_word("\nYou decide to follow the voice to see what it is, and maybe you will meet a fairy. Suddenly the sound stops and you wake up to find yourself deep in the desert. You think to yourself that you must have just met a fairy. You follow the herd of camels and find a house not far away. You go up to the door and find it closed.")
    choice = input
    show_word_by_word("\nYou decide KNOCK on the door or PUSH the door and enter? ")
    choice = input().lower()
    if choice == "knock":
        handle_knock_on_the_door_choice()
    elif choice == "push":
        handle_push_the_door_and_enter_choice()
    else:
        show_word_by_word("\nSorry, that's not a valid choice. Please try again.")
    return 

def handle_knock_on_the_door_choice():
    show_word_by_word("\nYou hold your voice and raise your hand to knock on the door, making the sound of a buckle, you wait for a while, the door slowly opens, in front of you is an old man of age, the old man invites you into the house to talk, you follow behind the old man, into the house, you look around and find a cage inside a tiger, the tiger looks familiar, but can not remember where to see. You feel scared, but you are lucky that you didn't push the door directly.At this point, the old man asks you where you came from, and you walk towards him and tell him what you have experienced.")
    return 

def handle_push_the_door_and_enter_choice():
    show_word_by_word("\nYou came to the door directly push the door and want to explore the situation, when you push open the door a black shadow pavement, you did not see what it is, this black shadow months to come closer and closer, suddenly you found the opposite of the black shadow is a tiger, but at this time it is too late to avoid.")
    return 

def handle_look_choice():
    show_word_by_word("\nYou stand and watch all this happen, you look at the bear that appears in front of you, your legs are powerless to walk, you watch the bear slowly coming towards you, you are very afraid, you want this is a dream, you believe more and more this is a dream, when the bear is closer and closer to you, you suddenly woke up, you open your eyes and look around to find in your bedroom, you wipe your face with your hands, sigh a sigh of relief! You think to yourself that it was a dream!")
    return 

def get_flower():
# draw tree body
    def Tree(branch, t):
        time.sleep(0)
        if branch > 3:
            if 8 <= branch <= 12:
                if random.randint(0, 2) == 0:
                    t.color('snow')  
                else:
                    t.color('lightcoral')  
                t.pensize(branch / 3)
            elif branch < 8:
                if random.randint(0, 1) == 0:
                    t.color('snow')
                else:
                    t.color('lightcoral')  
                t.pensize(branch / 2)
            else:
                t.color('sienna')  
                t.pensize(branch / 10)  # 6 #10
            t.forward(branch)
            a = 1.5 * random.random()
            t.right(20 * a)
            b = 1.5 * random.random()
            Tree(branch - 10 * b, t)
            t.left(40 * a)
            Tree(branch - 10 * b, t)
            t.right(20 * a)
            t.up()
            t.backward(branch)
            t.down()

    # Falling petals
    def Petal(m, t):
        for i in range(m):
            a = 200 - 400 * random.random()
            b = 10 - 20 * random.random()
            x, y = t.position()
            t.up()
            t.setposition(-350, y-280)  # Set the starting position to be near the bottom-left of the window
            t.down()
            t.forward(b)
            t.left(0)
            t.forward(a)
            t.color('lightcoral')  
            t.circle(3)
            t.up()
            t.backward(a)
            t.right(0)
            t.backward(b)

    # drawing part
    w = T.Screen()
    w.setup(800, 600)
    w.bgcolor('wheat')  # wheat小麦

    # create first turtle，and draw a flower
    t1 = T.Turtle()
    t1.up()
    t1.hideturtle()
    t1.getscreen().tracer(5, 0)
    t1.color('sienna')
    t1.setposition(-250, -200)
    t1.left(90)
    t1.up()
    t1.backward(150)
    t1.down()
    Tree(60, t1) # changed the branch number to 60

    # draw falling petals
    t3 = T.Turtle()
    t3.hideturtle()
    t3.getscreen().tracer(5, 0)
    t3.color('lightcoral')
    Petal(100, t3)
    time.sleep(1)
    T.bye()

def weather():
    """
    Weather tools.
    """
    # print("Welcome to the Weather tools! You can tyoe anywhere of the city name, and I will show you the weather information of the city.")
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
            message = f"Error: City not found. Please ente mr a valid city name."
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

if __name__ == '__main__':
    main()