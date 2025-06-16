from django.shortcuts import render, redirect
from . import models, forms 
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from accounts.views import send_email
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse


# Create your views here.
class BookDetailsView(LoginRequiredMixin, DetailView):
    model = models.Book
    # pk_url_kwarg = 'pk'
    template_name = 'books/details.html'
    # in DetailView, context data of the selected object is autometically send as singular name of the model like 'book' for this case 


    def post(self, request, *args, **kwargs):
        book = self.get_object()
        review_form = forms.ReviewForm(data= self.request.POST)

        if review_form.is_valid():
            form_instance = review_form.save(commit=False)
            form_instance.user = self.request.user  
            form_instance.book = book 
            form_instance.save()
            # Redirect to the book details page
            return redirect(reverse('details', kwargs={'pk': book.id}))
        else:
            return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        reviews = book.reviews.all()
        context["form"] = forms.ReviewForm()
        context["reviews"] = reviews
        context["user_ever_borrowed"] = self.request.user.borrows.filter(book= book).exists()
        context["is_borrowed_by_current_user"] = book.is_borrowed_by_current_user(user= self.request.user)
        return context


class BorrowView(LoginRequiredMixin, View):
    def post(self, request, pk):
        user = request.user

        with transaction.atomic():
            book = models.Book.objects.select_for_update().get(pk=pk)
            profile = user.profile

            if book.is_borrowed:
                messages.warning(request, "This Book is already borrowed")
            elif book.price > profile.balance:
                messages.warning(request, "Sorry! You don't have enough Deposit balance.")
            else:
                profile.balance -= book.price
                profile.save(
                    update_fields = ['balance']
                )
                balance_after_borrow = profile.balance
                models.Borrow.objects.create(book=book, user=user, balance_after_borrow= balance_after_borrow)

                send_email(user, book.price, "Borrowed Book", 'books/borrowed_email.html')
                messages.success(request, f"You have successfully borrowed {book.title}")

        return redirect('details', pk=book.pk)