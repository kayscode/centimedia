from organisations.models import Organisations


class OrganisationRepository:

    @classmethod
    def create(cls, organisation_data):
        return Organisations.objects.create(
            name=organisation_data.get("name"),
            country=organisation_data.get("country_id"),
            address=organisation_data.get("address")
        )

    @classmethod
    def find_one(cls, organisation_id):
        return Organisations.objects.get(id=organisation_id)

    @classmethod
    def find_by_name(cls):
        pass

    @classmethod
    def find_all(cls):
        return Organisations.objects.all()

    @classmethod
    def delete(cls, organisation_id):
        organisation = cls.find_one(organisation_id)
        organisation.delete()

    @classmethod
    def update(cls, organisation_id, organisation_data):
        organisation = cls.find_one(organisation_id)
        organisation.name = organisation_data.name
        organisation.country = organisation_data.country

        return organisation.save()

    @classmethod
    def select_id_and_organisations_name(cls):
        return Organisations.objects.all(["id", "name"])
