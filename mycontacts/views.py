from django.shortcuts import render, get_object_or_404
from .forms import AddForm
from .models import Contact
from django.http import HttpResponseRedirect

def show(request):
    """ 
    This function gets all the members in your Database through your Model
    Any further usage please refer to: https://docs.djangoproject.com/el/1.10/ref/models/querysets/
    """
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html',{'contacts': contact_list})
    
def add(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            # new_member_picture = django_form.data.get('picture')
            new_member_name     = django_form.data.get('name')
            new_member_relation = django_form.data.get('relation')
            new_member_phone    = django_form.data.get('phone')
            new_member_email    = django_form.data.get('email')
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.create(
                name     = new_member_name,
                relation = new_member_relation,
                phone    = new_member_phone,
                email    = new_member_email,
                )
                 
            contact_list = Contact.objects.all()
            return HttpResponseRedirect("/")     
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return render(request, 'mycontacts/add.html')
    else:
        return render(request, 'mycontacts/add.html')


def read(request, detail_id):

    data = get_object_or_404(Contact, pk=detail_id)

    return render(request, "mycontacts/view.html", {"data":data})

def edit(request, detail_id):

    data = get_object_or_404(Contact, pk=detail_id)

    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
        
            edit_member_name     = django_form.data.get("name")
            edit_member_relation = django_form.data.get("relation")
            edit_member_phone    = django_form.data.get('phone')
            edit_member_email    = django_form.data.get('email')
        
           
            data.name     = edit_member_name
            data.relation = edit_member_relation
            data.phone    = edit_member_phone
            data.email    = edit_member_email               
            data.save()

            contact_list = Contact.objects.all()
            return HttpResponseRedirect("/")
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return render(request, "mycontacts/edit.html", {"data":data})
    else:
        return render(request, "mycontacts/edit.html", {"data":data})

def delete(request, detail_id):
    contact = Contact.objects.get(pk=detail_id).delete()

    return HttpResponseRedirect('/')

    