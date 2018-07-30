import requests
#importing the requests library
import json

 # defining the api-endpoint
API_ENDPOINT = "http://67.205.135.0:6000/peers"
  
# data to be sent to api
json_data = {"url" : "23.99.178.214"}
jsonText = json.dumps(json_data) #convert to json type 

# sending post request and saving response as response object
response = requests.post(url = API_ENDPOINT, data = jsonText)

# extracting response text
peer_data_response = response
print("The data posted was: " + peer_data_response.text)

peers_as_json = json.loads(peer_data_response.text)
i = 0
blockchain_list = [dict() for x in range ((len(peers_as_json['peers'])) -1)]   #make an array of dictionaries, length of urls retrieved

for peer in peers_as_json['peers']: #now check each url and see which ones are alive!
   # print("peer is " + peer)
    if (peer != "23.99.178.214"): #if peer isn't self....
        serverStatusCode = requests.get(peer + '/print')
       # print(serverStatusCode.status_code)
        blockchain_list[i]['address'] = peer
        if (serverStatusCode.status_code == 200):
            blockchain_list[i]['health']  = "ALIVE"
            blockchain_list[i]['status'] = serverStatusCode.status_code
            blockchain_list[i]['text'] = serverStatusCode.text
        else:
            blockchain_list[i]['health']  = "DEAD"
            blockchain_list[i]['status'] = serverStatusCode.status_code
            blockchain_list[i]['text'] = "NULL"
        i = i + 1 #bump the counter
    

print(len(blockchain_list))

for chain in blockchain_list:
    try:
        print(chain["address"] + " is " + chain["health"] +  " with status_code of " + str(chain["status"]))
        print("Chain data is " + chain["text"])
    except:
        print("one item could not be printed")
     




