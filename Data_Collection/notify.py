from twilio.rest import Client
import scraper

# Your Account SID from twilio.com/console
account_sid = "ACbd5a48eda8cb7c440bdd78ec7cef06fd"
# Your Auth Token from twilio.com/console
auth_token  = "4ab9007474b3aa00a6683ff39f432a74"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body= scraper.getCurrentStockPrice("MSFT"),
                              from_='+17069984045',
                              status_callback='http://postb.in/1234abcd',
                              to='+16365797036'
                          )
print(message.sid)