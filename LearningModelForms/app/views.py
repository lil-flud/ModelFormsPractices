from django.shortcuts import render
from app.forms import CustomerForm, AuthorForm, BookForm

# Create your views here.


# def home(request):
#     form = CustomerForm()
#     if request.method == "POST":
#         # print(request.POST)
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form": form}
#     return render(request, "home.html", context)


def home(request):
    form = AuthorForm()
    if request.method == "POST":
        print(request.POST)
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)
