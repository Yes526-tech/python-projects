class Comment:
    def __init__(self, username, likes, dislikes):
        self.username = username
        self.likes = likes
        self.dislikes = dislikes
c1 = Comment("Sert", 2002, 5210)
c2 = Comment("Emre", 232, 5033)
c3 = Comment("Yunus", 200, 0)
c4 = Comment("Mert", 20210, 5230)
c5 = Comment("Goril", 33333, 321)


comments = [c1, c2, c3, c4, c5]
for c in comments:
    print(f"username: {c.username}")
    print(f"likes: {c.likes} and dislikes: {c.dislikes}")