from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import PESELForm
from .utils import verify_pesel_and_get_date_info, get_pesel_information


class PESELFormView(FormView):
    template_name = "task2/peselform.html"
    form_class = PESELForm
    success_url = "/pesel_result/"

    def form_valid(self, form):
        pesel = form.cleaned_data.get("pesel")
        date_info = verify_pesel_and_get_date_info(pesel)

        if date_info:
            pesel_information = get_pesel_information(pesel, date_info)
            self.request.session["pesel_info"] = pesel_information
        else:
            self.request.session["pesel_error"] = "Invalid PESEL"

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["pesel_info"] = self.request.session.get("pesel_info", None)
        context["error"] = self.request.session.get("pesel_error", None)

        if "pesel_info" in self.request.session:
            del self.request.session["pesel_info"]
        if "error" in self.request.session:
            del self.request.session["error"]

        return context


class PESELResultView(TemplateView):
    template_name = "task2/peselresult.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pesel_info"] = self.request.session.get("pesel_info", None)
        context["error"] = self.request.session.get("pesel_error", None)
        return context
