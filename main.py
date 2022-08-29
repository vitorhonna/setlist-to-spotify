import setlistfm
import utils

def main():
    setlists = setlistfm.get_setlists(
        3, 
        '6797c795-08b4-4da2-a4d8-95a554c2a91c', 
        artistName='jao', 
        cityName='')

    songs_popularity = utils.calculate_popularity(setlists)

    # for setlist in setlists:
    #     print(setlist)
    #     utils.calculate_popularity(setlist)

if __name__ == '__main__':
    main()