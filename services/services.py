import random

from lexicon.lexicon_en import LEXICON_EN


def get_bot_choice() -> str:
    return random.choice(['pit', 'scissors', 'paper'])


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {'pit': 'scissors',
             'scissors': 'paper',
             'paper': 'pit'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'


def _normalize_user_answer(user_choice: str) -> str:
    for key in LEXICON_EN:
        if LEXICON_EN[key] == user_choice:
            return key
    raise Exception
