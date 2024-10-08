from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import UploadFileForm

import random


class UploadFileFormView(FormView):
    template_name = "task1/fileupload.html"
    form_class = UploadFileForm
    success_url = ""

    def form_valid(self, form):
        file = self.request.FILES["file"]
        if not file.name.endswith(".txt"):
            form.add_error("file", "Only .txt files are allowed.")
            return self.form_invalid(form)
        text = scramble_text(file)

        return render(self.request, "task1/result.html", {"scrambled_text": text})

    # def form_invalid(self, form):
    #     return super().form_invalid(form)


def scramble_text(file):
    text = file.read().decode("utf-8")
    words = text.split()

    def shuffle_word(word):
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            return word[0] + "".join(middle) + word[-1]
        return word

    scrambled_words = [shuffle_word(word) for word in words]
    return " ".join(scrambled_words)
