def calculate_popularity(setlists):
    # print(setlists)
    class Song:
        def __init__(self, name, relativePopularity):
            self.name = name
            self.relativePopularity = relativePopularity
            self.count = 1

        def updateCount(self):
            self.count = self.count + 1

        def updateRelativePopularity(self, newRelativePopularity):
            self.relativePopularity = (
                self.relativePopularity+newRelativePopularity)/2

        def calculatePopularity(self):
            popularity = self.relativePopularity / self.count
            return popularity

    songs = []

    setlist = setlists[1]

    for i in range(len(setlist)):
        song = setlist[i].lower()
        print(i+1, song)

        song_popularity = {
            'name': song,
            'count':
            ''
        }

    return
