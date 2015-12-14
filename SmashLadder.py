#Challonge needs to be installed using, pip install, directions listed on website. 
import challonge

def main():
    #set credentials and the tournament information.
    challonge.set_credentials("eliasingea", "LTQX768N8omoYw2aaRYTn6EyP6yVztkaRjd7TBkQ")
    #show the specific tournament that we would like to get information from
    tournament = challonge.tournaments.show("qt98yh8i")
    tournamentId = tournament["id"]
    #get the information for all the games for the tournament.
    games = challonge.matches.index(tournamentId)
    #get information for all the participants.
    participants = challonge.participants.index(tournament["id"])

    print tournament["id"]
    print tournament["state"]
    file = open("streamedGames.txt", "w")
    #There are the identifiers for the games that will be streamed.
    streamedGames = ['B', 'O', 'G', 'T', 'K', 'W', 'M']
    #This is the call to the function that will give us the names
    #for the next open game to be streamed.
    playerNameOne, playerNameTwo = getPlayers(games, streamedGames, tournamentId)
    #writes the names to a textfile named streamedGames.txt
    file.write(playerNameOne)
    file.write("\n")
    file.write(playerNameTwo)

#Function to get games that match.
def getPlayers(games, streamedGames, tournamentId):
    #we do a nested for loop through all the streamedGames list and the games from the api.
    for s in streamedGames:
        for g in games:
            #if a game matches one of the streamed games.
            if(g["identifier"] == s):
                #if the game that matches is open.
                #There will only be one open per game matched from streamedGames.
                if(g["state"] == "open"):
                    player1 = g["player1-id"]
                    player2 = g["player2-id"]
                    #Games does not give the option to get player names
                    #therefor we make a call to the api to get the names from participants.
                    playerNameOne = challonge.participants.show(tournamentId, player1)["name"]
                    playerNameTwo = challonge.participants.show(tournamentId, player2)["name"]
                    print playerNameOne, playerNameTwo
                    return playerNameOne, playerNameTwo

#Basic python command to run the main function.
if  __name__ =='__main__':
    main()
