import os
import json


with open('cache.json') as b:
  dataCache = json.load(b)

#Loop through the metaboss decode output
for file in os.listdir("mints_data"):

  mintId = os.path.basename(file).split('.')[0]
  fileOpen = open("mints_data/" + file)
  fileData = json.load(fileOpen)

  #Loop through the cache file items to gather the new uri
  for c in dataCache["items"]:

    #Check if the name is the same
    if dataCache["items"][c]["name"] == fileData["name"]:

      #Format data
      dataOutput = {
        "mint_account": mintId,
        "uri": dataCache["items"][c]["metadata_link"]
      }

      with open("output/" + fileData["name"] + ".json", "w") as f:
        json.dump(dataOutput, f)
      
      break
