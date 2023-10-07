from organisations.models import User


class UserRepository:
    def __int__(self):
        self.user_manager = User.objects

    def create(self, user):
        self.user_manager.create(
            username=user.username,
            email=user.email,
            password=user.password,
            organisation=user.organisation_id
        )

    def find_one(self, user_id):
        return self.user_manager.get(id=user_id)

    def find_by_username(self, username):
        return self.user_manager.get(username=username)

    def find_all(self):
        return self.user_manager.all()

    def update(self, user_id, user_data):
        user = self.find_one(user_id)
        user.password = user_data.get("password")
        user.username = user_data.get("username")

        return user.save()

    def delete(self, user_id):
        user = self.find_one(user_id)
        user.delete()
