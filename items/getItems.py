import requests	#to request the json data from the site it is at
import json #to save data format as

#gets and saves a json file of the champions and info about them
def items():
    line = open("../../../nsr/key/key.txt", "r")
    key = str(line.readline()).rstrip()
    line.close

    r = requests.get("https://na.api.pvp.net/api/lol/static-data/na/v1.2/item?api_key=" + key)

    file_ = open('items.json', 'w')
    file_.write(json.dumps(r.json()))
    file_.close()

#run app
if __name__ == '__main__':
    items()
