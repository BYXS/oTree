# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range, safe_json
from .models import Constants

class Feedback(Page):

    form_model = models.Player
    form_fields = ['feedback', 'suggestion']

    def participate_condition(self):
        return True

    template_name = 'feedback/Feedback.html'

    def after_next_button(self):
        self.player.payoff = 0


def pages():
    return [Feedback]
