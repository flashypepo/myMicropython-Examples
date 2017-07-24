'''
get the subscriber count of a YouTube channel
2017-0604 PePo: Youtube channel "AllesOverHondenTrimmen"
pre-condition: esp32 is connected to local wifi
'''
# #############
# configuration
# #############
# APIKEY = "YOURAPIKEY"# YouTube Data API v3 key generated here: https://console.developers.google.com
APIKEY = 'AIzaSyBSSYCxEHpVWDEFxUlLCnYaz_gdkXNQsxQ' #2017-0604

# ChannelId van het kanaal waar je de subscribers count van wilt weten.
# 1. My YouTube channel id -- subscribers count = 0 ;-(
# CHANNELID = "UCIMAi9RkqOehE1l0dY7vxIw"
# 2. educ8st.tv YouTube channel id -- subscribers count ±35890
CHANNELID = "UCxqx59koIGfGRRGeEm5qzjQ"
# 3. TODO: opvragen die van AllesOverHondenTrimmen
# CHANNELID = ""
# TODO: via Account-photo gear, YouTube instellingen, and then "advanced"
# you will see youtube ID and youtube channel ID.

# #############
# setup
# #############
print("Device must be connected to WiFi")
APIHOST = "www.googleapis.com"
subscribers = 0
subscribersBefore = 0

# #############
# get connected and request YouTube statistics of ChannelId
# #############
import socket
s = socket.socket()
addr = socket.getaddrinfo(APIHOST, 443)
cmd = b'GET /youtube/v3/channels?part=statistics&id=%s&key=%s HTTP/1.1\r\n%s\r\nUser-Agent: ESP8266/1.1\r\nConnection: close\r\n\r\n' % CHANNELID, APIHOST, APIKEY
s.send(cmd)

# #############
# receive data
# #############
# TODO: fine-tune all statements by trial-and-error !!!!
s.recv(1000)
html = _  # save data
html.split(b'\r\n\r\n') # convert to list of json data
_[-1] # last element is json-data ???
data = _ # save last element, json-data we want ??

# voorbeeld van JSON data dat ik terugkrijgt (mijn APIKEY + educ8st.tv ChannelId
# opgevraagd via webbrowser https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCxqx59koIGfGRRGeEm5qzjQ&key=AIzaSyBSSYCxEHpVWDEFxUlLCnYaz_gdkXNQsxQ
'''
{
 "kind": "youtube#channelListResponse",
 "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/tP0IcAsqQLqvW9bO1wTAlCXvwD8\"",
 "pageInfo": {
  "totalResults": 1,
  "resultsPerPage": 1
 },
 "items": [
  {
   "kind": "youtube#channel",
   "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/5mwl7HgPTlVfavGZwk8CEEZooQ0\"",
   "id": "UCxqx59koIGfGRRGeEm5qzjQ",
   "statistics": {
    "viewCount": "3740732",
    "commentCount": "0",
    "subscriberCount": "35890",
    "hiddenSubscriberCount": false,
    "videoCount": "126"
   }
  }
 ]
}
'''

# #############
# parse json-data
# #############
import json
json.loads(data) # returns dictionary
data = - # save last output

# check structures, it should be similar to Arduino code:
#subscribers = root["items"]["statistics"]["subscriberCount"];
subscribers = data['items']['statistics']['subscriberCount']
print('... subscribers:', subscribers)

# see also StackOverFlow: https://stackoverflow.com/questions/31416862/parse-youtube-subscribers-count-with-new-youtube-api-v3

