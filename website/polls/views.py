from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question, Answer
from polls.forms import PostForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
#from django.contrib.auth.views import LoginView

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
			question = Question.objects.get(id=question_id) 
			answer = Answer(answer_text=answer, author_text=name, question = question)
			answer.save()
			return HttpResponseRedirect('/polls/')
	else:
			form = NameForm()
	return HttpResponseRedirect('/polls/')

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/polls/')
    else:
        return HttpResponseRedirect('/login/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/logout_success/')

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
