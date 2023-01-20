import pandas as pd
import requests
from twilio.rest import Client

#Replace the account_sid and auth_token from the details you get from Twilio account.
account_sid = '*******************************'
auth_token = '*********************************'
client = Client(account_sid, auth_token)

#Replace the apikey with the actual API key that you get from newsapi
news_url = 'https://newsapi.org/v2/everything?q=Tesla&language=en&coutry=us&sortBy=publishedAt&apiKey=*********'
news = requests.get(news_url)
latest_news = news.json()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_INTRADAY"

#Replace the apikey with the actual API key that you get from alphavantage

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=60min&apikey=************'
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


#All the latest news and description of the news will be available in this section using print is optional
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



# This will send a message to your phone number.
# You can remove the Tesla_news_2, Tesla_news_3, Tesla_news_2_description and Tesla_news_3_description. from the message if you don't need it.

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
        to='+9198111111118'
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
    to = '+9191111111118'
    )
    






