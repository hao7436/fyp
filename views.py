from django.shortcuts import render
from .models import *
# Create your views here.
from newsapi import NewsApiClient
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView

                              

def index(request):

 return render(request, 'antiScam/index.html')

def scamType(request):
 
 return render(request, 'antiScam/ScamType.html')

def typeDetail1(request):
 
 return render(request, 'antiScam/typeDetail1-Impersonation.html')

def typeDetail2(request):
 
 return render(request, 'antiScam/typeDetail2-Ecommerce.html')

def typeDetail3(request):
 
 return render(request, 'antiScam/typeDetail3-SMSscams.html')

def typeDetail4(request):
 
 return render(request, 'antiScam/typeDetail4-Internetlove.html')

def stories(request):
 stories = Stories.objects.all().order_by("-id")
 return render(request, 'antiScam/stories.html',{'stories':stories})

def mediaNews(request):
 newsapi = NewsApiClient(api_key='f0517292ba784eb48dbbb16c1535b45b')
 top_headlines = newsapi.get_everything(q='scams')
 #sources = newsapi.get_sources()
 list_b = []
 list_c = []
 
 for item in top_headlines['articles']:
  list_b.append(item['title'])
  list_c.append(item['url'])

 result = zip(list_b, list_c)
 context = {
    'mylist': result,
  }
 
 return render(request, 'antiScam/mediaNews.html',context)

def addStory(request):
 
 
 return render(request, 'antiScam/addStory.html')

def addStoryAction(request):

  if request.method == 'POST':
        form = storyForm(request.POST)
        if form.is_valid():
            stories = Stories()
            stories.authorFname = form.cleaned_data['authorFname']
            stories.authorLname = form.cleaned_data['authorLname']
            stories.authorEmail = form.cleaned_data['authorEmail']
            stories.authorNumber = form.cleaned_data['authorNumber']
            stories.scamTitle = form.cleaned_data['scamTitle']
            stories.scamType = form.cleaned_data['scamType']
            stories.nameOfScamer = form.cleaned_data['nameOfScamer']
            stories.contentOfScamer = form.cleaned_data['contentOfScamer']
            stories.emailOfScamer = form.cleaned_data['emailOfScamer']
            stories.scamDetail = form.cleaned_data['scamDetail']
            stories.save()
            return HttpResponseRedirect('/stories/')
  else:
        stories = Stories.objects.all()
        form = storyForm()
        return render(request, 'antiScam/stories.html',{'stories':stories})

def addCooperationAction(request):

  if request.method == 'POST':
        form = CooperationForm(request.POST)
        if form.is_valid():
            cooperations = Cooperation()
            cooperations.organisationName = form.cleaned_data['organisationName']
            cooperations.organisationEmail  = form.cleaned_data['organisationEmail']
            cooperations.personInContact  = form.cleaned_data['personInContact']
            cooperations.ContactNumber  = form.cleaned_data['ContactNumber']
            cooperations.cooperationDetail  = form.cleaned_data['cooperationDetail']
            cooperations.timestamp  = form.cleaned_data['timestamp']
            cooperations.save()
            return HttpResponseRedirect('/cooperation/')
  else:
        form = CooperationForm()
        return render(request, 'antiScam/cooperation.html')

def addJoinActivitesAction(request):

  if request.method == 'POST':
        form = JoinActivitesForm(request.POST)
        if form.is_valid():
            joinactivites = JoinActivites()
            joinactivites.activitesTitle = form.cleaned_data['activitesTitle']
            joinactivites.joinerName  = form.cleaned_data['joinerName']
            joinactivites.joinerEmail  = form.cleaned_data['joinerEmail']
            joinactivites.joinerContactNumber = form.cleaned_data['joinerContactNumber']
            joinactivites.joinerDob = form.cleaned_data['joinerDob']
            joinactivites.joinAs = form.cleaned_data['joinAs']
            joinactivites.save()
            return HttpResponseRedirect('/activities/')
  else:
        form = JoinActivitesForm()
        return render(request, 'antiScam/Activities.html')



def activities(request):
 activities = AddActivites.objects.all().order_by("-id")
 
 return render(request, 'antiScam/Activities.html',{'activities':activities})

class activitiesList(ListView):
 model = AddActivites
 context_object_name = 'master_activities'

 def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['master_activities'] = AddActivites.objects.all().order_by("-id")
    return context

 def get_template_names(self):

    return 'antiScam/Activities.html'

def activitiesDetail1(request):
 
 return render(request, 'antiScam/activites-detail1.html')

def activitiesDetail2(request):
 
 return render(request, 'antiScam/activites-detail2.html')

def cooperation(request):
 
 return render(request, 'antiScam/cooperation.html')

class ActivitesDetail(DetailView):
 model = AddActivites
 context_object_name = 'addactivites'
 template_name = 'antiScam/activites-detail.html'
 def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['master_activites'] = AddActivites.objects.all()
    return context