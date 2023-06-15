from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_en import LEXICON_EN

button_yes = KeyboardButton(text=LEXICON_EN['yes_btn'])
button_no = KeyboardButton(text=LEXICON_EN['no_btn'])

yes_no_builder = ReplyKeyboardBuilder()

yes_no_builder.row(button_yes, button_no, width=2)
yes_no_kb = yes_no_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

btn_1 = KeyboardButton(text=LEXICON_EN['pit'])
btn_2 = KeyboardButton(text=LEXICON_EN['paper'])
btn_3 = KeyboardButton(text=LEXICON_EN['scissors'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[btn_1], [btn_2], [btn_3]],
    resize_keyboard=True
)
