from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

# keybord 1

joy=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Радио для релакса', url='https://radiopotok.ru/RelaxTime33')],
    [InlineKeyboardButton(text='Интересные факты о животных', url='https://pikabu.ru/story/100_interesnyikh_faktov_o_zhivotnyikh_7406889')],
    [InlineKeyboardButton(text='Анекдоты', url='https://kartaslov.ru/книги/500_самых_свежих_анекдотов/1')],
    [InlineKeyboardButton(text='Красивые пейзажи', url='https://cameralabs.org/6752-50-krasivykh-pejzazhnykh-fotografij-so-vsej-zemli')],
    ])

# keyboard 2

horoscope=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Телец', callback_data='zodiac')],
    [InlineKeyboardButton(text='Близнецы', callback_data='zodiac')], 
    [InlineKeyboardButton(text='Рак', callback_data='zodiac')],
    [InlineKeyboardButton(text='Лев', callback_data='zodiac')],
    [InlineKeyboardButton(text='Дева', callback_data='zodiac')], 
    [InlineKeyboardButton(text='Весы', callback_data='zodiac')],
    [InlineKeyboardButton(text='Скорпион', callback_data='zodiac')],
    [InlineKeyboardButton(text='Овен', callback_data='zodiac')], 
    [InlineKeyboardButton(text='Контакты', callback_data='zodiac')],
    [InlineKeyboardButton(text='Козерог', callback_data='zodiac')],
    [InlineKeyboardButton(text='Водолей', callback_data='zodiac')], 
    [InlineKeyboardButton(text='Рыбы', callback_data='zodiac')]
    ])

# keyboard 3

media=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Клип', url='https://www.youtube.com/watch?v=vx2u5uUu3DE')]
    ])

