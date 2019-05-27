from django.shortcuts import render,get_object_or_404,redirect
from .models import Phonebook
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .forms import UpdateForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
class ContactListView(ListView):
    model = Phonebook
    template_name = 'app/index.html'
    context_object_name = 'profiles'

    def get_query(self):
        query = self.request.GET.get('q')
        if query:

            return Phonebook.objects.filter(name__icontains=query) | Phonebook.objects.filter(emailaddress__icontains=query)
        else:
            return Phonebook.objects.all()

class ContactCreateView(CreateView):
    model = Phonebook
    fields = '__all__'

def add_contact(request, name_id):
    form = UpdateForm(request.POST or None,
                    request.FILES or None)

    album = get_object_or_404(Phonebook, pk=name_id)

    if form. is_valid():
        song = form.save(commit=False)


    return render(request, 'app/add_contact.html', {'form': form})


def delete_contact(request, name_id):
    name = get_object_or_404(Phonebook, pk=name_id)
    name.delete()
    return redirect('app:index')


def update_contact(request,name_id):
    name = get_object_or_404(Phonebook, pk=name_id)
    form = UpdateForm(request.FILES or None,
                      request.POST or None,
                      instance = name)
    if form.is_valid():
        form.save()
        return redirect('app:index')
    return render(request, 'app/phonebook_form.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        login(request,user)
        return redirect('app:index')
    return render(request, 'register/login.html')

def logout_user(request):
    logout(request)
    return redirect('app:index')









