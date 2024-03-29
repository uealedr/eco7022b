import random

from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'holtlaury'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    LOTTERY_PAYOFFS = {
        "A": [Currency("2.00"), Currency("1.60")],
        "B": [Currency("3.85"), Currency("0.10")]
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    @staticmethod
    def _make_choice_field(label: str):
        return models.StringField(
            choices=["A", "B"],
            label=label,
            widget=widgets.RadioSelectHorizontal
        )

    choice1 = _make_choice_field("1-in-10")
    choice2 = _make_choice_field("2-in-10")
    choice3 = _make_choice_field("3-in-10")
    choice4 = _make_choice_field("4-in-10")
    choice5 = _make_choice_field("5-in-10")
    choice6 = _make_choice_field("6-in-10")
    choice7 = _make_choice_field("7-in-10")
    choice8 = _make_choice_field("8-in-10")
    choice9 = _make_choice_field("9-in-10")
    choice10 = _make_choice_field("10-in-10")
    paid_choice = models.StringField()
    die_roll = models.IntegerField()

    def choice_fields(self):
        return ['choice1', 'choice2', 'choice3', 'choice4', 'choice5',
                'choice6', 'choice7', 'choice8', 'choice9', 'choice10']

    def determine_outcome(self):
        self.die_roll = random.randint(0, 9)
        self.paid_choice = random.choice(self.choice_fields())
        chosen_lottery = getattr(self, self.paid_choice)
        target_roll = int(self.paid_choice.replace("choice", ""))
        if self.die_roll < target_roll:
            self.payoff = C.LOTTERY_PAYOFFS[chosen_lottery][0]
        else:
            self.payoff = C.LOTTERY_PAYOFFS[chosen_lottery][1]


# PAGES
class DecisionPage(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return player.choice_fields()

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.determine_outcome()


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    DecisionPage,
    ResultsWaitPage,
    Results
]
