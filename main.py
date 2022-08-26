import setlistfm
import utils

setlists = setlistfm.get_setlists(
    5, '6797c795-08b4-4da2-a4d8-95a554c2a91c', artistName='jao', cityName='')

utils.calculate_popularity(setlists)

# for setlist in setlists:
#     print(setlist)
#     utils.calculate_popularity(setlist)
