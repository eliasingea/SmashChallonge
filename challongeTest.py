import challonge
import time

challonge.set_credentials("eliasingea", "LTQX768N8omoYw2aaRYTn6EyP6yVztkaRjd7TBkQ")

tournament = challonge.tournaments.show("eliasTest")

print(tournament["id"])

participants = challonge.participants.index(tournament["id"])
for p in participants:
	name = p["name"]
	active = p["seed"]
	print(name)
	print(active)
games = challonge.matches.index(tournament["id"])
for g in games:
	if(g["state"] == "open"):
		print(g["identifier"],g["state"])
	if(g["state"] == "pending"):
		print(g["identifier"], g["state"])
		if(g["identifier"] == "H"):
			theB = g["id"]
state = challonge.matches.show(tournament["id"], theB)["state"]
while(state is not "open"):
	if state == "pending":
		time.sleep(10)
