from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question, PostForm



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def get_answer(request,question_id):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			answer = form.cleaned_data['your_answer']
			name = form.cleaned_data['your_name']
			return HttpResponseRedirect('/thanks/')
	else:
        	form = NameForm()
	return HttpResponseRedirect('/thanks/')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
