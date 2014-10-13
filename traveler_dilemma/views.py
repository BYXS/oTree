# -*- coding: utf-8 -*-
from __future__ import division
import traveler_dilemma.models as models
from traveler_dilemma._builtin import Page, WaitPage


def variables_for_all_templates(self):
    return dict(total_q=1, instructions='traveler_dilemma/Instructions.html')


class Introduction(Page):

    template_name = 'global/Introduction.html'

    def variables_for_template(self):
        return {'max_amount': self.subsession.max_amount,
                'min_amount': self.subsession.min_amount,
                'reward': self.subsession.reward,
                'penalty': self.subsession.penalty}


class Question1(Page):
    template_name = 'global/Question.html'
    form_model = models.Player
    form_fields = 'training_answer_mine', 'training_answer_others'
    question = '''Suppose that you claim the antiques are worth 50 points
        and the other traveler claims they are worth 100 points.
        What would you and the other traveler receive in compensation from
        the airline?'''

    def participate_condition(self):
        return self.subsession.round_number == 1

    def variables_for_template(self):
        return dict(num_q=1, question=self.question)


class Feedback1(Page):
    template_name = 'traveler_dilemma/Feedback.html'

    def participate_condition(self):
        return self.subsession.round_number == 1

    def variables_for_template(self):
        return dict(
            num_q=1, mine=self.player.training_answer_mine,
            others=self.player.training_answer_others)


class Claim(Page):

    template_name = 'traveler_dilemma/Claim.html'

    form_model = models.Player
    form_fields = ['claim']


class ResultsWaitPage(WaitPage):

    scope = models.Group

    def after_all_players_arrive(self):
        for p in self.group.players:
            p.set_payoff()


class Results(Page):

    template_name = 'global/ResultsTable.html'

    def variables_for_template(self):
        other = self.player.other_player().claim
        if self.player.claim < other:
            reward = self.subsession.reward
        elif self.player.claim > other:
            reward = -self.subsession.penalty
        else:
            reward = 0
        return dict(
            table=[
                ('', 'Points'),
                ('You claimed', self.player.claim),
                ('The other traveler claimed',
                 self.player.other_player().claim),
                ('Amount paid to both',
                 int(self.player.payoff - self.player.BONUS - reward)),
                ('Your reward/penalty', reward and '%+i' % reward),
                ('Thus you receive',
                 int(self.player.payoff - self.player.BONUS)),
                ('In addition you get a participation fee of',
                 self.player.BONUS),
                ('So in sum you will get', int(self.player.payoff)),
                ])


class Question2(Page):
    template_name = 'global/Question.html'
    form_model = models.Player
    form_fields = 'feedback',

    def participate_condition(self):
        return self.subsession.round_number == 1

    def variables_for_template(self):
        return dict(
            num_q=1,
            title='Questionnaire',
            hide_instructions=True,
            question='How well do you think this sample game was implemented?')


def pages():

    return [Introduction,
            Question1,
            Feedback1,
            Claim,
            ResultsWaitPage,
            Results,
            Question2]
