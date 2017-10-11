from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question, Answer
from polls.forms import PostForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#from django.contrib.auth.views import LoginView

def index(request):
	print(request.user)
	if not request.user.is_authenticated:
		messages.error(request, 'Please login first to view the questions!')
		return HttpResponseRedirect('/polls/login/')
	else:
		print("ajhsb")
		latest_question_list = Question.objects.order_by('-pub_date')
		context = {'latest_question_list': latest_question_list}
		return render(request, 'polls/index.html', context)

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth_login(request, user)
				return HttpResponseRedirect('/polls/')
			else:
				messages.error(request, 'Incorrect Password!')
				print("Here")
				return HttpResponseRedirect('/polls/login')
	else:
		return render(request, 'polls/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/polls/login/')
    else:
        form = UserCreationForm()
        return render(request, 'polls/signup.html')

def detail(request, question_id):
	if not request.user.is_authenticated:
		messages.error(request, 'Please login first to view the questions!')
		return HttpResponseRedirect('/polls/login/')
	else:
		question = get_object_or_404(Question, pk=question_id)
		return render(request, 'polls/detail.html', {'question': question})

def get_answer(request,question_id):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			answer = form.cleaned_data['your_answer']
			name = request.user.username
			question = Question.objects.get(id=question_id) 
			answer = Answer(answer_text=answer, author_text=name, question = question)
			answer.save()
			return HttpResponseRedirect('/polls/')
	else:
		return HttpResponseRedirect('/polls/')

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/polls/login/')

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
