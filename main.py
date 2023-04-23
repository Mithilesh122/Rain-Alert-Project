import requests
from twilio.rest import Client
api_key="93777a505aef927eb76cefe0f61e289e"
parameters={"lat":15.317277,
            "lon":75.713890,
            "appid":"93777a505aef927eb76cefe0f61e289e"}
response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
data=response.json()
weather_codes = [x['weather'][0]['id'] for x in data['hourly']]
if any(code in weather_codes for code in range(200, 600)):
    # It's raining, send an SMS
    account_sid = 'ACbc8d3dca6b8638750b8694923043a807'
    auth_token = '4984c4230158922dc6804c819aea91db'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's raining today!",
            from_='+16812069007',
            to='+918310714930'
        )

    print(message.sid)
else:
    # It's not raining
    account_sid = 'ACbc8d3dca6b8638750b8694923043a807'
    auth_token = '4984c4230158922dc6804c819aea91db'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's not raining today!",
        from_='+16812069007',
        to='+918310714930'
    )

    print(message.sid)