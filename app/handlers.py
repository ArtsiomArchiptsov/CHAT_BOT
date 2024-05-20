from aiogram import  F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message,CallbackQuery

from app.API import get_dogs

import app.keyboards as kb 
import random
import time

from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext


router=Router()

class Reg(StatesGroup):
    guess=State()
   

# Функция, которая начинает работать, если ввести команду /start
@router.message(CommandStart()) 
async def cmd_start(message:Message): 
    await message.reply(f'Привет, {message.from_user.first_name}!\
                        \nЯ чат-бот Marina! Я рада Вас видеть в моем чате.\
                        \nЯ постараюсь сделать, чтобы время, которое Вы проведете\
                        \nздесь не было потрачено зря.\
                        \nКстати, если введешь команду /info я расскажу тебе,\
                        \nчто я умею. ')   
    
@router.message(Command('relax'))
async def get_info(message:Message):
    await message.answer('Минутка релакса', reply_markup=kb.joy) 

# Функция выводит случайную картинку собак

@router.message(Command('dog'))
@router.message(F.text.lower() == 'хочу собачку')
async def info(message: types.Message):
    img_dogs = get_dogs()
    await message.answer('Вуф-вуф-вуф...')
    await message.answer_photo(img_dogs)

# Функция выводит картинку по URL

@router.message(Command('photo'))
async def get_photo(message:Message):
    await message.answer_photo(photo='https://yandex.by/images/search?img_url=https%3A%2F%2Fcs4.pikabu.ru%2Fpost_img%2Fbig%2F2015%2F08%2F27%2F11%2F1440700178_876074300.jpg&lr=157&pos=15&rpt=simage&source=serp&stype=image&text=красивые%20фото', 
                               caption="Очень красивый закат!")

# Функция выводит случайную шутку

@router.message(Command('joke'))
async def get_joke(message:Message):
    joke=[
        "Жизнь — как рояль: клавиша белая, клавиша черная… крышка.",
        "Моя собака знает много команд. И что самое главное, я уже научился выполнять некоторые из них...",
        "Говорят, в барах закончилось пиво в связи с иностранными туристами... Да у меня каждое утро такая проблема в холодильнике",
        "Я человек простой - увидел таракана, собрал вещи, переехал.",
        "Люблю вести ночной образ жизни. Особенно поспать.",
        "Есть три вещи, на которые страшно смотреть с утра после пьянки: лицо, кошелек и СПИСОК ИСХОДЯЩИХ ВЫЗОВОВ.",
        "В наше время самое надежное противозачаточное средство — компьютер, который практически исключает не только возможность нежелательной беременности, но и саму возможность половых контактов."
    ]

    rand_joke=random.choice(joke)
    await message.answer('Сегодняшняя шутка дня!')
    time.sleep(2)
    await message.answer(rand_joke)

# Функция выводит гороскоп

@router.message(Command('horoscope'))
async def get_photo(message:Message):
    await message.answer('Выберите ваш знак зодиака', reply_markup=kb.horoscope)

@router.callback_query(F.data=='zodiac')
async def catalog(callback:CallbackQuery):
    first = ["Сегодня — идеальный день для новых начинаний.",
                 "Оптимальный день для того, чтобы решиться на смелый поступок!",
                 "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
                 "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
                 "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

    second = ["Но помните, что даже в этом случае нужно не забывать про",
                  "Если поедете за город, заранее подумайте про",
                  "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
                  "Если у вас упадок сил, обратите внимание на",
                  "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

    second_add = ["отношения с друзьями и близкими.",
                      "работу и деловые вопросы, которые могут так некстати помешать планам.",
                      "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
                      "бытовые вопросы — особенно те, которые вы не доделали вчера.",
                      "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

    third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
                 "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
                 "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
                 "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
                 "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


    rand_horoscope = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)

    await callback.answer('Сегодня ваш гороскоп',show_alert=True) 
    time.sleep(2)
    await callback.message.edit_text(rand_horoscope, reply_markup=kb.horoscope)        
                    
# функция генерирует случайную картинку

@router.message(Command('image'))
async def get_photo(message:Message):
    joke=[
        "https://yandex.by/images/search?img_url=https%3A%2F%2Fscontent-hel3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2F53340364_415763742568738_5440831766156617910_n.jpg%3Fstp%3Ddst-jpg_e35%26_nc_ht%3Dscontent-hel3-1.cdninstagram.com%26_nc_cat%3D110%26_nc_ohc%3D89zqvLFAzLsAX9akfej%26edm%3DAABBvjUBAAAA%26ccb%3D7-4%26oh%3D00_AT8osJciHq5poXRXHUhk3JQxYnsxKSJPinCIpPTRTqdT9w%26oe%3D62182E59%26_nc_sid%3D83d603&lr=157&pos=5&rpt=simage&source=serp&text=красивые%20картинки",
        "https://yandex.by/images/search?img_url=https%3A%2F%2Fcrosti.ru%2Fpatterns%2F00%2F24%2F05%2F73_preview_5798ff62.jpg&lr=157&pos=10&rpt=simage&source=serp&text=красивые%20картинки",
        "https://yandex.by/images/search?img_url=https%3A%2F%2Fimg.goodfon.com%2Foriginal%2F4500x2971%2Fc%2F1b%2Fozero-gory-les-zakat-derevya.jpg&lr=157&pos=11&rpt=simage&source=serp&text=красивые%20картинки",
        "https://yandex.by/images/search?img_url=https%3A%2F%2Fs.poembook.ru%2Ftheme%2Fad%2Faf%2Fd3%2F4e09b59eb49fd5e8788db55bc926147105c49722.jpeg&lr=157&pos=12&rpt=simage&source=serp&text=красивые%20картинки",
        "https://yandex.by/images/search?img_url=https%3A%2F%2Fscontent-hel3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2Fe15%2F264489450_131153002661600_1358306770161013387_n.jpg%3F_nc_ht%3Dscontent-hel3-1.cdninstagram.com%26_nc_cat%3D108%26_nc_ohc%3DGCBv_OqPVyEAX8qFpVC%26edm%3DAABBvjUBAAAA%26ccb%3D7-4%26oh%3D00_AT80BN4uylXBrdLNgmxdnLUm1BATx8BNxpAbAU67qxtEHA%26oe%3D61E3D2BB%26_nc_sid%3D83d603&lr=157&pos=13&rpt=simage&source=serp&text=красивые%20картинки",
        "https://yandex.by/images/search?img_url=https%3A%2F%2Fs1.1zoom.ru%2Fbig3%2F76%2F356720-admin.jpg&lr=157&pos=16&rpt=simage&source=serp&text=красивые%20картинки",
       
    ]

    rand_joke=random.choice(joke)
    await message.answer('Сегодняшняя картинка!')
    time.sleep(2)
    await message.answer_photo(photo=rand_joke)


    
# функция, которая предоставляет краткую информацию о чат-боте. если ввести команду /info

@router.message(Command('info'))
async def get_info(message:Message):
    await message.answer('\"КРАТКОЕ ОПИСАНИЕ ФУНКЦИОНАЛА БОТА\"\
                         \nДанный бот, является учебным. Он должен показать,\
                         \nпо крайней мере, весь тот объем материала, который\
                         \nбыл изучен.\
                         \nДанный бот может\
                         \n- гененрировать гороскоп,\
                         \n- генерировать шутки,\
                         \n- выводить рандомную картинку,\
                         \n- может вывести обычную картинку\
                         \n- отправить на какой-либо сайт по ссылке,\
                         \n- провести краткий диалог между пользователем и ботом,\
                         \n- а также краткая цепочка сообщений с последующим выводом данных на экран.\
                         \nПривводе команды /relax, будет выведено диалоговое окно\
                         \n с название \"Минутка релакса\", в котором будет набор\
                         \nкнопок с ссылками для дальнейшего перехода по ним.\
                         \nЕсли с клавиатуры ввести \'хочу собачку\' или ввести команду /dog,\
                         \nбот выведит рандомную картинку собаки\
                         \nТакже бот может вывести картинку. Если ввести команду /photo, бот выведет картинку заката.\
                         \nПри  вводе команды /joke бот выведит рандомную шутку\
                         \nПри вводе команды /horoscope бот выводит гороскоп.\
                         \nПри вводе команды /image выводится случайная картинка\
                         \nЕще бот способен вести коротенький диалог. Чтобы начать даилог,\
                         \nс клавиатуры в кконсоли нужно ввести следующие команды:\
                         \n- привет,\
                         \n- как тебя зовут,\
                         \n- как дела,\
                         \n- хочу песенку,\
                         \n- что ты умеешь,\
                         \n- пока.') 
 
# Диалог с ботом

@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply(f'Привет, {message.from_user.first_name}! Я рада тебя видеть')
    elif 'как тебя зовут'  in message.text.lower():
        await message.reply('Я - Marina!')
    elif 'как дела'  in message.text.lower():
        await message.reply('У меня все отлично и я рада что ты зашел ко мне в гости!')
    elif 'хочу песенку'  in message.text.lower():
        await message.reply('Слушай с удовольствием!', reply_markup=kb.media)
    elif 'что ты умеешь'  in message.text.lower():
        await message.reply('Я могу немногое, ноя учусь. Если ты введешь /info\
                            \nто увидишь мои возможности.')
    elif 'пока'  in message.text.lower():
        await message.reply('До встречи! Когда ты в следующий раз придешь, я буду еще лучше, круче и умнее.')
    else:
        await message.reply('Я думаю, ты хотел что-то другое сделать.')