from django.utils import timezone as tz
from django.shortcuts import render, redirect
from .models import User, Profile
from books.models import Borrow
from django.views.generic import View, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserLoginForm, DepositForm
from django.contrib.auth import login
from django.db import transaction
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse_lazy


def send_email(user, amount, subject, message_template):
    message = render_to_string(message_template, context={
        'user' : user, 
        'amount' : amount,
    })
    email = EmailMultiAlternatives(subject, to=[user.email])
    email.attach_alternative(message, "text/html")
    email.send()


# Create your views here.
class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('profile')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'files': self.request.FILES
        })
        return kwargs

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        messages.success(self.request, f"{user.username} Registered Successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        form = context['form']
        context["title"] = "Registration Form"
        context['account_fields'] = [
            form['username'], form['first_name'], form['last_name'], 
            form['email'], form['password1'], form['password2']
        ]
        context['personal_fields'] = [
            form['profile_picture'], form['birth_date'], form['gender']
        ]
        context['address_fields'] = [
            form['street_address'], form['city'], form['postal_code']
        ]
        return context
    
    

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "Login Form"
        return context
    

class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user

        # here .select_related('book') avoids extra DB hits when accessing borrow.book.title in the template
        borrow_history = user.borrows.select_related('book').order_by('-borrow_date')

        return render(request, 'accounts/profile.html', context= {'borrow_history' : borrow_history})
    

class ReturnBookView(LoginRequiredMixin, View):
    def post(self, request, pk):

        try:
            with transaction.atomic():

                # Lock the profile row to prevent race conditions
                borrow_instance = Borrow.objects.select_related('book').select_for_update().get(pk= pk, user= request.user, return_date__isnull= True)
                user = request.user
                profile = Profile.objects.select_for_update().get(user=user)
                
                profile.balance += borrow_instance.book.price
                profile.save(
                    update_fields= ['balance']
                )

                borrow_instance.return_date = tz.now()
                borrow_instance.balance_after_return = profile.balance 
                borrow_instance.save(
                    update_fields= ['return_date', 'balance_after_return',]
                )

                send_email(user, borrow_instance.book.price, "Book Returned and Refunded", 'accounts/return_book_email.html')
                messages.success(request, f"{borrow_instance.book.title} has been returned and refunded Borrow Price successfully.")

        except Borrow.DoesNotExist:
            messages.warning(request, "No active borrow record found.")

        return redirect('profile')

    

class DepositView(LoginRequiredMixin, FormView):
    form_class = DepositForm
    template_name = 'accounts/deposit.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = self.request.user
        amount = form.cleaned_data.get('amount')

        with transaction.atomic():
            # Lock the profile row to prevent race conditions
            profile = Profile.objects.select_for_update().get(user=user)

            profile.balance += amount
            profile.save(
                update_fields = ['balance']
            )

            messages.success(
                self.request,
                f'{"{:,.2f}".format(float(amount))}৳ was deposited to your account successfully'
            )

            send_email(user, amount, "Deposit Message", 'accounts/deposit_email.html')

        return super().form_valid(form)
    
