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

from django.views.generic.edit import CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy

# Add Class
class imeiCreate(CreateView):
	template_name = 'add.html'
	form_class = ItemForm
	model = Item

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(imeiCreate, self).form_valid(form)

# UpdateView class
class imeiUpdate(UpdateView):
	model = Item

# DeleteView Class
class imeiDelete(DeleteView):
	model = Item
	success_url = reverse_lazy('deleted')

class DetailView(generic.DetailView):
	model = Poll
	template_name = 'imei-detail.html'

def base(request):
	return render_to_response('base.html')

def intro(request):
	return render(request, 'intro.html')

@login_required
def home(request):
	return render(request, 'index.html',)

@login_required
def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = Q(imei__iexact=query, stolen__iexact='s') 
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
def detail(request, item_imei):
	s = get_object_or_404(Item, imei = item_imei)
	return render(request, 'imei-detail.html',)	


@login_required
def edit(request, item_imei):
	item = get_object_or_404(Item, imei=item_imei)
	if request.method == "POST":
		form = ItemForm(request.POST, instance = item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/detail/%s' % item_imei)
	else:
		form = ItemForm(instance=item)

	return render(request, 'edit.html', {'item':item, 'form':form})

@login_required
def edit_info(request):
	return HttpResponse('Hmmm! It looks like you wanna edit something.')

@login_required
def delete(request, item_imei):
	try:
		item = get_object_or_404(Item, imei=item_imei)
		return render(request, 'del_confirm.html', {'item':item, 'item_imei':item_imei},)
	except Item.DoesNotExist:
		return render_to_response('del_success.html')
	#return render(request, 'delete_item.html', {'item':item, 'item_imei':item_imei},)
	
@login_required
def deleted(request, item_imei):
	query = get_object_or_404(Item, imei=item_imei)
	query.delete()
	return render(request, 'del_success.html', {'query':query},)


@login_required
def myList(request):
	return render(request, 'my-list.html')

class MyListView(ListView):
	template_name = 'my-list'
	context_object_name = 'created_by'
	
	def get_queryset(self):
		"""Return the last five published polls."""
		return Item.objects.filter('created_by')
		