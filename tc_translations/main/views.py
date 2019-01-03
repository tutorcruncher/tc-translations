from django.views.generic import TemplateView


class QuerySetMixin:
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.model.objects.request_qs(self.request)
        return self.model.objects.none()


class BasicView(QuerySetMixin, TemplateView):
    pass


class Index(BasicView):
    template_name = 'auth.jinja'
    title = 'Dashboard'


dashboard = Index.as_view()
