import json, os
import requests
import time
from os.path import join, getsize
#This File parses through all the NA.json matches in patches 5.11 & 5.14 Normal & Ranked
#to find the item builds with the highest win rate percentages and aquire other relivent
#info about the champions who used those builds. This information is aquired then saved
#for use via the 'build' webpage on the website after a user has chosen a champ and lane.


#Get champs and list items from 1 match
#get relivent info from the match data about champs and their builds
def getChampsAndItemsGivenMatch(matchInfoPath, matchInfoFile):
	champInfoPath = "../../champions/"
	champInfoFile = "champs.json"
	givenInfo = {}
	#lists of all the info we are interested in aquireing
	participantIds = []
	championIds = []
	championNames = []
	winner = []
	lane = []
	role = []
	magicDamageDealtToChampions = []
	magicDamageTaken = []
	physicalDamageDealtToChampions = []
	physicalDamageTaken = []
	totalDamageDealtToChampions = []
	totalDamageTaken = []
	totalHeal = []
	trueDamageDealtToChampions = []
	trueDamageTaken = []
	#champsItems is a 7x10 2d array, col = participants, row = items
	champsItems = [[0 for x in range(7)] for x in range(10)]
	
	#parse through every match in the NA region
	with open(os.path.join(matchInfoPath, matchInfoFile)) as match:
		matchData = json.load(match)
		for index, participants in enumerate(matchData["participants"]):
			participantIds.append(participants["participantId"])
			championIds.append(participants["championId"])
			lane.append(participants["timeline"]["lane"])
			role.append(participants["timeline"]["role"])
			for key, value in participants["stats"].iteritems():
				if key == "item0": champsItems[index][0]=value
				if key == "item1": champsItems[index][1]=value
				if key == "item2": champsItems[index][2]=value
				if key == "item3": champsItems[index][3]=value
				if key == "item4": champsItems[index][4]=value
				if key == "item5": champsItems[index][5]=value
				if key == "item6": champsItems[index][6]=value
				if key == "winner": winner.append(value)
				if key == "magicDamageDealtToChampions": magicDamageDealtToChampions.append(value)
				if key == "magicDamageTaken": magicDamageTaken.append(value)
				
				if key == "physicalDamageDealtToChampions": physicalDamageDealtToChampions.append(value)
				if key == "physicalDamageTaken": physicalDamageTaken.append(value)
				if key == "totalDamageDealtToChampions": totalDamageDealtToChampions.append(value)
				if key == "totalDamageTaken": totalDamageTaken.append(value)
				
				if key == "trueDamageDealtToChampions": trueDamageDealtToChampions.append(value)
				if key == "trueDamageTaken": trueDamageTaken.append(value)
				if key == "totalHeal": totalHeal.append(value)
				
				
	#save buidl info for each champion in LoL
	with open(os.path.join(champInfoPath, champInfoFile)) as champ:
		champData = json.load(champ)
		for index, champId in enumerate(championIds):
			for champ, champInfo in champData["data"].iteritems():
				if champId == champInfo["id"]:
					championNames.append(champInfo["name"])
	givenInfo["matchId"] = matchInfoFile
	givenInfo["champId"] = championIds
	givenInfo["winner"] = winner
	givenInfo["champItems"] = champsItems
	givenInfo["championName"] = championNames
	givenInfo["lane"] = lane
	givenInfo["role"] = role
	givenInfo["totalHeal"] = totalHeal
	givenInfo["magicDamageDealtToChampions"] = magicDamageDealtToChampions
	givenInfo["magicDamageTaken"] = magicDamageTaken
	givenInfo["physicalDamageDealtToChampions"] = physicalDamageDealtToChampions
	givenInfo["physicalDamageTaken"] = physicalDamageTaken
	givenInfo["totalDamageDealtToChampions"] = totalDamageDealtToChampions
	givenInfo["totalDamageTaken"] = totalDamageTaken
	givenInfo["trueDamageDealtToChampions"] = trueDamageDealtToChampions
	givenInfo["trueDamageTaken"] = trueDamageTaken

	return givenInfo

#saves the match ids and relvant info to json file by parsing matchInfo on everymatchId given in NA.json
def saveUsefulMatchInfo(originMatchInfoPath, matchInfoFile):
	index = 0
	exceptionCount = 0;
	gottenInfo = {}
	oneMatch = {}
	allMatches = {}
	for directory, ret_type, match_files in os.walk(originMatchInfoPath):
		for match in match_files:
			try:
				gottenInfo=getChampsAndItemsGivenMatch(originMatchInfoPath, match)
				oneMatch["matchId"] = match[:-5]
				oneMatch["matchInfo"] = gottenInfo
				allMatches[oneMatch["matchId"]] = oneMatch["matchInfo"]
			except Exception:
				exceptionCount+=1
			index+=1

	with open(matchInfoFile,'w') as outfile:
		json.dump(allMatches, outfile)

#returns the champion builds that won a match and their respective lanes
def getWinBuildsForEachChamp(matchInfoPath, matchInfoFile):
    	
	#creates a dir called allChamps that is ready to hold all champs builds
	champInfoPath = "../../champions/"
	champInfoFile = "champs.json"
	allChamps = {}
	with open(os.path.join(champInfoPath, champInfoFile)) as champ:
		champData = json.load(champ)
		for champName, champInfo in champData["data"].iteritems():
			allChamps[str(champInfo["id"])] = {"lane":{"TOP":{"build":[]},"BOTTOM":{"build":[]},"MIDDLE":{"build":[]},"JUNGLE":{"build":[]}}} 
			
	champ_id_dict = {}
    	with open(os.path.join(matchInfoPath, matchInfoFile)) as allMatches:
        	allMatchesData = json.load(allMatches)

		#parsed_match_info = []
		for matchId, match in allMatchesData.iteritems():
			lane = match["lane"]
			winner = match["winner"]
			champ_id = match["champId"]
			champ_items = match["champItems"]
			mddtc = match["magicDamageDealtToChampions"]
			mdt = match["magicDamageTaken"]
			pddtc = match["physicalDamageDealtToChampions"]
			pdt = match["physicalDamageTaken"]
			totalddtc = match["totalDamageDealtToChampions"]
			totaldt = match["totalDamageTaken"]
			trueddtc = match["trueDamageDealtToChampions"]
			truedt = match["trueDamageTaken"]
			totalHeal = match["totalHeal"]

		    #sort the items
			item_count = 0
			for x in range(item_count, len(champ_items)):
				champ_items[x] = sorted(champ_items[x])

			for line in zip(lane, winner, champ_id, champ_items, mddtc, mdt, pddtc, pdt, totalddtc, totaldt, trueddtc, truedt, totalHeal):
				if line[1] == True:
					allChamps[str(line[2])]["lane"][str(line[0])]["build"].append((line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]))
	return allChamps


#Returns the best Builds for each champion in each lane
def getFinalWinBuildForEachChamp(allChamps):
	finalBuilds = {}
	
	for champId, lanes in allChamps.iteritems():
		finalBuilds[champId] = {"lane":{"TOP":{"build":[]},"BOTTOM":{"build":[]},"MIDDLE":{"build":[]},"JUNGLE":{"build":[]}}} 
		for lane in lanes["lane"].iteritems():
			bestBuild = []
			bestCount = 0
			currCount = 0
			currBuild = []
			for x in range(len(lane[1]["build"])):
				for inx, build in enumerate(lane[1]["build"]):
					currBuild = lane[1]["build"][x]
					currCount+=1
					if inx > x:
						if build in currBuild:
							currCount+=1
				if currCount >bestCount:
					bestBuild = currBuild
					bestCount = currCount	
				currCount = 0
			
			finalBuilds[champId]["lane"][str(lane[0])]["build"] = bestBuild
			

	return finalBuilds

#runs the functions to get final builds and saves as json file
def getBuilds(matchInfoPath, matchInfoFile, finalBuildSaveFile):
	
	allChamps = getWinBuildsForEachChamp(matchInfoPath, matchInfoFile)
	finalBuilds = getFinalWinBuildForEachChamp(allChamps)
	with open(finalBuildSaveFile,'w') as outfile:
		json.dump(finalBuilds,outfile)

def main():
	
	matchInfoPath = "./"
	originalMatchInfoPath = "../../matches/matchInfo/5.11/NORMAL_5X5/NA/"
    	matchInfoFile = "na5.11NormMatchInfo.json"
	finalBuildSaveFile = "na5.11NormBuilds.json"

	saveUsefulMatchInfo(originalMatchInfoPath, matchInfoFile)
	getBuilds(matchInfoPath, matchInfoFile, finalBuildSaveFile)


if __name__ == "__main__":
	main()
