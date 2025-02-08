from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question


def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_questions_list": latest_questions_list,
    }
    print(latest_questions_list)

    return HttpResponse(template.render(context, request))


def show(request, question_id):
    print(question_id)
    # for q in Question.objects.all():
    #     if q.id == question_id:
    try:
        question = Question.objects.get(pk=question_id)
        template = loader.get_template("polls/show.html")
        context = {
            "question": question,
        }
    except Question.DoesNotExist:
        raise Http404(f"Question with id {question_id} not found")
    return HttpResponse(template.render(context, request))
    # return HttpResponse(q)
    # return HttpResponse(
    #     f"Wanna see an item? Sikeeeee!!! No item found for id {question_id}"
    # )


def create(request):
    return HttpResponse("Wanna create an item... alright \n\n\n double sike!")


def store(request):
    return HttpResponse("Ain't you tired of the sikes?")


def edit(request, question_id):
    print(question_id)
    return HttpResponse(
        f"You could not live with you own failure. Where did that bring you? Back to me. Question Id: {question_id}"
    )


def update(request, question_id):
    print(question_id)
    return HttpResponse(
        f"Mr. yale, there's no need to both cuss and yell, one of them will suffice. Question Id: {question_id}"
    )


def destroy(request, question_id):
    print(question_id)
    return HttpResponse(
        f"Dread it, run from it, destiny arrives all the same! Question Id: {question_id}"
    )


def vote(request, question_id):
    print(question_id)
    return HttpResponse(f"voting on Question {question_id}")


def result(request, question_id):
    print(question_id)
    return HttpResponse(f"results for {question_id}")
