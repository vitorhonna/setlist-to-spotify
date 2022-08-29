def checkIfSongIsInList(songName, list):
    for index, songFromList in enumerate(list):
        if songFromList.name == songName:
            return [True, index]
    return [False, None]


def calculate_popularity(setlists):
    # print(setlists)

    class Song:
        def __init__(self, name, relativePopularity):
            self.name = name
            self.count = 1
            self.relativePopularity = relativePopularity

        def updateCount(self):
            self.count = self.count + 1

        def updateRelativePopularity(self, newRelativePopularity):
            self.relativePopularity = (
                self.relativePopularity+newRelativePopularity)/2

        def calculatePopularity(self):
            popularity = self.relativePopularity / self.count
            print(round(popularity, 2))
            return popularity

        def lookInside(self):
            print(f'{self.name}, {self.count}, {round(self.relativePopularity, 2)}')

    songsPopularity = []

    for setlistPosition, setlist in enumerate(setlists):
        print(setlist)
        print('='*50)
        for songPositionInSetlist, songName in enumerate(setlist):
            songName = songName.lower()

            [songIsInList, index] = checkIfSongIsInList(
                songName, songsPopularity)

            if songIsInList:
                # print(f'{songName} SIM, posicao {index}')
                song = songsPopularity[index]
                relativePopularity = (songPositionInSetlist+1) / len(setlist)
                song.updateRelativePopularity(relativePopularity)
                song.updateCount()
            else:
                # print(f'{songName} NAO')
                relativePopularity = (songPositionInSetlist+1) / len(setlist)
                song = Song(songName, relativePopularity)
                songsPopularity.append(song)

    for song in songsPopularity: 
        song.lookInside()
        # song.calculatePopularity()

            # print(songPositionInSetlist+1, song.name)

    # EXPECTED OUTPUT STRUCTURE
    # songs_info = [
    #     {
    #         'name': 'clarão',
    #         'relativePopularity': 0.01,
    #         'count': 3,
    #     },
    #     {
    #         'name': 'meninos e meninas',
    #         'relativePopularity': 0.50,
    #         'count': 3,
    #     },
    #     {
    #         'name': 'idiota',
    #         'relativePopularity': 0.99,
    #         'count': 3,
    #     },
    # ]

    return songsPopularity
