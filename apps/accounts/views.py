from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from .models import Profile
from .auth_helpers import authenticate_user, is_staff_account, login_account


def register(request):
    if request.user.is_authenticated:
        if is_staff_account(request.user):
            return redirect('dashboard:index')
        return redirect('store:home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        phone = request.POST.get('phone', '').strip()

        errors = []
        if not username:
            errors.append('L\'identifiant est obligatoire.')
        if not email:
            errors.append('L\'email est obligatoire.')
        if password1 != password2:
            errors.append('Les mots de passe ne correspondent pas.')
        if User.objects.filter(username__iexact=username).exists():
            errors.append('Ce nom d\'utilisateur est déjà pris.')
        if User.objects.filter(email__iexact=email).exists():
            errors.append('Cet email est déjà utilisé.')

        if not errors:
            try:
                validate_password(password1, user=User(username=username, email=email))
            except ValidationError as exc:
                errors.extend(exc.messages)

        if errors:
            for err in errors:
                messages.error(request, err)
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name,
            )
            user.is_staff = False
            user.is_superuser = False
            user.save(update_fields=['is_staff', 'is_superuser'])

            profile, _ = Profile.objects.get_or_create(user=user)
            profile.phone = phone
            profile.save()

            login_account(request, user)
            messages.success(request, f'Bienvenue {first_name or username} ! Votre compte client a été créé.')
            return redirect('store:home')

    return render(request, 'accounts/auth.html', {'initial_form': 'sign-up'})


def login_view(request):
    if request.user.is_authenticated:
        if is_staff_account(request.user):
            return redirect('dashboard:index')
        return redirect('store:home')

    if request.method == 'POST':
        identifier = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate_user(identifier, password, request)

        if user is None:
            messages.error(request, 'Identifiants incorrects.')
        elif user.is_staff or user.is_superuser:
            messages.error(
                request,
                'Les comptes administrateur ne se connectent pas ici. '
                'Utilisez le panneau de gestion : /dashboard/connexion/'
            )
        elif not user.is_active:
            messages.error(request, 'Ce compte est désactivé. Contactez le support.')
        else:
            login_account(request, user)
            messages.success(request, f'Bienvenue {user.first_name or user.username} !')
            next_url = request.GET.get('next', '/')
            if next_url.startswith('/dashboard') or next_url.startswith('/admin'):
                next_url = '/'
            return redirect(next_url)

    return render(request, 'accounts/auth.html', {'initial_form': 'sign-in'})


def logout_view(request):
    was_staff = is_staff_account(request.user)
    logout(request)
    messages.info(request, 'Vous avez été déconnecté.')
    if was_staff:
        return redirect('dashboard:login')
    return redirect('store:home')


@login_required
def profile(request):
    if is_staff_account(request.user):
        messages.info(request, 'Les administrateurs utilisent le panneau de gestion.')
        return redirect('dashboard:index')

    profile_obj, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', user.email)
        user.save()

        profile_obj.phone = request.POST.get('phone', '')
        profile_obj.address = request.POST.get('address', '')
        profile_obj.city = request.POST.get('city', '')
        if 'avatar' in request.FILES:
            profile_obj.avatar = request.FILES['avatar']
        profile_obj.save()
        messages.success(request, 'Profil mis à jour.')
        return redirect('accounts:profile')

    from apps.orders.models import Order
    from apps.store.models import Wishlist

    orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]
    wishlist = Wishlist.objects.filter(user=request.user).select_related('product')[:4]

    return render(request, 'accounts/profile.html', {
        'profile': profile_obj,
        'orders': orders,
        'wishlist': wishlist,
        'page': 'compte',
    })
