from ogranisations.repositories import OrganisationRepository


def generate_organisation_select_form_choices():
    organisation_repository = OrganisationRepository()
    organisations_data = organisation_repository.select_id_and_organisations_name()
    organisations_choices = []

    for organisation in organisations_data:
        organisations_choices.append((organisation.id, organisation.name))

    return organisations_choices
