class User:
    active_users = 0
    @classmethod
    def display_active_users(cls):
        return f"there is {cls.active_users} in the site"
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        User.active_users += 1
    def full_name(self):
        return f"{self.name} {self.lastname}"
class Moderator(User):
    active_moderator = 0
    @classmethod
    def display_active_moderators(cls):
        return f"there is {cls.active_moderator} in the site"
    def __init__(self,name, lastname, community):
        super().__init__(name, lastname)
        self.community = community
print(User.display_active_users())
u1 = User("ali", "Korkmaz")
m1 = Moderator("Yağmur", "Korkmaz", "yazılım")
print(User.display_active_users())

