
# Music Recommendation Program created by @roxyfarhad @12/06/18
# The app will give you a choice of three differnet artists
# of which you can choose one of them and a list of similar artists appears.
# Among the similar artists, you can again choose one and their songs and albums will print out.

import spotipy
import spotipy.util as util
import os

# get the username and create the token

username = input("what is your spotify username: ")

# user ID: blm123xjstrpo2l3jcpbs78qi
try:
    token = util.prompt_for_user_token(username)

except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)


# creating spotify object
spotifyObject = spotipy.Spotify(auth=token)

# Introduction to the app

user = spotifyObject.current_user()
displayName = user['display_name']

print("Welcome to Spotify " + displayName + "!")
print("")
print("This program will allow you to choose an artist and find similar aritsts.")

# the list of bands that you can see

print("You can choose to find a list of artists similar to one of the "
      "these three: Frank Ocean, America, Amy Winehouse")
print("")

choice = input("Press 1 for Frank Ocean, 2 for America, 3 for Amy Winehouse")

# Getting the information of Frank Ocean if 1 is pressed.

if choice == "1":

    # Getting the ID

        artistFrank = "Frank Ocean"
        frank = spotifyObject.search(artistFrank, 1, 0, "artist")
        artist = frank['artists']['items'][0]
        frankID = artist['id']

    # Showing the Genres

        print("Here are the list of genres of Frank Ocean:")

        frankGenre = artist['genres'][0]
        print(frankGenre)

    # Showing the top tracks

        print("")
        print("Here are a list of Frank Ocean's top tracks")

        frankTopTracks = spotifyObject.artist_top_tracks(frankID)

        for tracks in frankTopTracks['tracks'][:5]:
            print("TRACK: " + tracks['name'])

        print("Related artists to Frank Ocean: ")
        relatedFrank = spotifyObject.artist_related_artists(frankID)
        # takes 5 related artists
        relatedOne = relatedFrank['artists'][0]['name']
        relatedTwo = relatedFrank['artists'][1]['name']
        relatedThree = relatedFrank['artists'][2]['name']
        relatedFour = relatedFrank['artists'][3]['name']
        relatedFive = relatedFrank['artists'][4]['name']

        print(relatedOne + ", " + relatedTwo + ", " + relatedThree + ", " + relatedFour + ", " + relatedFive)

        print("")

# Finding the information of related artists based on user choice

        print("Pick one artist from the list to find those artists' tracks and albums.")
        relatedChoice = input(
            "Press 1 - " + relatedOne + ", 2 - " + relatedTwo + ", 3 - " + relatedThree + ", 4 - " + relatedFour + ". 5 - " + relatedFive)

        if relatedChoice == "1":
            choiceOne = spotifyObject.search(str(relatedOne), 1, 0, "artist")
            artistChoiceOne = choiceOne["artists"]["items"][0]
            choiceOneID = artistChoiceOne["id"]

        # Choosing whether you only want to see their top tracks or albums + tracks

            tracksOrAlbums = input(
                "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
            print("")

            if tracksOrAlbums == "1":
                artistTopTracks = spotifyObject.artist_top_tracks(choiceOneID)
                for tracks in artistTopTracks['tracks'][:5]:
                    print("TRACK: " + tracks['name'])

            if tracksOrAlbums == "2":
                choiceOneAlbums = spotifyObject.artist_albums(choiceOneID)
                choiceOneAlbums = choiceOneAlbums["items"]

                for albums in choiceOneAlbums:
                    print("ALMBUM: " + albums['name'])
                    albumID = albums['id']

                    choiceOneTracks = spotifyObject.album_tracks(albumID)
                    choiceOneTracks = choiceOneTracks['items']

                    r = 1

                    for tracks in choiceOneTracks:
                        print(str(r) + ": " + tracks['name'])
                        r += 1

        if relatedChoice == "2":
            choiceTwo = spotifyObject.search(str(relatedTwo), 1, 0, "artist")
            artistChoiceTwo = choiceTwo['artists']['items'][0]
            choiceTwoID = artistChoiceTwo['id']

            tracksOrAlbums = input(
                "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")

            print("")

            if tracksOrAlbums == "1":
                artistTopTracks = spotifyObject.artist_top_tracks(choiceTwoID)
                for tracks in artistTopTracks['tracks'][:5]:
                    print("TRACK: " + tracks['name'])

            if tracksOrAlbums == "2":

                choiceTwoAlbums = spotifyObject.artist_albums(choiceTwoID)
                choiceTwoAlbums = choiceTwoAlbums['items']

                for albums in choiceTwoAlbums:
                    print("ALBUM: " + albums['name'])
                    albumID = albums['id']

                    choiceTwoTracks = spotifyObject.album_tracks(albumID)
                    choiceTwoTracks = choiceTwoTracks['items']

                    r = 1

                    for tracks in choiceTwoTracks:
                        print(str(r) + ": " + tracks['name'])
                        r += 1

        if relatedChoice == "3":
            choiceThree = spotifyObject.search(str(relatedThree), 1, 0, "artist")
            artistChoiceThree = choiceThree['artists']['items'][0]
            choiceThreeID = artistChoiceThree['id']

            tracksOrAlbums = input(
                "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
            print("")

            if tracksOrAlbums == "1":
                artistTopTracks = spotifyObject.artist_top_tracks(choiceThreeID)
                for tracks in artistTopTracks['tracks'][:5]:
                    print("TRACK: " + tracks['name'])

            if tracksOrAlbums == "2":

                choiceThreeAlbums = spotifyObject.artist_albums(choiceThreeID)
                choiceThreeAlbums = choiceThreeAlbums['items']

                for albums in choiceThreeAlbums:
                    print("Album: " + albums['name'])
                    albumID = albums['id']

                    choiceThreeTracks = spotifyObject.album_tracks(albumID)
                    choiceThreeTracks = choiceThreeTracks['items']

                    r = 1

                    for tracks in choiceThreeTracks:
                        print(str(r) + ", " + tracks['name'])
                        r += 1

        if relatedChoice == "4":
            choiceFour = spotifyObject.search(str(relatedFour), 1, 0, "artist")
            artistChoiceFour = choiceFour['artists']['items'][0]
            choiceFourID = artistChoiceFour['id']

            tracksOrAlbums = input(
                "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
            print("")

            if tracksOrAlbums == "1":
                artistTopTracks = spotifyObject.artist_top_tracks(choiceThreeID)
                for tracks in artistTopTracks['tracks'][:5]:
                    print("TRACK: " + tracks['name'])

            if tracksOrAlbums == "2":

                choiceFourAlbums = spotifyObject.artist_albums(choiceFourID)
                choiceFourAlbums = choiceFourAlbums['items']

                for albums in choiceFourAlbums:
                    print("ALBUM: " + albums['name'])
                    albumID = albums['id']

                    choiceFourTracks = spotifyObject.album_tracks(albumID)
                    choiceFourTracks = choiceFourTracks['items']

                    r = 1

                    for tracks in choiceFourTracks:
                        print(str(r) + ": " + tracks['name'])
                        r += 1

        if relatedChoice == "5":
            choiceFive = spotifyObject.search(str(relatedFive), 1, 0, "artist")
            artistChoiceFive = choiceFive['artists']['items'][0]
            choiceFiveID = artistChoiceFive['id']

            tracksOrAlbums = input(
                "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
            print("")

            if tracksOrAlbums == "1":
                artistTopTracks = spotifyObject.artist_top_tracks(choiceFiveID)
                for tracks in artistTopTracks['tracks'][:5]:
                    print("TRACK: " + tracks['name'])

            if tracksOrAlbums == "2":

                choiceFiveAlbums = artistChoiceFive['id']
                choiceFiveAlbums = choiceFiveAlbums['items']

                for albums in choiceFiveAlbums:
                    print("ALBUM: " + albums['name'])
                    albumID = albums['id']

                    choiceFiveTracks = spotifyObject.album_tracks(albumID)
                    choiceFiveTracks = choiceFiveTracks['items']

                    r = 1

                    for tracks in choiceFiveTracks:
                        print(str(r) + ": " + tracks['name'])
                        r += 1

if choice == "2":
    artistAmerica = "America"
    america = spotifyObject.search(artistAmerica, 1, 0, "artist")
    artist = america['artists']['items'][0]

    americaID = artist['id']

    print("Here are the list of genres of America:")

    AmericaGenre = artist['genres'][0]
    print(AmericaGenre)
    print("")

    print("Here are a list of America's top tracks")

    AmericaTopTracks = spotifyObject.artist_top_tracks(americaID)

    for tracks in AmericaTopTracks['tracks'][:5]:
        print("TRACK: " + tracks['name'])

    print("")
    print("Related artists to America: ")
    relatedAmerica = spotifyObject.artist_related_artists(americaID)
    # takes 5 related artists
    relatedOne = relatedAmerica['artists'][0]['name']
    relatedTwo = relatedAmerica['artists'][1]['name']
    relatedThree = relatedAmerica['artists'][2]['name']
    relatedFour = relatedAmerica['artists'][3]['name']
    relatedFive = relatedAmerica['artists'][4]['name']

    print(relatedOne + ", " + relatedTwo + ", " + relatedThree + ", " + relatedFour + ", " + relatedFive)
    print("")

    print("Pick one artist from the list to find those artists' tracks and albums.")
    relatedChoice = input(
        "Press 1 - " + relatedOne + ", 2 - " + relatedTwo + ", 3 - " + relatedThree + ", 4 - " + relatedFour + ". 5 - " + relatedFive)
    print("")

    if relatedChoice == "1":
        choiceOne = spotifyObject.search(str(relatedOne), 1, 0, "artist")
        artistChoiceOne = choiceOne["artists"]["items"][0]
        choiceOneID = artistChoiceOne["id"]

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceOneID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceOneAlbums = spotifyObject.artist_albums(choiceOneID)
            choiceOneAlbums = choiceOneAlbums["items"]

            for albums in choiceOneAlbums:
                print("ALMBUM: " + albums['name'])
                albumID = albums['id']

                choiceOneTracks = spotifyObject.album_tracks(albumID)
                choiceOneTracks = choiceOneTracks['items']

                r = 1

                for tracks in choiceOneTracks:
                    print(str(r) + ": " + tracks['name'])
                    r += 1

    if relatedChoice == "2":
        choiceTwo = spotifyObject.search(str(relatedTwo), 1, 0, "artist")
        artistChoiceTwo = choiceTwo['artists']['items'][0]
        choiceTwoID = artistChoiceTwo['id']

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceTwoID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceTwoAlbums = spotifyObject.artist_albums(choiceTwoID)
            choiceTwoAlbums = choiceTwoAlbums['items']

            for albums in choiceTwoAlbums:
                print("ALBUM: " + albums['name'])
                albumID = albums['id']

                choiceTwoTracks = spotifyObject.album_tracks(albumID)
                choiceTwoTracks = choiceTwoTracks['items']

                r = 1

                for tracks in choiceTwoTracks:
                    print(str(r) + ": " + tracks['name'])
                    r += 1

    if relatedChoice == "3":
        choiceThree = spotifyObject.search(str(relatedThree), 1, 0, "artist")
        artistChoiceThree = choiceThree['artists']['items'][0]
        choiceThreeID = artistChoiceThree['id']

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceThreeID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceThreeAlbums = spotifyObject.artist_albums(choiceThreeID)
            choiceThreeAlbums = choiceThreeAlbums['items']

            for albums in choiceThreeAlbums:
                print("Album: " + albums['name'])
                albumID = albums['id']

                choiceThreeTracks = spotifyObject.album_tracks(albumID)
                choiceThreeTracks = choiceThreeTracks['items']

                r = 1

                for tracks in choiceThreeTracks:
                    print(str(r) + ", " + tracks['name'])
                    r += 1

    if relatedChoice == "4":
        choiceFour = spotifyObject.search(str(relatedFour), 1, 0, "artist")
        artistChoiceFour = choiceFour['artists']['items'][0]
        choiceFourID = artistChoiceFour['id']

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceFourID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceFourAlbums = spotifyObject.artist_albums(choiceFourID)
            choiceFourAlbums = choiceFourAlbums['items']

            for albums in choiceFourAlbums:
                print("ALBUM: " + albums['name'])
                albumID = albums['id']

                choiceFourTracks = spotifyObject.album_tracks(albumID)
                choiceFourTracks = choiceFourTracks['items']

                r = 1

                for tracks in choiceFourTracks:
                    print(str(r) + ": " + tracks['name'])
                    r += 1

    if relatedChoice == "5":
        choiceFive = spotifyObject.search(str(relatedFive), 1, 0, "artist")
        artistChoiceFive = choiceFive['artists']['items'][0]
        choiceFiveID = artistChoiceFive['id']

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceFiveID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceFiveAlbums = spotifyObject.artist_albums(choiceFiveID)
            choiceFiveAlbums = choiceFiveAlbums['items']

            for albums in choiceFiveAlbums:
                print("ALBUM: " + albums['name'])
                albumID = albums['id']

                choiceFiveTracks = spotifyObject.album_tracks(albumID)
                choiceFiveTracks = choiceFiveTracks['items']

                r = 1

                for tracks in choiceFiveTracks:
                    print(str(r) + ": " + tracks['name'])
                    r += 1

if choice == "3":
    artistAmy = "Amy Winehouse"
    amy = spotifyObject.search(artistAmy, 1, 0, "artist")
    artist = amy['artists']['items'][0]
    amyID = artist['id']

    print("")
    print("Here are the list of genres of Amy Winehouse:")

    amyGenre = artist['genres'][0]
    print(amyGenre)
    print("")

    print("Here are a list of Amy Winehouse's top tracks")

    amyTopTracks = spotifyObject.artist_top_tracks(amyID)

    for tracks in amyTopTracks['tracks'][:5]:
        print("TRACK: " + tracks['name'])

    print("")

    print("Related artists to Amy Winehouse: ")
    relatedAmy = spotifyObject.artist_related_artists(amyID)
    # takes 5 related artists
    relatedOne = relatedAmy['artists'][0]['name']
    relatedTwo = relatedAmy['artists'][1]['name']
    relatedThree = relatedAmy['artists'][2]['name']
    relatedFour = relatedAmy['artists'][3]['name']
    relatedFive = relatedAmy['artists'][4]['name']

    print(relatedOne + ", " + relatedTwo + ", " + relatedThree + ", " + relatedFour + ", " + relatedFive)

    print("")
    print("Pick one artist from the list to find those artists' tracks and albums.")
    relatedChoice = input(
        "Press 1 - " + relatedOne + ", 2 - " + relatedTwo + ", 3 - " + relatedThree + ", 4 - " + relatedFour + ". 5 - " + relatedFive)
    print("")

    if relatedChoice == "1":
        choiceOne = spotifyObject.search(str(relatedOne), 1, 0, "artist")
        artistChoiceOne = choiceOne["artists"]["items"][0]
        choiceOneID = artistChoiceOne["id"]

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceOneID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceOneAlbums = spotifyObject.artist_albums(choiceOneID)
            choiceOneAlbums = choiceOneAlbums["items"]

            for albums in choiceOneAlbums:
                print("ALMBUM: " + albums['name'])
                albumID = albums['id']

                choiceOneTracks = spotifyObject.album_tracks(albumID)
                choiceOneTracks = choiceOneTracks['items']

                r = 1

                for tracks in choiceOneTracks:
                    print(str(r) + ": " + tracks['name'])
                    r += 1

    if relatedChoice == "2":
        choiceTwo = spotifyObject.search(str(relatedTwo), 1, 0, "artist")
        artistChoiceTwo = choiceTwo['artists']['items'][0]
        choiceTwoID = artistChoiceTwo['id']

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceTwoID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceTwoAlbums = spotifyObject.artist_albums(choiceTwoID)
            choiceTwoAlbums = choiceTwoAlbums['items']

            for albums in choiceTwoAlbums:
                print("ALBUM: " + albums['name'])
                albumID = albums['id']

                choiceTwoTracks = spotifyObject.album_tracks(albumID)
                choiceTwoTracks = choiceTwoTracks['items']

                r = 1

                for tracks in choiceTwoTracks:
                    print(str(r) + ": " + tracks['name'])
                    r += 1

    if relatedChoice == "3":
        choiceThree = spotifyObject.search(str(relatedThree), 1, 0, "artist")
        artistChoiceThree = choiceThree['artists']['items'][0]
        choiceThreeID = artistChoiceThree['id']

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceThreeID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceThreeAlbums = spotifyObject.artist_albums(choiceThreeID)
            choiceThreeAlbums = choiceThreeAlbums['items']

            for albums in choiceThreeAlbums:
                print("Album: " + albums['name'])
                albumID = albums['id']

                choiceThreeTracks = spotifyObject.album_tracks(albumID)
                choiceThreeTracks = choiceThreeTracks['items']

                r = 1

                for tracks in choiceThreeTracks:
                    print(str(r) + ", " + tracks['name'])
                    r += 1

    if relatedChoice == "4":
        choiceFour = spotifyObject.search(str(relatedFour), 1, 0, "artist")
        artistChoiceFour = choiceFour['artists']['items'][0]
        choiceFourID = artistChoiceFour['id']

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceFourID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceFourAlbums = spotifyObject.artist_albums(choiceFourID)
            choiceFourAlbums = choiceFourAlbums['items']

            for albums in choiceFourAlbums:
                print("ALBUM: " + albums['name'])
                albumID = albums['id']

                choiceFourTracks = spotifyObject.album_tracks(albumID)
                choiceFourTracks = choiceFourTracks['items']

                r = 1

                for tracks in choiceFourTracks:
                    print(str(r) + ": " + tracks['name'])
                    r += 1

    if relatedChoice == "5": # there is a problem with this one must fix
        choiceFive = spotifyObject.search(str(relatedFive), 1, 0, 'artist')
        artistChoiceFive = choiceFive['artists']['items'][0]
        choiceFiveID = artistChoiceFive['id']

        tracksOrAlbums = input(
            "Press 1 to see the artists top 5 tracks, or press 2 to see the artists' top albums with their tracks")
        print("")

        if tracksOrAlbums == "1":
            artistTopTracks = spotifyObject.artist_top_tracks(choiceFiveID)
            for tracks in artistTopTracks['tracks'][:5]:
                print("TRACK: " + tracks['name'])

        if tracksOrAlbums == "2":

            choiceFiveAlbums = spotifyObject.artist_albums(choiceFiveID)
            choiceFiveAlbums = choiceFiveAlbums['items']

            for albums in choiceFiveAlbums:
                print("ALBUM: " + albums['name'])
                albumID = albums['id']

                choiceFiveTracks = spotifyObject.album_tracks(albumID)
                choiceFiveTracks = choiceFiveTracks['items']

                r = 1

                for tracks in choiceFiveTracks:
                    print(str(r) + ": " + tracks['name'])
                    r += 1

print("")
print("I hope you found some great new tracks to add to your playlist!")







