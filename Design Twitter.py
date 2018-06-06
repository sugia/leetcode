'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet_id = 0
        self.user_tweet = {}
        self.user_user = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.user_tweet:
            self.user_tweet[userId] = [(self.tweet_id, tweetId)]
            self.tweet_id += 1
        else:
            self.user_tweet[userId].append((self.tweet_id, tweetId))
            self.tweet_id += 1
        
        # print('postTweet', self.user_tweet)
        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = []
        if userId in self.user_tweet:
            res += self.user_tweet[userId]
        
        if userId in self.user_user:
            for user in self.user_user[userId]:
                if user in self.user_tweet:
                    res += self.user_tweet[user]
                

        res.sort(key = lambda x: x[0], reverse = True)
        
        tweet = []
        for i in xrange(min(len(res), 10)):
            tweet.append(res[i][1])
            
        return tweet
    
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        
        if followerId not in self.user_user:
            self.user_user[followerId] = set([followeeId])
        else:
            if followeeId not in self.user_user[followerId]:
                self.user_user[followerId].add(followeeId)
        
        # print('follow', self.user_user)
        
    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        
        if followerId == followeeId:
            return
        
        if followerId in self.user_user:
            if followeeId in self.user_user[followerId]:
                self.user_user[followerId].remove(followeeId)
                
        # print('unfollow', self.user_user)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
