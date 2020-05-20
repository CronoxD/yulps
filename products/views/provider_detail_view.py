
# Django
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Models
from products.models import Provider, Score

# Forms
from products.forms import ScoreForm

# Utilities
from django.db import IntegrityError


class ProviderDetailView(DetailView):
    model = Provider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['score_form'] = ScoreForm()
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        score_form = ScoreForm(request.POST)
        if score_form.is_valid():
            try:
                score_form.instance.user = request.user
                score_form.instance.provider = self.object
                score_form.save()
            except IntegrityError:
                score = Score.objects.get(
                    user=request.user,
                    provider=self.object
                )
                score_form.instance.id = score.id
                score_form.save()
        else:
            context = self.get_context_data(object=self.object)
            context['score_form'] = score_form
            return self.render_to_response(context)
        return self.get(request, args, kwargs)