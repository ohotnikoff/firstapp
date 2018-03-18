# -*- coding: utf-8 -*-
from django.forms import ModelForm

class RegForm(ModelForm):
    class Meta:
        pass
        # model = Comment
        # fields = ['comment_text']