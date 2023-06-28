import random

# song_list = []
# for i in range(5):
#     song = input("Enter a song title: ")
#     song_list.append(song)

# print(song_list)

# NUM_SONGS = 3

# song_requests = []

# for song_num in range(NUM_SONGS):
#   song_request = input('Enter a song title: ')
#   song_requests.append(song_request)

# print(song_requests)

#ask user enter the song
#append it to the list
#ask if user wants to continue
#when user doesn't want to continue, return a song from the list


print("Welcome to DJ Pythonic's Song Request Manager!")
print("Enter the song title to make a song request.")
print("To exit, enter Quit.")

song_requests = []
song_request = None

while True:
    song_request = input("Enter a song title: ")
    if song_request == "Quit":
        break
    else:
        if song_request in song_requests:
            song_index = song_requests.index(song_request) + 1
            print(f'''The song {song_request} has already been requested. \n It is song number {song_index} on the list.''')
        else:
            song_requests.append(song_request)
            song_index = song_requests.index(song_request) + 1
            print(f'''The song {song_request} has been added to the list. \n It is song number {song_index} on the list.''')

print("Thank you for your requests. Enjoy the show!")
# print out the entire list of song requests, but don’t print the [ and ] !
