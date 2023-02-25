from django.forms import ModelForm
from app.models import Customer, Author, Book

# Create the form class.


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "title", "birth_date"]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "authors"]
