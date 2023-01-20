import pandas as pd
import requests
from twilio.rest import Client

account_sid = 'ACa6f547287077124615bc0304f7497455'
auth_token = '5dffaab217eef737df69df327e4fc28d'
client = Client(account_sid, auth_token)


news_url = 'https://newsapi.org/v2/everything?q=Tesla&language=en&coutry=us&sortBy=publishedAt&apiKey=07d7128697cf4aaf8dbadefe3d6ee06d'
news = requests.get(news_url)
latest_news = news.json()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_INTRADAY"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=60min&apikey=EK0IRU6IDBOEEJ6D'
r = requests.get(url)
data = r.json()

time_series = data['Time Series (60min)']
desired_time = '20:00:00'
desired_data = {k:v for k, v in time_series.items() if desired_time in k}
df = pd.DataFrame.from_dict(desired_data)
df_new = df.iloc[:, [0,1,]]
print(df_new)
close_price_1= float(df_new.iat[3, 1])
close_price_2 = float(df_new.iat[3, 0])
print(close_price_1)
print(close_price_2)
stock = ((close_price_2 - close_price_1) /close_price_1) * 100



def stock_price(stock_check):
    if close_price_1 > close_price_2:
        return stock
    else:
        return stock
price = stock_price(stock)
Tesla_stock = round(abs(price))
print(Tesla_stock)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
Tesla_news_1 = latest_news['articles'][0]['title']
Tesla_news_2 = latest_news['articles'][1]['title']
Tesla_news_3 = latest_news['articles'][2]['title']
Tesla_news_1_description = latest_news['articles'][0]['description']
Tesla_news_2_description = latest_news['articles'][1]['description']
Tesla_news_3_description = latest_news['articles'][2]['description']
print(Tesla_news_1)
print(Tesla_news_1_description)
print(Tesla_news_2)
print(Tesla_news_2_description)
print(Tesla_news_3)
print(Tesla_news_3_description)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


if close_price_1 > close_price_2:
    message = client.messages.create(
        messaging_service_sid='MG03d75c6095398fe0ad243d00e246dc30',
        body=f'TSLA: 🔻{Tesla_stock}%'
             f'Headline:{Tesla_news_1}'
             f'Brief:{Tesla_news_1_description}'
             f'Headline:{Tesla_news_2}'
             f'Brief:{Tesla_news_2_description}'
             f'Headline:{Tesla_news_3}'
             f'Brief:{Tesla_news_3_description}',
        to='+919844379098'
    )
else:
    message = client.messages.create(
        messaging_service_sid='MG03d75c6095398fe0ad243d00e246dc30',
        body=f'TSLA: 🔺{Tesla_stock}%'
             f'Headline:{Tesla_news_1}'
             f'Brief:{Tesla_news_1_description}'
             f'Headline:{Tesla_news_2}'
             f'Brief:{Tesla_news_2_description}'
             f'Headline:{Tesla_news_3}'
             f'Brief:{Tesla_news_3_description}',
    to = '+919844379098'
    )





#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

