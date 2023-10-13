from organisations.models import User


class UserRepository:

    @classmethod
    def create(cls, user):
        return User.objects.create(
            username=user.username,
            email=user.email,
            password=user.password,
            organisation=user.organisation_id
        )

    @classmethod
    def find_one(cls, user_id):
        return User.objects.get(id=user_id)

    @classmethod
    def find_by_username(cls, username):
        return User.objects.get(username=username)

    @classmethod
    def find_all(cls):
        return User.objects.all()

    @classmethod
    def update(cls, user_id, user_data):
        user = cls.find_one(user_id)
        user.email = user_data.get("email")
        user.password = user_data.get("password")
        user.username = user_data.get("username")

        return user.save()

    @classmethod
    def delete(cls, user_id):
        user = cls.find_one(user_id)
        user.delete()
