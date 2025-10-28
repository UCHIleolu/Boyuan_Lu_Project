from song_functions import *

the_menu = {"L" : "List",
    "A" : "Add",
    "E" : "Edit",
    "D" : "Delete",
    "M" : "Show statistical data on",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program",}
all_songs = {
   "12332": {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
   },
   "14567": {
      "title": "Soul Meets Body",
      "artist": "Death Cab for Cutie",
      "length": "",
      "album": "Plans",
      "genre": ["indie pop", "indie rock"],
      "rating": 5,
      "released": "07/16/2005",
      "favorite": True,
      "uid":14567
      },
   "78210": {
      "title": "Fake Love",
      "artist": "BTS",
      "length": "04:02",
      "album": "",
      "genre": ["hip hop", "electro pop", "Korean pop"],
      "rating": 3,
      "released": "05/18/2018",
      "favorite": False,
      "uid":78210
      },
    "99105": {
      "title": "Foil",
      "artist": "'Weird Al' Yankovic",
      "length": "02:22",
      "album": "Mandatory Fun",
      "genre": ["pop", "parody"],
      "rating": 5,
      "released": "07/15/2014",
      "favorite": True,
      "uid": 99105
      }
}
allkeys = ["12332","14567","78210","99105"]
list_menu = {
    "A": "all songs - full",
    "B": "all songs - titles only",
    "F": "favorite songs",
    "G": "songs of a specific genre"
}

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}

opt = None

while True:
    print_main_menu(the_menu)
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper()
    
    if opt not in the_menu:
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'Q':
        print("Goodbye!\n")
        break
    elif opt == 'L':
        if all_songs == {}:
            print("WARNING: There is nothing to display!")
            input("::: Press Enter to continue")
            continue

        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_songs(all_songs, rating_map, show_id = True)
        elif subopt == 'B':
            print_songs(all_songs, rating_map, title_only = True)
        elif subopt == 'F':
            print_songs(all_songs, rating_map, fave = True)
        elif subopt == 'G':
            print_songs(all_songs, rating_map, get_genre = True)

           # ----------------------------------------------------------------
    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            song_info = []
            print("::: Enter each required field:")
            a_dict= {str(input("Title: ")),
                     str(input("Artist: ")),
                     str(input("Length (00:00 format): ")),
                     str(input("Album: ")),
                     str(input("Genre (separate them with commas): ")),
                     str(input("Rating (1-5): ")),
                     str(input("Release Date (MM/DD/YYYY format): ")),
                     str(input("Favorite (T/F): ")),
                     str(input("Unique ID: "))
                     }
            result = get_new_song(a_dict,rating_map, allkeys)
            if type(result) == dict:
                all_songs.update(a_list)
                print(f"Successfully added a new song!")
                print_song(result, rating_map)
            elif type(result) == tuple:
                print(f"WARNING: invalid data!")
                print(f"Error: {result[0]}")

            print("::: Would you like to add another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()
            input("::: Press Enter to continue")
            # ----------------------------------------------------------------
    elif opt == 'E':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}:
                print("WARNING: There is nothing to edit!")
                break
            print("::: Song list:")
            print_songs(all_songs, rating_map, title_only = True, show_id = True)
            print("::: Enter the song ID you wish to edit.")
            user_option = input("> ")
            if is_valid_uid(user_option, allkeys)== False: 
                subopt = get_selection("edit", all_songs[user_option], to_upper = False, go_back = True)
                if subopt == 'M': 
                    break
                print(f"::: Enter a new value for the field |{subopt}|") # TODO
                field_info = input("> ")
                result = edit_song(all_songs, user_option, rating_map, subopt, field_info, allkeys) #TODO
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")  # TODO
                    print_song(result, rating_map)  # TODO
                else: # edit_song() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  # TODO
                    print(f"The song was not updated.")
            else: # song ID is incorrect/invalid
                print(f"WARNING: |{user_option}| is an invalid song ID!")  # TODO

            print("::: Would you like to edit another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()
            input("::: Press Enter to continue")
            # ----------------------------------------------------------------
    elif opt == 'D':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == []:
                print("WARNING: There is nothing to delete!")
                break
            print(print_songs(all_songs, rating_map,title_only = True, show_id = True,))
            print("::: Which task would you like to delete?")
            print("X - Delete all tasks at once")
            print("::: OR Enter the number corresponding to the song ID")
            print("::: OR press 'M' to cancel and return to the main menu.")
            subopt = input("> ")

            if subopt != 'X' and subopt != 'M' and is_valid_uid(subopt, allkeys) == True:
                print(f'WARNING: |{subopt}| is an invalid song ID!')
            else:
                if subopt == 'M':
                    break
                elif subopt == 'X':
                    print('::: WARNING! Are you sure you want to delete ALL songs?')
                    print('::: Type Yes to continue the deletion.')
                    if input('> ') == 'Yes':
                        for sid, song in list(all_songs.items()):
                            all_songs.pop(sid)
                            print('Deleted all songs.')
                else:
                    print('Success!')
                    d = delete_song(all_songs, subopt)
                    print(f'Deleted the song |{d}|')

            print("::: Would you like to delete another song? Enter 'y' to continue.")
            continue_action = input("> ")
            continue_action = continue_action.lower()
            input("::: Press Enter to continue")
            # ----------------------------------------------------------------
    elif opt == "M":
        continue_action = 'y'
        while continue_action == 'y':
            print('::: What would you like to show statistical data on?')
            print('A - Mean value of all song ratings')
            print('B - Median value of all song ratings')
            print('C - Standard Deviation value of all song ratings')
            print('D - Histogram of all song ratings')
            print('::: Enter your selection')
            subopt = input('> ')
            do_stats(all_songs, subopt)
            print("Would you like to get different statistics? Enter 'y' to continue.")
            continue_action = input("> ")
            continue_action = continue_action.lower()
            # ----------------------------------------------------------------
    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            result = save_to_csv(all_songs, filename) # TODO: Call the function with appropriate inputs and capture the output
            if result == -1: # TODO
                print(f"WARNING: |{filename}| is an invalid file name!") # TODO
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the songs to |{filename}|")
                continue_action = 'n'
            input('::: Press Enter to continue')
    #--------------------------------------------------------------------------
    elif opt == 'R':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input('> ')
            result = load_from_csv(filename, all_songs, rating_map, allkeys)
            if result == None:
                print(f"WARNING: |{filename}| was not found!")
                print("::: Would you like to try again? Enter 'y' to try again.")
                continue_action = input("> ")
                continue_action = continue_action.lower()
            elif result == -1:
                print("WARNING: invalid input - must end with '.csv'")
                print("::: Would you like to try again? Enter 'y' to try again.")
                continue_action = input("   > ")
                continue_action = continue_action.lower()
            else:
                if result == []:
                    print(f"Successfully restored all songs from |filename|")
                    break
                else:
                    print(f"WARNING: |{filename}| contains invalid data!")
                    print(f"The following rows from the file were not loaded: \n{result}")
                    print("Would you like to try again? ")
                    continue_action = input("Enter 'y' to try again.\n> ")
                    continue_action = continue_action.lower()
            # ----------------------------------------------------------------
                
                    

           
print("Have a nice day!")

