from django.shortcuts import render

from organisations.repositories.country import CountryRepository


def country_list(request):
    country_repository = CountryRepository()
    context = {
        "countries": country_repository.find_all()
    }
    return render(request, "", context)


def show_Country(request, country_id):
    country_repository = CountryRepository()

    context = {
        "country": country_repository.find_one(country_id)
    }

    return render(request, "", context)


def create_country(request):
    pass


def store_country(request):
    if request.method == "POST":
        pass


def update_country(request,country_id):

    if request.method == "PUT":
        pass