# Views.py Handwritten by google.com/+Nkansahrexford
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from main.models import Item
from main.forms import ItemForm, NotifyForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
#from django.contrib import messages # Apply later
from django.views.generic import ListView
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


def intro_page(request):
    """Current introductory page in use"""
    return render(request, 'menpha.html')


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
        'user': request.user,  # For checking permission in template
    })


class CreateImei(CreateView):
    """ Adds an object to database by a user in context"""
    template_name = 'add.html'
    form_class = ItemForm
    model = Item

    def form_valid(self, form):
        #save current user into "created_by" field in models.
        form.instance.created_by = self.request.user
        return super(CreateImei, self).form_valid(form)

    @method_decorator(login_required())
    def dispatch(self, * args, ** kwargs):
        return super(CreateImei, self).dispatch(* args, ** kwargs)


class UpdateImei(UpdateView):
    """ Updates an object in context.

    If request.user is same as created_by value in model, dispatch
    fucntion proceeds. Else PermissionDenied. Useful for preventing
    one user from editing item added by another user. """
    model = Item
    fields = ['device', 'slug', 'type_of_item', 'description', 'photo', 'stolen']
    template_name = 'item_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        pulled = Item.objects.get(slug=kwargs['slug'])
        if pulled.created_by == request.user:
            return super(UpdateImei, self).dispatch(request, *args, **kwargs)
        raise PermissionDenied

    #@method_decorator(login_required())
    #def dispatch(self, * args, ** kwargs):
    #	return super(UpdateImei, self).dispatch( * args, ** kwargs)


class DeleteImei(DeleteView):
    """ Deletes the the context object.
    If request.user is same as created_by value in model,
    dispatch fucntion proceeds. Else PermissionDenied.

    Useful for preventing one user from deleting
    item added by another user. """
    model = Item
    context_object_name = 'to_delete'
    success_url = reverse_lazy('myList')
    template_name = 'item_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        grab = Item.objects.get(slug=kwargs['slug'])
        if grab.created_by == request.user:
            return super(DeleteImei, self).dispatch(request, *args, **kwargs)
        raise PermissionDenied


class ListImei(ListView):
    """Lists all the items added by a user."""
    model = Item
    template_name = 'item_list.html'

    def get_queryset(self):
        qset = Q(created_by=self.request.user)
        return Item.objects.filter(qset).distinct().order_by('-pub_date')

    @method_decorator(login_required())
    def dispatch(self, * args, ** kwargs):
        return super(ListImei, self).dispatch(* args, ** kwargs)


@login_required
def imei_detail(request, slug):
    """ Still used to display detail of object. Should be replaced
    with Class Based View DetailView class."""
    s = get_object_or_404(Item, slug=slug)
    return render(request, 'imei-detail.html', {'mylist': s, 'user': request.user})


@login_required
def notify(request, slug):
    """ Send notification email to original owner of device who lost it """
    grab = Item.objects.get(slug=slug)
    if request.method == "POST":  # If the form has been submitted...
        form = NotifyForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = request.user.email
            cc_myself = form.cleaned_data['cc_myself']
            recipients = [grab.created_by.email]

            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/app/notify/thanks/')  # Redirect after POST
    else:
        form = NotifyForm()  # An unbound form
    return render(request, 'send-mail.html', {'form': form, })
