import requests	#to request the json data from the site it is at
import json #to save data format as

#gets and saves a json file of the champions and info about them
def champs():
    apiKey = key()
    r = requests.get("https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?api_key="+apiKey)

    file_ = open('champs.json', 'w')
    file_.write(json.dumps(r.json()))
    file_.close()

#reads a file that contains a key for the Riot API
def key():
    line = open("../../../nsr/key/key.txt", "r")
    key = str(line.readline()).rstrip()
    line.close

    return (key)

#run app
if __name__ == '__main__':
    champs()
