from organisations.models import Country


class CountryRepository:

    def __int__(self):
        self.country_manager = Country.objects

    def create(self, continent: str, name: str):
        return self.country_manager.create(
            continent=continent,
            name=name
        )

    def find_one(self, country_id: int):
        return self.country_manager.get(id=country_id)

    def find_by_name(self, name: str):
        return self.country_manager.get(name=name)

    def find_all(self):
        return self.country_manager.all()

    def update(self, country_id, country_data):
        country = self.find_one(country_id)
        country.name = country_data["name"]
        country.continent = country_data["continent"]

        return country.save()

    def delete(self, country_id):
        country = self.find_one(country_id)
        country.delete()

    def select_id_and_country_name(self):
        return self.country_manager.all(["id","name"])