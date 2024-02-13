from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView
from django_gems.user_profile.forms import AccountProfileForm
from django_gems.common.mixins import NavigationBarMixin
from django_gems.user_profile.models import AccountProfile

UserModel = get_user_model()

class UserUpdateView(NavigationBarMixin, UpdateView):
    template_name = 'user-profile/update-profile.html'
    model = AccountProfile
    form_class = AccountProfileForm

    def get_success_url(self):
        return reverse_lazy('details_changed', kwargs={
            'pk': self.request.user.pk,
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nav_bar_context = self.get_nav_bar_context()
        context.update(nav_bar_context)
        context['form'] = self.get_form()
        return context


class UserDeleteView(DeleteView):
    template_name = 'user-profile/delete-profile.html'
    model = UserModel
    success_url = reverse_lazy('profile-deleted')

