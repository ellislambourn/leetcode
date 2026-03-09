class Twitter:

    def __init__(self):
        self.posts = {} # user : [(time, postId)]
        self.time = 0
        self.following = {} # user : set(userIds)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.createUser(userId)
        self.posts[userId].append((self.getTime(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.posts:
            self.createUser(userId)
        # all the tweets:
        tweets = []
        tweets += [post for post in self.posts[userId]] # users own tweets
        tweets += [post for followerID in self.following[userId] for post in self.posts[followerID]] # following tweets
        
        tweets.sort(reverse = True)
        return [tweetId[1] for tweetId in tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.posts:            
            self.createUser(followerId)
        if followeeId not in self.posts:
            self.createUser(followeeId)
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.posts:
            self.createUser(followerId)
        if followeeId not in self.posts:
            self.createUser(followeeId)
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
    def getTime(self) -> int:
        self.time += 1
        return self.time

    def createUser(self, userId):
        self.posts[userId] = []
        self.following[userId] = set()