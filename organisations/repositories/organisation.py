from organisations.models import Organisations


class OrganisationRepository:

    def __int__(self):
        self.organisation_manager = Organisations.objects

    def create(self, organisation_data):
        return self.organisation_manager.create(
            name=organisation_data.get("name"),
            country=organisation_data.get("country_id"),
            address=organisation_data.get("address")
        )

    def find_one(self, organisation_id):
        return self.organisation_manager.get(id=organisation_id)

    def find_by_name(self):
        pass

    def find_all(self):
        return self.organisation_manager.all()

    def delete(self, organisation_id):
        organisation = self.find_one(organisation_id)
        organisation.delete()

    def update(self, organisation_id, organisation_data):
        organisation = self.find_one(organisation_id)
        organisation.name = organisation_data.name
        organisation.country = organisation_data.country

        return organisation.save()

    def select_id_and_organisations_name(self):
        return self.organisation_manager.all(["id","name"])
