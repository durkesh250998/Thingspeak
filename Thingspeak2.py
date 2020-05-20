from urllib.request import urlopen

import json
import time


READ_API_KEY=''
CHANNEL_ID=''


while True:
    TS = urlopen("https://api.thingspeak.com/channels/999233/feeds.json?api_key=".format(CHANNEL_ID,READ_API_KEY))

    response = TS.read()

    data=json.loads(response.decode('utf-8'))

    print(data)

    print (data["feeds"][1]["field1"])

    a=data["feeds"][1]["field1"]

    if a=='1' :
        print("wood")
        break

    elif a=='2' :
        print("metal")
        break

    else:
        print("plastic")
        break

    TS.close()
