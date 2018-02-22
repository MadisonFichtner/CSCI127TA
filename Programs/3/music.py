from csv import reader

def longest_song():
    lib = open("music.csv",'r')
    libreader = reader(lib, skipinitialspace=True)
    next(libreader) # skip the column names

    longest = [0, 'temp'] # to save details of longest song
    for song in libreader:
        if float(song[9]) > longest[0]:
            longest[0] = float(song[9])
            longest[1] = song[33]

    print("Title:", longest[1])
    print("Length to nearest second:", round(longest[0]))
    lib.close()

def songs_by_year(year):
    lib = open("music.csv",'r')
    libreader = reader(lib, skipinitialspace=True)
    next(libreader) # skip the column names

    count = 0
    for song in libreader:
        if year == int(song[-1]):
            count += 1

    print("The number of songs from", year,"is", count)
    lib.close()

def all_songs_by_artist(artist):
    lib = open("music.csv",'r')
    libreader = reader(lib, skipinitialspace=True)
    next(libreader) # skip the column names

    songs = []
    for song in libreader:
        if artist.lower() == song[2].lower():
            songs.append(song[33])

    print("\nSongs In Alphabetical Order")
    print("---------------------------")
    if len(songs) == 0:
        print("There are no songs by this artist.")
    else:
        songs.sort()
        for title in songs:
            print(title)
    print("---------------------------")

    lib.close()

def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. You choose something that is interesting and non-trivial.")
    print("5. Quit.")

def main():
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            longest_song()
        elif (choice == 2):
            year = int(input("Enter desired year: "))
            songs_by_year(year)
        elif (choice == 3):
            artist = input("Enter name of artist: ").lower()
            all_songs_by_artist(artist)
        elif (choice == 4):
            pass
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")

main()
