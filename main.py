import setlistfm
import utils
from tabulate import tabulate


def main():

    artist_name = input("Enter artist name: ")

    artists = setlistfm.get_artist_info(artistName=artist_name)
    artist_id = int(input('\nEnter artist id: '))
    artist_mbid = artists[artist_id-1]['mbid']

    setlists = setlistfm.get_setlists(
        numberOfSetlists=10,
        artistMbid=artist_mbid,
        artistName='',
        cityName='')

    if not setlists:
        print('\nNo setlists found :(')
        return

    songsScore = utils.calculate_songs_score(setlists)

    finalSetlist = utils.build_final_setlist(songsScore)
    print(finalSetlist)
    print(len(finalSetlist))


if __name__ == '__main__':
    main()


# avril = ['Girlfriend',
#          'Bite Me',
#          'What the Hell',
#          'Complicated',
#          'My Happy Ending',
#          'Love It When You Hate Me',
#          'Sk8er Boi',
#          "I'm With You"]
