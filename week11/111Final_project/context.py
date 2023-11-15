def adventure_game():
    """
    An adventure game.
    """
    print("Welcome to the Adventure game!")
    item = select_item()
    if item == "match":
        handle_match_choice()
    elif item == "flashlight":
        handle_flashlight_choice()

def select_item():
    while True:
        item = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ").lower()
        if item == "match" or item == "flashlight":
            return item
        else:
            print("Sorry, that's not a valid choice. Please try again.")

def handle_match_choice():
    choice = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ").lower()
    if choice == "run":
        handle_run_choice()
    elif choice == "hide":
        handle_hide_choice()
    else:
        print("Sorry, that's not a valid choice. Please try again.")

def handle_run_choice():
    print("You've been running for a long time, you're out of breath, and suddenly you find yourself in a forest, when you suddenly hear a strange noise in the grass ahead.")
    choice = input("Do you want to go up and CHECK IT OUT or KEEP RUNNING? ").lower()
    if choice == "check it out":
        handle_check_it_out_choice()
    elif choice == "keep running":
        handle_keep_running_choice()
    else:
        print("Sorry, that's not a valid choice. Please try again.")

def handle_check_it_out_choice():
    print("You decide to go up to investigate the situation, and find that it is a wild boar sound, when the boar found you, the boar suddenly ran forward. ")
    choice = input("You decide to stay where you are or follow the direction of the boar running? ").lower()
    if choice == "go up and see":
        go_up_and_see_choice()
    elif choice == "ignore it":
        ignore_it_choice()
    else:
        print("Sorry, that's not a valid choice. Please try again.")

def handle_keep_running_choice():
    print("You hear the noise and are afraid that it is a wild animal, so you continue to run away. When you really can't run, you decide to stop and rest for a while. At this point you seem to hear the sound of singing not far away, ")
    choice = input("you decide to go up to see where the song is coming from or ignore it. ").lower()
    if choice == "go up and see":
        go_up_and_see_choice()
    elif choice == "ignore it":
        ignore_it_choice()
    else:
        print("Sorry, that's not a valid choice. Please try again.")

def go_up_and_see_choice():
    print("You boldly go up to know how this wilderness singing, while wondering while going forward, over the hill and found a piece of paradise, ")
    choice = input("you decided to enter this peach garden or return to the original place. ").lower()
    if choice == "enter":
        enter_the_paradice()
    elif choice == "return":
        return_to_original_place_choice()
    else:
        print("Sorry, that's not a valid choice. Please try again.")

def ignore_it_choice():
    print("You think you are too tired, in case this song is something bad such as from")

def handle_start_choice():
    print("You find yourself standing in the middle of a dense forest. You can see a narrow path to your left and a winding road to your right. Which path do you choose?")
    choice = input("Enter 1 to take the narrow path or 2 to take the winding road: ")
    if choice == "1":
        enter_the_paradise()
    elif choice == "2":
        print("You start walking down the winding road. After a few minutes, you come across a matchbox lying on the ground.")
        handle_match_choice()
    else:
        print("Invalid choice. Please try again.")
        handle_start_choice()

def enter_the_paradise():
    print("You take the narrow path and it leads you to a beautiful paradise. Enjoy your stay!")

def handle_match_choice():
    print("What do you do with the matchbox?")
    choice = input("Enter 1 to light a match or 2 to check it out: ")
    if choice == "1":
        print("You light a match and the whole area lights up. You see a path that was not visible before. Do you take it?")
        interesting_road_choice()
    elif choice == "2":
        handle_check_it_out_choice()
    else:
        print("Invalid choice. Please try again.")
        handle_match_choice()

def handle_check_it_out_choice():
    print("You check out the matchbox and find a key inside. You don't know what it's for, but it seems important. You continue down the winding road.")
    the_path_that_looks_eerie_choice()

def interesting_road_choice():
    choice = input("Enter 1 to take the interesting road or 2 to continue down the winding road: ")
    if choice == "1":
        print("You take the interesting road and discover a treasure chest. Congratulations!")
    elif choice == "2":
        print("You continue down the winding road.")
        the_path_that_looks_eerie_choice()
    else:
        print("Invalid choice. Please try again.")
        interesting_road_choice()

def the_path_that_looks_eerie_choice():
    print("You come across a path that looks eerie. Do you continue or turn back?")
    choice = input("Enter 1 to continue or 2 to turn back: ")
    if choice == "1":
        print("You continue down the path and eventually come to a dead end. You turn back and continue down the winding road.")
    elif choice == "2":
        print("You turn back and continue down the winding road.")
    else:
        print("Invalid choice. Please try again.")
        the_path_that_looks_eerie_choice()

handle_start_choice()

