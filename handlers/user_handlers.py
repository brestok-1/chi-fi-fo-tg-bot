from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_en import LEXICON_EN
from services.services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_EN['start'], reply_markup=yes_no_kb)


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_EN['help'], reply_markup=yes_no_kb)


@router.message(Text(text=LEXICON_EN['yes_btn']))
async def process_positive_answer(message: Message):
    await message.answer(text=LEXICON_EN['yes'], reply_markup=game_kb)


@router.message(Text(text=LEXICON_EN['no_btn']))
async def process_negative_answer(message: Message):
    await message.answer(text=LEXICON_EN['no'])


@router.message(Text(text=[LEXICON_EN['paper'], LEXICON_EN['scissors'], LEXICON_EN['pit']]))
async def process_game_btn(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f"{LEXICON_EN['bot_choice']} {LEXICON_EN[bot_choice]}")
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_EN[winner], reply_markup=yes_no_kb)
