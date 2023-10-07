from django.shortcuts import render, redirect


def get_list_confirmation_demands(request):
    """
        list all no treat confirmation demands by descending order
    """

    if request.method == "GET":
        # retrieve all no treated confirmation demands
        context = {

        }
        return render(request, "", context)


def show_confirmation_demand(request):
    """
        see confirmation demand in details
    """

    if request.method == "GET":
        # fetch confirmation demand
        context = {

        }
        return render(request, "", context)


def reject_confirmation_demand(request):
    """
        mark a confirmation demands as rejected
    """

    if request.method == "POST":
        # fetch confirmation demand by id

        # update the status of the confirmation demands as rejected

        return redirect("")  # redirect to the notifications demands list


def accept_confirmation_demand(request):
    """
            mark a confirmation demands as rejected
        """

    if request.method == "POST":
        # fetch confirmation demand by id

        # update the status of the confirmation demands as accepted

        return redirect("")  # redirect to be notifications demands list
