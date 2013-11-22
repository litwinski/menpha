from django.db.models import Q
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from main.models import Item
from main.forms import ItemForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Add Class
class create(CreateView):
	template_name = 'add.html'
	form_class = ItemForm
	model = Item

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(create, self).form_valid(form)

# UpdateView class- -----------------------------------
class update(UpdateView):
	model = Item

# DeleteView Class----------------------------------------
class deleteItem(DeleteView):
	model = Item
	context_object_name = 'to_delete'
	success_url = reverse_lazy('myList')

# List View
class list(ListView):
	model = Item
	def get_queryset(self):
		qset = Q(created_by=self.request.user)
		#s = Item.objects.get(created_by=self.request.user)
		#return Item.objects.get(created_by=self.request.user)
		return Item.objects.filter(qset).distinct().order_by('-pub_date')


# Function Based Views. Eliminate gradually when CBV takes over.
def base(request):
	return render_to_response('version1.html')

def intro(request):
	return render(request, 'intro.html')

@login_required
def home(request):
	return render(request, 'index.html',)

@login_required
def search(request):
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
def success(request):
	return HttpResponse('success')

@login_required
def detail(request, slug):
	s = get_object_or_404(Item, slug = slug)
	return render(request, 'imei-detail.html', {'s':s})	