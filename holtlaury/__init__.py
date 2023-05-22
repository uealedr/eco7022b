from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'holtlaury'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice1 = models.StringField(
        choices=["A", "B"]
    )
    choice2 = models.StringField(
        choices=["A", "B"]
    )
    paid_choice = models.StringField()
    die_roll = models.IntegerField()


# PAGES
class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['choice1', 'choice2']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    DecisionPage,
    ResultsWaitPage,
    Results
]
