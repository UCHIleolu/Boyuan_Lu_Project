def print_main_menu(the_menu):
        """
        Given a dictionary `menu`,
        prints the keys and values as the
        formatted options of a menu.
        Adds additional prints for decoration
        and to output a question
        "What would you like to do?"       
        """
        for i in the_menu:
                print(i,':',the_menu[i])
        return ''

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None

    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def get_written_date(date_list):
    """
    The function ...
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month = month_names[int(date_list[0])]
    day = str(int(date_list[1]))
    date = month + ' ' + day + ', ' + str(date_list[2])
    return date


def print_song(song, rating_map, title_only = False, showid=False):
    """
    param: song (dict) - a single song dictionary
    param: rating_map (dict) - a dictionary object that is expected
            to have the string keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed for the
            rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the name of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the id number of the song is not displayed.
            Otherwise, displays the id number.

    returns: None; only prints the song values

    Helper functions:
    - get_written_date() to display the 'duedate' field
        You created a similar function in a previous lab.
    """
    if title_only == True and showid == False:
        if song['title'] == '':
            print(f"   TITLE: ")
        else:
            print(f"   TITLE: {song['title']}")
    elif title_only == True and showid == True:
        if song['title'] == '':
            print(f"      ID: {song['uid']} |   TITLE: ")
        else:
            print(f"      ID: {song['uid']} |   TITLE: {song['title']}")
    elif title_only == False and showid == True:
        if song['title'] =='':
            print(f"      ID: {song['uid']} |   TITLE: ")
        else:
            print(f"      ID: {song['uid']} |   TITLE: {song['title']}")
    else:
        if song['title'] == '':
            print(f"   TITLE: ")
        else:
            print(f"   TITLE: {song['title']}")
        


    if title_only == False:
        if song['artist'] == '':
            print(f"  ARTIST: ")
        else:
            print(f"  ARTIST: {song['artist']}")
        if song['length'] != '':
            print(f"  LENGTH: {song['length']}")
        if song['album'] != '':
            print(f"   ALBUM: {song['album']}")
        if song['genre'] != []:
            D = ', '.join(str(i) for i in song['genre'])
            d = D.title()
            print(f"   GENRE: {d}")
        print(f"  RATING: {rating_map[str(song['rating'])]}")
        if song['released'] != '':
            date_list = song['released'].split("/")
            print(f"RELEASED: {get_written_date(date_list)}")
        print(f"FAVORITE: {song['favorite']}")
        print('*'*42)


    
def print_songs(song_dict, rating_map, title_only = False, show_id = False, fave = False, get_genre = False):
    """
    param: song_dict (dict) - a dictionary containing dictionaries with
            the song data
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the title of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the key (unique ID number) of the song is not displayed.
            Otherwise, displays the id number.
    param: fave (Boolean) - by default, set to False, and prints all songs.
            Otherwise, if it is set to True, prints only the songs marked as favorite.
            This parameter is meant to be used exclusive of get_genre
            (i.e. if fave=True, then get_genre should be False, and vice versa).
    param: get_genre (Boolean) - by default, set to False, and prints all songs.
            If set to True, then the function should ask the user for a
            genre keyword (string) and print only those songs that contain that string in its genre value.
            This parameter is meant to be used exclusive of fave (i.e. if fave=True, then get_genre should be False, and vice versa).
            NOTE: If a song has multiple instances of that genre keyword, you should only print the song once.

    returns: None; only prints the song values from the song_list

    Helper functions:
    - print_song() to print individual songs
    """
    print("*"*42)
    for sid, song in song_dict.items():

        if fave == False and get_genre == False:
            print_song(song, rating_map, title_only, show_id)

        elif fave == True and get_genre ==False:
            if song['favorite'] == True:
                    print_song(song, rating_map, title_only, show_id)

    if get_genre == True:
        genre = input('Enter genre:: ')
        if genre in song['genre']:
                print_song(song, rating_map, title_only, show_id)


def delete_song(song_dict, songid):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: songid (str) - a string that is expected to
            contain the key to a song dictionary (i.e. same as its unique ID)

    The function first checks if the dictionary of songs is empty.
    The function then validates the song ID to verify
    that the provided ID key can access an element from song_dict
    On success, the function saves the item's "title" from song_dict
    and returns that string ("title" value)
    after the item is deleted from song_dict.

    returns:
    If the input list is empty, return 0.
    If the ID is not valid (i.e. not found in the song_dict), return -1.
    Otherwise, on success, the entire song is removed from song_dict
    and the function returns the title of the deleted song.
    """
    if len(song_dict) == 0:
        return 0
    if songid not in song_dict:
        return -1
    else:
        song = song_dict.pop(songid)
        return song['title']

def is_valid_addlist(List):
    """
    The entire input list has to be made up of strings.
    The function calls the helper function is_valid_addlist() to check this.
    This helper function returns a Boolean value.
    If the value is invalid, then get_new_song() has to return a tuple containing
    the message string "Bad list. Found non-string, or bad length" and the integer 0.
    """
    if len(List) != 9:
        return False
    else:
        if type(List[0]) != str:
            return False
        elif type(List[1]) != str:
            return False
        elif type(List[2]) != str:
            return False
        elif type(List[3]) != str:
            return False
        elif type(List[4]) != str:
            return False
        elif type(List[5]) != str:
            return False
        elif type(List[6]) != str:
            return False
        elif type(List[7]) != str:
            return False
        elif type(List[8]) != str:
            return False
        else:
            return True


def is_valid_title(title):
    """
    The "title" value has to be a string that's at least 2 characters long
    and at most 40 characters long.
    The function calls the helper function is_valid_title() to check this.
    This helper function returns a Boolean value.
    If the value is invalid, then get_new_song() has to return a tuple containing
    the message string "Bad Title length" and the integer -1.
    """
    if type(title) == str:
        if 2 <= len(title) <= 40:
            return True
        else:
            return False
    else:
        return False

def is_valid_time(time):
    """
    The "length" value has to be in 00:00 format, that is, it's a string that has 2 digits, followed by a colon, followed by 2 digits.
    The function calls the helper function is_valid_time() to check this.
    This helper function returns a Boolean value.
    If the value is invalid, then get_new_song() has to return a tuple containing
    the message string "Invalid time format for Length" and the integer -2.
    """
    if len(time) != 5:
        return False
    else:
        if time.count(":") != 1:
            return False
        else:
            if time[0] not in "0123456789":
                return False
            elif time[1] not in "0123456789":
                return False
            elif time[3] not in "0123456789":
                return False
            elif time[4] not in "0123456789":
                return False
            else:
                return True


def is_valid_month(date_list):
    if len(date_list) == 3:
        for i in date_list:
            if type(i) is not str:
                return False
        if date_list[0].isdigit():
            month = int(date_list[0]) 
            if month >= 1 and month <= 12:
                return True
    else:
        return False

def is_valid_day(date_list):
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if is_valid_month(date_list) is True:
        if date_list[1].isdigit():
            month = int(date_list[0])
            day = int(date_list[1])
            if day >= 1 and day <= num_days[month]:
                return True
    else:
        return False

def is_valid_year(date_list):
    if is_valid_month(date_list) and is_valid_day(date_list):
        if date_list[2].isdigit():
            year = int(date_list[2])
            if year > 1000: 
                return True
    else:
        return False

def is_valid_date(date_string):
    """
    The "released" value has to be in MM/DD/YYYY format.
    The function calls the helper function is_valid_date() to check this.
    is_valid_date() is very much like an exercise you all did before:
    refer to Lab 7.19 for big clues on how to do this.
    This helper function returns a Boolean value.
    You have implemented a function like this in previous labs.
    If the value is invalid, then get_new_song() has to return a tuple containing
    the message string "Invalid date format for Release Date" and the integer -4.
    """
    date_list = date_string.split("/")
    if len(date_list) == 3 and is_valid_month(date_list) is True and is_valid_day(date_list) is True and is_valid_year(date_list) is True:
        return True
    else:
        return False

def is_valid_uid(a_str, key_list):
    """
    The "uid" value is a string that has to be made up of exactly 5 digits.
    The range of these digits can only be "10000" to "99999".
    Additionally, this value has to be unique to any other uid value in the
    current song dictionary (all_songs). The function calls the
    helper function is_valid_uid(str, key_list) to check this.
    The key_list parameter is a list of all the keys in the song dictionary
    (hint: you can use the .key() method to obtain these).
    This helper function returns a Boolean value.
    If the value is invalid, then get_new_song() has to return a tuple containing
    the message string "Unique ID is invalid or non-unique" and the integer -6.
    """
    
    if len(a_str) != 5:
        return False
    elif a_str[0] not in "0123456789":
        return False
    elif a_str[1] not in "0123456789":
        return False
    elif a_str[2] not in "0123456789":
        return False
    elif a_str[3] not in "0123456789":
        return False
    elif a_str[4] not in "0123456789":
        return False
    elif int(a_str) not in range(10000,99999):
        return False
    else:
        x = list(key_list)
        x.append(a_str)
        for i in x:
            if x.count(a_str) > 1:
                return False
            else:
                return True

def new_fave(fave):
    if fave[0] == "T" or "t":
        return True
    elif fave[0] == 'F' or 'f':
        return False

def get_new_song(List, Dict, Key_list):
    """
    Once validation is taken care of, then the values passed into get_new_song()
    through its list parameter, must be added as values
    to a new dictionary with the 9 song keys (i.e. "title", "artist", "length", etc…)
    Important: make sure when you add these values that they
    are added as the correct data type.
    The new dictionary gets returned at the conclusion of this process.
    """
    if is_valid_addlist(List) == False:
        return ("Bad list. Found non-string, or bad length", 0)

    Fave = str(List[7])
    
    
    if is_valid_time(List[2]) == False:
        return ("Invalid time format for Length", -2)
    elif type(List[5]) != str:
        return ("Invalid Rating value", -3)
    elif List[5] != '1' and List[5] != '2' and List[5] != '3' and List[5] != '4' and List[5] != '5':
        return ("Invalid Rating value", -3)
    elif is_valid_date(List[6]) == False:
        return ("Invalid date format for Release Date", -4)
    elif  Fave[0] != "T" and "t" and "F" and "f":
        return ("Invalid value for Favorite", -5)
    elif is_valid_uid(List[8], Key_list) == False:
        return ("Unique ID is invalid or non-unique", -6)
    elif is_valid_title(List[0]) == False:
        return ("Bad Title length", -1)
    else:
        new_dict = {
            "title": List[0],
            "artist": List[1],
            "length": List[2],
            "album": List[3],
            "genre": list(List[4].split(',')),
            "rating": int(List[5]),
            "released": List[6],
            "favorite": new_fave(Fave),
            "uid": int(List[8])
            }
        return new_dict

def edit_song(song_dict, songid, rating_map, field_key, field_info, allkeys):
    """
    param: song_dict (dict) - dictionary of all songs
    param: songid (str) - a string that is expected to contain the key of
            a song dictionary (same value as its unique id)
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: field_key (string) - a text expected to contain the name
            of a key in the song dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            song_dict[field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary.

    The function first calls some of its helper functions
    to validate the provided field.
    If validation succeeds, the function proceeds with the edit.

    return:
    If song_dict is empty, return 0.
    If the field_key is not a string, return -1.
    If the remainder of the validation passes, return the dictionary song_dict[songid].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions depending on the field_key:
    - is_valid_title()
    - is_valid_time()
    - is_valid_date()
    - is_valid_uid()
    """
    D ={'title': is_valid_title(field_info),
        'time': is_valid_time(field_info),
        'date': is_valid_date(field_info),
        'uid': is_valid_uid(field_info, allkeys)
        }
    if song_dict == {}:
        return 0
    elif type(field_key) != str:
        return -1
    elif D[field_key] == False:
        return field_key
    else:
        song_dict[songid][field_key] = field_info
        return song_dict[songid]
    

def do_stats(song_dict, opt):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: opt (str) - an option from the menu
    to do one of the following statistical calculations:
        "A" - find the mean (average) of all song ratings values
        "B" - find the median of all song ratings values
        "C" - find the standard deviation of all song ratings values
        "D" - print out a histogram of all song ratings values

    Helpful hint: see example on top of page in
    zyBook Ch. 8.4 to see how to do mean and stddev calculations.

    returns: Nothing! This function only PRINTS out results.    
    """
    Key = "rating"
    Value = [sub[Key] for sub in song_dict.values() if Key in sub.keys()]
    rating = list(Value)

    mean = sum(rating)/len(rating)

    rating.sort()
    a = len(rating) // 2
    if len(rating)%2 != 0:
        median = rating[a]
    else:
        median = (rating[a] + rating[a-1]) / 2

    tmp = 0
    for i in rating:
        tmp += (i - mean )**2
    std_dev = (tmp/len(rating))**0.5

    count1 = "*"*(rating.count(1))
    count2 = "*"*(rating.count(2))
    count3 = "*"*(rating.count(3))
    count4 = "*"*(rating.count(4))
    count5 = "*"*(rating.count(5))
               
    if opt == "A":
        print(f'The mean value of all ratings is: {mean:.2f}')
    elif opt == "B":
        print(f'The median value of all ratings is: {median:.2f}')
    elif opt == "C":
        print(f'The standard deviation value of all ratings is: {std_dev:.2f}')
    else:
        print(f'1 {count1}')
        print(f'2 {count2}')
        print(f'3 {count3}')      
        print(f'4 {count4}')
        print(f'5 {count5}')

def save_to_csv(song_dict, filename):
    """
    param: song_dict(dict of dict) - The dictionary of songs stored 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the songs. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every song in the dictionary and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:

    * title
    * artist
    * length
    * album
    * genre (all element in the original list are converted to string
        joined with commas separating)
    * rating (converted to string)
    * released (written as string, i.e, "06/06/2022", NOT "June 6, 2022")
    * favorite (converted to string)
    * uid

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    import os
    if filename[-4:] != '.csv':
        return -1
    else:
        with open(filename, 'w', newline='') as a:
            csv_writer = csv.writer(a)
            row = []
            for key, value in song_dict.items():
                row.append(key)
                for i in value:
                    row.append(i)
                    csv_writer.writerow(row)
        return None

def load_from_csv(filename, in_dict, rating_map, allkeys):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_dict (dict of dict) - A dictionary of songs (dictionary objects) to which
            the songs read from the provided filename are added.
            If in_dict is not empty, the existing songs are not dropped.
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new song using the `get_new_song()` function.
    - If the function `get_new_song()` returns a valid song object,
    it gets added to `in_dict`.
    - If the `get_new_song()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid song data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_dict` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_dict and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_dict`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_song().

    Helper functions:
    - get_new_song()
    """
    import csv
    import os
    if filename[-4:] != '.csv':
        return -1
    elif os.path.isfile(filename) != True:
        return None
    else:
        with open(filename, 'r') as a:
            csv_reader = csv.reader(a, delimiter=',')
            row_num = 1
            file = []
            for row in csv_reader:
                if type(get_new_song(row, rating_map, allkeys)) != dict:
                    file.append(row_num)
                else:
                    in_dict[tuple(allkeys)]=(get_new_song(row, rating_map, allkeys))
                    row_num += 1
            return file
            



