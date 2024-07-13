# shop/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Product, Feedback, FeaturedGame
from .forms import FeedbackForm

class HomeView(ListView):
    model = FeaturedGame
    template_name = 'home.html'
    context_object_name = 'featured_games'

class GamePlatformView(ListView):
    model = Product
    template_name = 'game_platform.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__name=self.kwargs['category'])

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class CreateFeedbackView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateFeedbackView(LoginRequiredMixin, UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback_form.html'

    def get_queryset(self):
        return Feedback.objects.filter(author=self.request.user)

class DeleteFeedbackView(LoginRequiredMixin, DeleteView):
    model = Feedback
    template_name = 'confirm_delete_feedback.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Feedback.objects.filter(author=self.request.user)

class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart.html'

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', [])
    cart.append(product.pk)
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', [])
    if product.pk in cart:
        cart.remove(product.pk)
    request.session['cart'] = cart
    return redirect('cart')

class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout.html'

@login_required
def process_checkout(request):
    if request.method == 'POST':
        request.session['cart'] = []
        return redirect('home')
    return redirect('checkout')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Process contact form submission here
        return redirect('home')  # Redirect after form submission
    return render(request, 'contact_us.html')
