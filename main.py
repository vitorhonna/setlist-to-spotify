import setlistfm
import utils
from tabulate import tabulate
import string
import spotify

print()

# Generate spotify token here (SPOTIFY_TOKEN)
# https://developer.spotify.com/console/post-playlists/


def main():
    search_name = input("Enter artist name: ")

    artists = setlistfm.get_artist_info(artistName=search_name)

    artist_id = input('\nEnter artist id [default=1]: ')
    artist_id = int(artist_id) if artist_id else 1

    artist_name = artists[artist_id-1]['name']
    artist_mbid = artists[artist_id-1]['mbid']

    number_of_setlists = input(
        '\nEnter the number of setlists to process (max 20) [default=5]: ')
    number_of_setlists = int(number_of_setlists) if number_of_setlists else 5

    min_setlist_size = input(
        '\nEnter a minimum setlist size (# songs) [default=7]: ')
    min_setlist_size = int(min_setlist_size) if min_setlist_size else 7

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

    print(f'\nThe playlist will contain the following songs (if available on Spotify):')
    table = tabulate([[i+1, string.capwords(song)] for i, song in enumerate(finalSetlist)],
                     tablefmt='presto'
                     )
    print(table)

    playlistApproved = True if input(
        '\nCreate playlist [Y/n]? ') == 'Y' else False

    if playlistApproved:
        print('\nLooking for songs on Spotify...')
        song_uris = spotify.get_song_uris(finalSetlist, artist_name)
        print(f'\n{len(song_uris)} of {len(finalSetlist)} songs were found')
        # print(song_uris)

        user_id = spotify.get_user_id()
        # print(user_id)

        playlist_name = input('\nEnter playlist name: ')
        print('\nCreating playlist...')
        [playlist_id, playlist_link] = spotify.create_playlist(
            playlist_name, user_id)

        print(f'\nAdding songs to playlist "{playlist_name}"...')
        spotify.add_songs_to_playlist(song_uris, playlist_id)

        print(
            f'\nYour playlist "{playlist_name}" is ready! :)\nYou can access it here: {playlist_link}')

    else:
        print('\n[X] Playlist creation was cancelled [X]')


if __name__ == '__main__':
    main()
