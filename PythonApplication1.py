import requests 
import pprint
import json
import os
from twilio.rest import Client
r = requests.get(os.environ.get('TFL_API'))
response_data = r.json()
i = 0     
Text = []
while i < len(r.json()) :
    if (response_data[i]["lineStatuses"][0]["statusSeverityDescription"]) != "Good Service":
        Text.append(response_data[i]["name"]+" - "+response_data[i]["lineStatuses"][0]["statusSeverityDescription"])
    i = i + 1
if(len(Text) > 0):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body= str(Text)[1:-1],
                         from_= os.environ.get('TWILIO_FROM_NUM'),                         
                         to=os.environ.get('TWILIO_TO_NUM'))
    print(message.sid)
    print(Text) 
else: print("No Reported Issues")    

        







