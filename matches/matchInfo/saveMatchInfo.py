import json, os
import requests
import time

#Query API for matchInformation from given matchID's.
#This scrip queries and saves Ranked & Normal matches in patches 5.11 and 5.14
#Uses our two dev keys to get requests a quickly as possible(tanglewreak's and lizabeth's keys)
#5.11 norm saved
#5.11 ranked saved
#5.14 norm saved
#5.14 ranked saved
#manually change the patch & ranked/normal match info type you want in the jsonPath and savePath


#get and use the two dev key's
line = open("../../../../nsr/key/key.txt", "r")
key1 = str(line.readline()).rstrip()
key2 = str(line.readline()).rstrip()
line.close
jsonPath = "../AP_ITEM_DATASET/5.11/RANKED_SOLO/" 
jsonFile = "NA.json"
savePath = "5.11/RANKED_SOLO/NA/"
indexAll = 0
indexT = 0
indexL = 0
exceptionCount = 0
exceptionLines = ""

apiKeyTangle = key1
apiKeyLiz = key2

with open(os.path.join(jsonPath,jsonFile)) as json_file:
	jsonText = json.load(json_file)
	for matchId in jsonText:
		if (indexAll >= 20) and (indexAll % 20 == 0):
			#sleep long enough to run queries again
			time.sleep(10)
			indexT = 0
			indexL = 0
		indexAll += 1
		if indexT < 10:
			requestPath = "https://na.api.pvp.net/api/lol/na/v2.2/match/" + str(matchId) + "?api_key=" + apiKeyTangle
			indexT+=1
		else:
			requestPath = "https://na.api.pvp.net/api/lol/na/v2.2/match/" + str(matchId) + "?api_key=" + apiKeyLiz
			indexL+=1
			if indexL >= 10:
				indexL=0
				indexT=0	
		try:
			request = requests.get(requestPath)
			#with open((savePath+str(matchId)+".json"),'w') as outfile:
			with open(("test/"+str(matchId)+".json"),'w') as outfile:
				json.dump(request.json(), outfile)
		except Exception:
			print "Exception"
			exceptionCount +=1
			exceptionLines += ", "+ str(matchId)
			time.sleep(10)
			indexT=0
			indexL=0


