import setlistfm
import utils
from tabulate import tabulate
import string

print()


def main():
    artist_name = input("Enter artist name: ")

    artists = setlistfm.get_artist_info(artistName=artist_name)
    artist_id = int(input('\nEnter artist id: '))
    artist_mbid = artists[artist_id-1]['mbid']
    number_of_setlists = int(
        input('\nEnter the number of setlists to process (max 20): '))
    min_setlist_size = int(input('\nEnter minimum setlist size (# songs): '))

    setlists = setlistfm.get_setlists(
        numberOfSetlists=number_of_setlists,
        minSetlistSize=min_setlist_size,
        artistMbid=artist_mbid,
    )

    if not setlists:
        print('\nNo setlists found :(')
        return

    songsScore = utils.calculate_songs_score(setlists)

    finalSetlist = utils.build_final_setlist(songsScore)

    print(f'\nThe playlist will contain the following songs:')
    table = tabulate([[i+1, string.capwords(song)] for i, song in enumerate(finalSetlist)],
                     tablefmt='presto'
                     )
    print(table)

    playlistAprroved = True if input(
        '\nCreate playlist [Y/n]? ') == 'Y' else False

    if playlistAprroved:
        print('\nCreating playlist...')
    else:
        print('\n[X] Playlist creation was cancelled [X]')


if __name__ == '__main__':
    main()