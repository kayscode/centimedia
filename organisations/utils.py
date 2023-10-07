from ogranisations.repositories import CountryRepository
from ogranisations.repositories import OrganisationRepository


def get_country_list():
    country_repository = CountryRepository()
    countries = country_repository.find_all()
    country_choices = []

    for country in countries:
        country_choices.append((country.id,country.name))

    return country_choices


def generate_organisation_select_form_choices():
    organisation_repository = OrganisationRepository()
    organisations_data = organisation_repository.select_id_and_organisations_name()
    organisations_choices = []

    for organisation in organisations_data:
        organisations_choices.append((organisation.id, organisation.name))

    return organisations_choices
