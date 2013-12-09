# Views.py Handwritten by google.com/+Nkansahrexford
from django.db.models import Q
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from main.models import Item
from main.forms import ItemForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
#from django.contrib import messages # Apply use in Use
from django.views.generic import ListView
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def intro_page(request):
	"""Current introductory page in use"""
	return render(request, 'metrika.html')

@login_required
def app_home(request):
	""" App homepage. This page displays the search box """
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


def base(request):
	""" Old introductory page deprecated"""
	return render(request, 'intro.html')

class CreateImei(CreateView):
	""" Adds an object to database by a user in context"""
	template_name = 'add.html'
	form_class = ItemForm
	model = Item

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(CreateImei, self).form_valid(form)

	@method_decorator(login_required())
	def dispatch(self, * args, ** kwargs):
		return super(CreateImei, self).dispatch( * args, ** kwargs)

class UpdateImei(UpdateView):
	""" Updates an object in context """
	model = Item
	fields = fields = ['device', 'slug', 'description', 'photo', 'stolen']

	@method_decorator(login_required())
	def dispatch(self, * args, ** kwargs):
		return super(UpdateImei, self).dispatch( * args, ** kwargs)


class DeleteImei(DeleteView):
	""" Deletes the the context object """
	model = Item
	context_object_name = 'to_delete'
	success_url = reverse_lazy('myList')

	@method_decorator(login_required())
	def dispatch(self, * args, ** kwargs):
		return super(DeleteImei, self).dispatch( * args, ** kwargs)

class ListImei(ListView):
	""" Lists all the items added by a user."""
	model = Item
	def get_queryset(self):
		qset = Q(created_by=self.request.user)
		#s = Item.objects.get(created_by=self.request.user) # No idea why, but results in error
		#return Item.objects.get(created_by=self.request.user)
		return Item.objects.filter(qset).distinct().order_by('-pub_date')

	@method_decorator(login_required())
	def dispatch(self, * args, ** kwargs):
		return super(ListImei, self).dispatch( * args, ** kwargs)

@login_required
def imei_detail(request, slug):
	""" Still used to display detail of object. Should be replaced with 
	Class Based View DetailView class."""
	s = get_object_or_404(Item, slug = slug)
	return render(request, 'imei-detail.html', {'s':s})	

# Give the code below a test-drive. For preventing unauthorized
# Update of IMEI.
def post(self, request, * args, ** kwargs):
	s = get_object_or_404(Item, slug = slug)
	if not request.user == s.created_by:
		return HttpResponseForbidden()
	self.object = self.get_object()
	return super(AuthorInterest, self).post(request, * args, ** kwargs)