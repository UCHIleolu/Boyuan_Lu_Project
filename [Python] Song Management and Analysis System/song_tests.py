from song_functions import *

addlist1 = ["Cardigan - Extended Version", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", "3", "07/27/2020", "True", "12333"]
addlist2 = ["Cardigan - Extended Version", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", 3, "07/27/2020", True, "12334"]
addlist3 = ["Cardigan - Extended Version", "Taylor Swift", "b7:59", "Folklore"]
addlist4 = ["x", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", "3", "07/27", "True", "1233"]
addlist5 = ["x", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", "3", "07/27/2020", "True", "1233"]
key_list =["11111","12222","12333","12344"]
Dict ={
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
rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}
allkeys = ["12332","14567","78210","99105"]

dict1={}
uid1 = 11118

assert is_valid_addlist(addlist1) == True
assert is_valid_addlist(addlist2) == False
assert is_valid_addlist(addlist3) == False

assert is_valid_title(addlist1[0]) == True
assert is_valid_title(addlist4[0]) == False

assert is_valid_time(addlist1[2]) == True
assert is_valid_time(addlist3[2]) == False

assert is_valid_date(addlist1[6]) == True
assert is_valid_date(addlist4[6]) == False

assert is_valid_uid(addlist2[8],key_list) == True
assert is_valid_uid(addlist1[8],key_list) == False
assert is_valid_uid(addlist4[8],key_list) == False

assert get_written_date(["01", "01", "1970"]) == "January 1, 1970"
assert get_written_date(["02", "03", "2000"]) == "February 3, 2000"
assert get_written_date(["10", "15", "2022"]) == "October 15, 2022"
assert get_written_date(["12", "31", "2021"]) == "December 31, 2021"

assert get_new_song(addlist2,Dict,key_list) == ('Bad list. Found non-string, or bad length', 0)
assert get_new_song(addlist4,Dict,key_list) == ('Invalid date format for Release Date', -4)
assert get_new_song(addlist5,Dict,key_list) == ('Unique ID is invalid or non-unique', -6)

assert edit_song(dict1, "12332", rating_map, 'uid', '12999', allkeys) == 0
assert edit_song(Dict, "12332", rating_map, uid1, '12999', allkeys) == -1

assert delete_song(dict1, "12332") == 0
assert delete_song(Dict, '22274') == -1

assert load_from_csv('ilovecs', Dict, rating_map, allkeys) == -1
assert load_from_csv('ilovecs.csv', Dict, rating_map, allkeys) == None

assert save_to_csv(Dict, 'ilovecs') == -1
assert save_to_csv(Dict, '111111') == -1




