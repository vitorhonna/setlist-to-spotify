def checkIfSongIsInList(songName, list):
    for index, songFromList in enumerate(list):
        if songFromList.name == songName:
            return [True, index]
    return [False, None]


def calculate_songs_score(setlists):
    class Song:
        def __init__(self, name, score):
            self.name = name
            self.score = score

        def updateScore(self, relativeScore):
            self.score = (
                self.score+relativeScore)/2

        def getJson(self):
            return {
                "name": self.name,
                "score": self.score,
            }

        def lookInside(self):
            print(f'{self.name}, {round(self.score, 2)}')

    songsScore = []

    for setlistPosition, setlist in enumerate(setlists):
        for songPositionInSetlist, songName in enumerate(setlist):
            songName = songName.lower()

            [songIsInList, index] = checkIfSongIsInList(
                songName, songsScore)

            if songIsInList:
                song = songsScore[index]
                relativeScore = (songPositionInSetlist+1) / len(setlist)
                song.updateScore(relativeScore)
            else:
                relativeScore = (songPositionInSetlist+1) / len(setlist)
                song = Song(songName, relativeScore)
                songsScore.append(song)

    songsScore_dicts = []

    for song in songsScore:
        songsScore_dicts.append(song.getJson())

    # EXPECTED OUTPUT
    # songs_info = [
    #     {
    #         'name': 'clarão',
    #         'relativePopularity': 0.01
    #     },
    #     {
    #         'name': 'meninos e meninas',
    #         'relativePopularity': 0.50
    #     },
    #     {
    #         'name': 'idiota',
    #         'relativePopularity': 0.99
    #     },
    # ]

    return songsScore_dicts


def build_final_setlist(songsScore_dicts):
    songsScore_dicts.sort(key=lambda x: x['score'])

    finalSetlist = []

    for songsScore_dict in songsScore_dicts:
        finalSetlist.append(songsScore_dict['name'])

    return finalSetlist
