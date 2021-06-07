import GetOldTweets3 as got
import datetime
import pandas as pd
import time

start=datetime.datetime(2017, 3, 15)
end=datetime.datetime(2018, 3, 15)

date_generated=[start+datetime.timedelta(days=x) for x in range(0,(end-start).days)]

days_range=[]

for date in date_generated:
    days_range.append(date.strftime("%Y-%m-%d"))

tweetCriteria = got.manager.TweetCriteria().setUsername("elonmusk").setSince("2017-01-20").setUntil("2019-12-31")

print("데이터 수집 시작========")
start_time = time.time() 
tweet = got.manager.TweetManager.getTweets(tweetCriteria) 
print("데이터 수집 완료======== {0:0.2f}분".format((time.time() - start_time)/60)) 
print("=== 총 트윗 개수 {} ===".format(len(tweet)))

tweet_list = [] 
for i in tqdm(tweet):
    username = i.username 
    tweet_date = i.date.strftime("%Y-%m-%d") 
    tweet_time = i.date.strftime("%H:%M:%dS") 
    content = i.text 
    favorites = i.favorites 
    retweets = i.retweets 
    link = i.permalink 
    info_list = [username, tweet_date, tweet_time, content, favorites, retweets, link] 
    tweet_list.append(info_list)

twitter_df = pd.DataFrame(tweet_list, columns = ["ID", "날짜", "시간", "내용", "리트윗 수", "좋아요 수", "링크"])

twitter_df.to_csv("twitter_trump.csv", index = False)
print("=== {}개의 트윗 저장 ===".format(len(tweet_list)))


