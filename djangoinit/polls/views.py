from django.db.models import F, Count
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils.timezone import now

from .models import Question, Choice


# def index(request):
#     latest_questions_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_questions_list": latest_questions_list,
#     }
#     print(latest_questions_list)

#     return HttpResponse(template.render(context, request))


# def show(request, question_id):
#     print(question_id)
#     # for q in Question.objects.all():
#     #     if q.id == question_id:
#     try:
#         question = Question.objects.get(pk=question_id)
#         template = loader.get_template("polls/show.html")
#         context = {
#             "question": question,
#         }
#     except Question.DoesNotExist:
#         raise Http404(f"Question with id {question_id} not found")
#     return HttpResponse(template.render(context, request))
#     # return HttpResponse(q)
#     # return HttpResponse(
#     #     f"Wanna see an item? Sikeeeee!!! No item found for id {question_id}"
#     # )


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
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/show.html",
            {
                "question": question,
                "error_message": "No choice selected.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# def result(request, question_id):
#     # print(question_id)
#     # return HttpResponse(f"results for {question_id}")

#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_questions_list"

    def get_queryset(self):
        return (
            Question.objects.annotate(num_choices=Count("choice"))
            .filter(num_choices__gt=0)
            .filter(pub_date__lte=now())
            .order_by("-pub_date")[:10]
        )


class ShowView(generic.DetailView):
    # model = Question
    template_name = "polls/show.html"

    def get_queryset(self):
        return (
            Question.objects.annotate(num_choices=Count("choice"))
            .filter(num_choices__gt=0)
            .filter(pub_date__lte=now())
        )


class ResultsView(generic.DetailView):
    # model = Question
    template_name = "polls/results.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=now())
