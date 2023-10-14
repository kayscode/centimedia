from organisations.models import User


class UserRepository:

    @classmethod
    def create(cls, user):
        return User.objects.create(
            username=user.get("username"),
            email=user.get("email"),
            password=user.get("password"),
            organisation=user.get("organisation_id"),
            account_type= user.get("account_type")
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
        user.account_type = user.get("account_type")
        user.avatar = user.get("avatar"),
        user.is_active = user.get("is_active")

        return user.save()

    @classmethod
    def delete(cls, user_id):
        user = cls.find_one(user_id)
        user.delete()
