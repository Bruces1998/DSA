from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.tweet_count = 0
        self.following = defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_count += 1
        self.tweets[userId].append((self.tweet_count, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        for tc, tweet_id in self.tweets[userId]:
            news.append((tc, tweet_id))
        
        for following in self.following[userId]:
            for tc, tweet_id in self.tweets[following]:
                news.append((tc, tweet_id))
        news.sort(reverse=True, key=lambda x: x[0])
        end_index = min(10, len(news))
        return [j for (i, j) in news[:end_index]]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)