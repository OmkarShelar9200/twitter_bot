import tweepy
import os # operating system library

def create_api():
  consumer_key = 'LcYClGwdDYq9axyCkB4PeT4Rq'
  consumer_secret = 'rZxPfggFEpTQgjm5uj0Ihf8juoFGHX2lQzFj4n5UGjtlffEfJz'
  access_token = '1292097403873443842-KsDUsiGquUuLVZNc4FlzF82yT1dmTu'
  access_token_secret ='zOVqtvSLXCi5M1fVM9YPtRQYPMtVUN5KLUcLGBIOLyD1C'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
# Complete code
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
    user = api.get_user('OmkarShelar29')
    api.update_profile(name=f'OMKAR|{follower_count(user)} Followers')
    print(f'Updating Twitter Name : OMKAR|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
 
