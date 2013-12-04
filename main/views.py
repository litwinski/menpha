from django.db.models import Q
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from main.models import Item
from main.forms import ItemForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import ListView
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class Create(CreateView):
	""" Adds an object to database by a user in context"""
	template_name = 'add.html'
	form_class = ItemForm
	model = Item

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(Create, self).form_valid(form)

class Update(UpdateView):
	""" Updates an object in context """
	model = Item
	fields = fields = ['device', 'slug', 'description', 'photo', 'stolen']

	@method_decorator(permission_required('main.change_item', raise_exception=True,))
	def dispatch(self, * args, ** kwargs):
		return super(Update, self).dispatch( * args, ** kwargs)


class DeleteItem(DeleteView):
	""" Deletes the the context object """
	model = Item
	context_object_name = 'to_delete'
	success_url = reverse_lazy('myList')

	@method_decorator(permission_required('main.delete_item'))
	def dispatch(self, * args, ** kwargs):
		return super(DeleteItem, self).dispatch( * args, ** kwargs)

class MyList(ListView):
	""" Lists all the items added by a user."""
	model = Item
	def get_queryset(self):
		qset = Q(created_by=self.request.user)
		#s = Item.objects.get(created_by=self.request.user)
		#return Item.objects.get(created_by=self.request.user)
		return Item.objects.filter(qset).distinct().order_by('-pub_date')

	@method_decorator(login_required())
	def dispatch(self, * args, ** kwargs):
		return super(MyList, self).dispatch( * args, ** kwargs)


# Function Based Views. Eliminate gradually when CBV takes over.
def base(request):
	""" Old introductory page deprecated"""
	return render(request, 'intro.html')

def intro(request):
	""" Current introductory page in use"""
	return render(request, 'metrika.html')

@login_required
def home(request):
	""" App homepage. This page displays the search box"""
	return render(request, 'index.html',)

@login_required
def search(request):
	""" Displays results of the searched query"""
	query = request.GET.get('q', '')
	if query:
		qset = Q(slug__iexact=query, stolen__iexact='s') 
		results = Item.objects.filter(qset).distinct()
	else:
		results = []
		
	return render(request, "search.html", {
		'results': results,
		'query': query,
	})

@login_required
def detail(request, slug):
	""" Still used to display detail of object. Should be replaced with 
	Class Based View DetailView class."""
	s = get_object_or_404(Item, slug = slug)
	return render(request, 'imei-detail.html', {'s':s})	