from django.http import HttpResponse


def index(request):
    return HttpResponse("The polls app.... hooray")


def view(request):
    return HttpResponse("Wanna see an item? Sikeeeee!!!")


def create(request):
    return HttpResponse("Wanna create an item... alright \n\n\n double sike!")


def store(request):
    return HttpResponse("Ain't you tired of the sikes?")


def edit(request):
    return HttpResponse(
        "You could not live with you own failure. Where did that bring you? Back to me"
    )


def update(request):
    return HttpResponse(
        "Mr. yale, there's no need to both cuss and yell, one of them will suffice"
    )


def destroy(request):
    return HttpResponse("Dread it, run from it, destiny arrives all the same!")
