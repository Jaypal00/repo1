from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from appone.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


class StudCreate(CreateView):
	template_name = 'studcreate.html'
	model = StudentAcademics
	fields = '__all__'
	success_url = reverse_lazy('cr')

class StudList(ListView):
	template_name = 'studlist.html'
	model = StudentInfo

class StudDetailView(DetailView):
	template_name = 'academics.html'
	model = StudentAcademics

class StudDeleteView(DeleteView):
	template_name = 'studdelete.html'
	model = StudentInfo
	success_url = "/list"

class StudUpdateView(UpdateView):
	template_name = 'studupdate.html'
	model = StudentAcademics
	fields = '__all__'
	success_url ="/list"

class SearchView(ListView):
	model = StudentAcademics
	template_name = 'search.html'
	context_object_name = 'all_search_results'

	def get_queryset(self):
		result = super(SearchView, self).get_queryset()
		query = self.request.GET.get('Name')

		if query:
			postresult = StudentAcademics.objects.filter(Name=query)
			result = postresult
			print(result.__dict__)

		else:
			result = None
		return result

class home(ListView):
	template_name = 'home.html'
	model = StudentInfo


import requests
from bs4 import BeautifulSoup


def webscrap(request):
	urls = []
	if request.method=='POST':
		formdata = request.POST
		website=formdata.get('search')
		url = website
		print('*********',website)
		reqs = requests.get(url)
		soup = BeautifulSoup(reqs.text, 'html.parser')


		for link in soup.find_all('a'):
			urls.append(link.get('href'))
			print(link.get('href'))
		return render(request,'webscraping.html',{'form':urls,'web':website})
	else:
		return render(request, 'webscraping.html')
