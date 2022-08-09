from aiogram import Dispatcher, executor, Bot, types
import config
import parsing_data
import SQLighter
import random
import text
bot = Bot(token=config.configuration['bot_token'])
dp = Dispatcher(bot)
p2 = parsing_data.ParserMovie()
@dp.message_handler(commands=['start'])
async def get_start(message: types.Message):
    SQLighter.s1.create_table('identificator')
    SQLighter.s1.add_info(message.from_user.id)  
    await bot.send_message(message.chat.id, config.configuration['get_start'], reply_markup=config.start_reply, disable_web_page_preview=True)
@dp.callback_query_handler(text='movie')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id,reply_markup=config.movie_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
p1 = parsing_data.ParserMovie()
@dp.callback_query_handler(text='movie_best')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_best.html'), reply_markup=config.markup_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_2021')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_data_movies1('moviehtmls/movie_2021.html'), reply_markup=config.movie_go_back_2step_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_2022')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_data_movies1('moviehtmls/movie_2022.html'), reply_markup=config.movie_go_back_2step_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_2023')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_data_movies1('moviehtmls/movie_2023.html'), reply_markup=config.movie_go_back_2step_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_genres_3steback')
async def next_keyboard(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.movie_genres_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_erotic')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_adult.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_action')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_action.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_sport')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_sport.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_adventure')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_adventure.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_animation')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_animation.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_comedy')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_comedy.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_documental')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_documental.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_drama')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_drama.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_fantasy')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_fantasy.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_horror')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_horror.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_mystery')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_mystery.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_romance')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_romance.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_short')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_short.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_sport')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_sport.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_thriller')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_thriller.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_war')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_war.html'), reply_markup=config.movie_genres_3steback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_erotic')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_adult.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_crime')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_crime.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_2022')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=text.serial_years['2'],reply_markup=config.serial_go_back_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_2021')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=text.serial_years['1'],reply_markup=config.serial_go_back_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
random_50 = ['moviehtmls/movie_50_1.html','moviehtmls/movie_50_2.html','moviehtmls/movie_50_3.html']
@dp.callback_query_handler(text='movie_50')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_50_best_movies(random.choice(random_50)), reply_markup=config.movie_go_back_2step_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_genres_goback')
async def next_keyboard(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.serial_genres_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_sitcom')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_sitcom.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_medical')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_medical.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_police')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_police.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_action')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_action.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_sport')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_sport.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_adventure')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_adventure.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_animation')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_animation.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_comedy')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_comedy.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_documental')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_documentary.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_drama')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_drama.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_fantasy')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_fantasy.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_horror')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_horror.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_mystery')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_mystery.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_romance')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_romance.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_short')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_short.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_sport')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_sport.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_thriller')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_thriller.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_war')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_war.html'), reply_markup=config.serial_goback_genres, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_2021')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=text.anime_2021_years['1'], reply_markup=config.anime_data_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_2022')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=text.anime_2021_years['2'], reply_markup=config.anime_data_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_2023')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=text.anime_2021_years['3'], reply_markup=config.anime_data_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_data_go_back')
async def next_keyboard(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.anime_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_genres_2stepback')
async def next_keyboard(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:',reply_markup=config.anime_genres_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_science_fiction')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_13.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_drama')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_1.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_horror')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_12.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_comedy')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_5.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_magic')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_7.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_adventure')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_8.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_daily')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_6.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_psihology')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_11.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_romance')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_2.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_secret')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_10.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_supernatural')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_4.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_thriller')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_14.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_fantasy')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_9.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_erotic')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_anime('animehtmls/anime_16.html'), reply_markup=config.anime_genres_2stepback, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)

@dp.callback_query_handler(text='go_back_1_step')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.category_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='anime_genres')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.anime_genres_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='movie_genres')
async def next_keyboard(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.movie_genres_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_genres')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.serial_genres_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='anime_go_back_button_2_step')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.anime_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='movie_go_back_button_2_step')
async def next_keyboard(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.movie_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_go_back_button_2_step')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.serial_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='video_games_go_back_button_2_step')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.video_games_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='serial')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id,reply_markup=config.serial_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='anime')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id,reply_markup=config.anime_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='video_games')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id,reply_markup=config.video_games_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='video_games_platforms')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.video_games_platforms_inline_1_page)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='movie_go_3_step')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.movie_inline)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='left_side_vdgms2')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.video_games_platforms_inline_1_page)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='right_side_vdgms1')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.video_games_platforms_inline_2_page)
@dp.callback_query_handler(text='left_side_vdgms1')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.video_games_platforms_inline_2_page)
@dp.callback_query_handler(text='right_side_vdgms2')
async def next_keyboard(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.message.chat.id,message.message.message_id, reply_markup=config.video_games_platforms_inline_1_page)
    await bot.answer_callback_query(callback_query_id=message.id)
@dp.callback_query_handler(text='movie_best_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_best_2.html'), reply_markup=config.markup_best2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_best_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_best_2.html'), reply_markup=config.markup_best2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_best_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_best.html'), reply_markup=config.markup_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_best_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_best_movie('moviehtmls/movie_best.html'), reply_markup=config.markup_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_goback')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.video_games_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_best')
async def movie_best(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_best.html'), reply_markup=config.video_games_goback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_ozh')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/games_ozh.html'), reply_markup=config.video_games_goback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_go_back_platforms')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.video_games_platforms_inline_1_page)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_go_back')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.video_games_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_go_back_platforms2')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.video_games_platforms_inline_2_page)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_play_station_5')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_65.html'), reply_markup=config.video_games_platform_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_play_station_4')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_55.html'), reply_markup=config.video_games_platform_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_play_station_3')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_5.html'), reply_markup=config.video_games_platform_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_play_station_2')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_4.html'), reply_markup=config.video_games_platform_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_play_station')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_3.html'), reply_markup=config.video_games_platform_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_xbox')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_7.html'), reply_markup=config.video_games_platform_go_back2, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_xbox_one')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_56.html'), reply_markup=config.video_games_platform_go_back2, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_xbox_360')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_8.html'), reply_markup=config.video_games_platform_go_back2, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_xbox_xs')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_66.html'), reply_markup=config.video_games_platform_go_back2, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_browser')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_61.html'), reply_markup=config.video_games_platform_go_back2, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_linux')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_59.html'), reply_markup=config.video_games_platform_go_back2, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_nintendo_switch')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_60.html'), reply_markup=config.video_games_platform_go_back2, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_nintendo_64')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_13.html'), reply_markup=config.video_games_platform_go_back, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_pc')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.games_pc_markup)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc_go_back')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.video_games_platforms_inline_1_page)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc_2stepback')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.games_pc_markup)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc1page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_1.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc2page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_2.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc3page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_3.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc4page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_4.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc5page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_5.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc6page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_6.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc7page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_7.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc8page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_8.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc9page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_9.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_pc10page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_pc_10.html'), reply_markup=config.games_pc_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_android')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.games_android_markup)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_android_2stepback')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.games_android_markup)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_andr1page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_22.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_andr2page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_android_2.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_andr3page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_android_3.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_andr4page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_android_4.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_andr5page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_android_5.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_andr6page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_android_6.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_andr7page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_android_7.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_andr8page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_android_8.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_ios')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.games_ios_markup)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios_2stepback')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.games_ios_markup)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios1page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_57.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios2page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_2.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios3page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_3.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios4page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_4.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios5page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_5.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios6page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_6.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios7page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_7.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios8page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_8.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios9page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_9.html'), reply_markup=config.games_ios_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_ios10page')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_ios_10.html'), reply_markup=config.games_android_2stepback_markup, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_popular')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_popular_1'], reply_markup=config.markup_popular_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_go_back')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.movie_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_popular_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_popular_2'], reply_markup=config.markup_popular2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_popular_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_popular_3'], reply_markup=config.markup_popular3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_popular_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_popular_3'], reply_markup=config.markup_popular3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_popular_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_popular_1'], reply_markup=config.markup_popular_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_popular_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_popular_1'], reply_markup=config.markup_popular_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_popular_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_popular_2'], reply_markup=config.markup_popular2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)

@dp.callback_query_handler(text='movie_ozhydaemye')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_ozh_1'], reply_markup=config.markup_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_o_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_ozh_2'], reply_markup=config.markup_o2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_o_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_ozh_3'], reply_markup=config.markup_o3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_o_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_ozh_3'], reply_markup=config.markup_o3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_o_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_ozh_1'], reply_markup=config.markup_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_o_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_ozh_1'], reply_markup=config.markup_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='movie_o_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.movie['movie_ozh_2'], reply_markup=config.markup_o2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)


@dp.callback_query_handler(text='serial_go_back')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.serial_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_go_back')
async def games(call: types.CallbackQuery):
    await call.message.edit_text(text='📌Выберите необходимую категорию:', reply_markup=config.anime_inline)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_best')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_best_1.html'), reply_markup=config.serial_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_best_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_best_2.html'), reply_markup=config.serial_best2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_best_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_best_3.html'), reply_markup=config.serial_best3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_best_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_best_3.html'), reply_markup=config.serial_best3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_best_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_best_1.html'), reply_markup=config.serial_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_best_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_best_1.html'), reply_markup=config.serial_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_best_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_best_2.html'), reply_markup=config.serial_best2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)

@dp.callback_query_handler(text='serial_ozhydaemye')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_o_1.html'), reply_markup=config.serial_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_o_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_o_2.html'), reply_markup=config.serial_o2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_o_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_o_3.html'), reply_markup=config.serial_o3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_o_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_o_3.html'), reply_markup=config.serial_o3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_o_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_o_1.html'), reply_markup=config.serial_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_o_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_o_1.html'), reply_markup=config.serial_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_o_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_o_2.html'), reply_markup=config.serial_o2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)

@dp.callback_query_handler(text='serial_popular')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_p_1.html'), reply_markup=config.serial_p_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_p_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_p_2.html'), reply_markup=config.serial_p2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_p_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_p_3.html'), reply_markup=config.serial_p3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_p_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_p_3.html'), reply_markup=config.serial_p3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_p_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_p_1.html'), reply_markup=config.serial_p_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_p_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_p_1.html'), reply_markup=config.serial_p_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='serial_p_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_serials('serialhtmls/serial_p_2.html'), reply_markup=config.serial_p2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)

@dp.callback_query_handler(text='anime_best')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_best_1'], reply_markup=config.anime_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_best_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_best_2'], reply_markup=config.anime_best2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_best_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_best_3'], reply_markup=config.anime_best3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_best_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_best_3'], reply_markup=config.anime_best3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_best_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_best_1'], reply_markup=config.anime_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_best_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_best_1'], reply_markup=config.anime_best_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_best_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_best_2'], reply_markup=config.anime_best2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)

@dp.callback_query_handler(text='anime_ozh')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_ozh_1'], reply_markup=config.anime_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_o_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_ozh_2'], reply_markup=config.anime_o2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_o_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_ozh_3'], reply_markup=config.anime_o3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_o_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_ozh_3'], reply_markup=config.anime_o3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_o_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_ozh_1'], reply_markup=config.anime_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_o_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_ozh_1'], reply_markup=config.anime_o_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_o_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_ozh_2'], reply_markup=config.anime_o2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)

@dp.callback_query_handler(text='anime_popular')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_p_1'], reply_markup=config.anime_p_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_p_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_p_2'], reply_markup=config.anime_p2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_p_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_p_3'], reply_markup=config.anime_p3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_p_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_p_3'], reply_markup=config.anime_p3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_p_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_p_1'], reply_markup=config.anime_p_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_p_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_p_1'], reply_markup=config.anime_p_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='anime_p_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.anime_years['anime_p_2'], reply_markup=config.anime_p2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)


@dp.callback_query_handler(text='video_games_popular')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_1.html'), reply_markup=config.games_popular_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_2.html'), reply_markup=config.games_popular2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_5.html'), reply_markup=config.games_popular5_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_3.html'), reply_markup=config.games_popular3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_1.html'), reply_markup=config.games_popular_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_4.html'), reply_markup=config.games_popular4_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_2.html'), reply_markup=config.games_popular2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_right_button4')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_5.html'), reply_markup=config.games_popular5_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_left_button4')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_3.html'), reply_markup=config.games_popular3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_right_button5')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_1.html'), reply_markup=config.games_popular_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_popular_left_button5')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=p1.parser_games('gamehtmls/game_popular_4.html'), reply_markup=config.games_popular4_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)



@dp.callback_query_handler(text='video_games_2021')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['1'], reply_markup=config.games_popular_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_right_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['2'], reply_markup=config.games_2021_2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_left_button')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['3'], reply_markup=config.games_2021_5_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_right_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['3'], reply_markup=config.games_2021_3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_left_button2')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['1'], reply_markup=config.games_2021_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_right_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['4'], reply_markup=config.games_2021_4_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_left_button3')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['2'], reply_markup=config.games_2021_2_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_right_button4')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['5'], reply_markup=config.games_2021_5_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_left_button4')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['3'], reply_markup=config.games_2021_3_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_right_button5')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['1'], reply_markup=config.games_2021_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='games_2021_left_button5')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2021['4'], reply_markup=config.games_2021_4_movie, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.callback_query_handler(text='video_games_2022')
async def next_keyboard(call: types.CallbackQuery):   
    await call.message.edit_text(text=text.games_years_2022['1'], reply_markup=config.games_go_back_inline, disable_web_page_preview=True)
    await bot.answer_callback_query(callback_query_id=call.id)
@dp.message_handler(commands=['sendalltext'])
async def sendall(message: types.Message):
  if message.chat.type == 'private':
    if message.from_user.id == айдиклинта:
      text = message.text[12:]
      users = SQLighter.s1.get_users()
      for row in users:
        try:
          await bot.send_message(row[0], text)
        except:
          pass
    await message.answer('успешная рассылка')
@dp.message_handler(commands=['getstatic'])
async def static(message: types.Message):
  if message.chat.type == 'private':
    if message.from_user.id == айди клинта: 
        await bot.send_message('айди клинта',f'''📊Статистика:

👤Кол-во пользователей: {len(SQLighter.s1.get_users())}''')
@dp.message_handler(content_types=['text'])
async def profile(message: types.Message):
    if message.text == '👤 Профиль':
        await bot.send_message(message.chat.id, f'😀 <b>Ваше имя:</b> {message.from_user.first_name}\n<b>🙋🏻‍♂️ Ваш id:</b> {message.from_user.id}', parse_mode='HTML' )
    if message.text == '📌 Выбрать категорию':
        await bot.send_message(message.chat.id, '📌Выберите необходимую категорию:', reply_markup=config.category_inline)
    if message.text == 'ℹ️ О нас':
        await bot.send_message(message.chat.id, config.configuration['about_us'], reply_markup=config.admin_inline, disable_web_page_preview=True)
    if message.text == '👤 Об авторе':
        await bot.send_photo(message.chat.id, '')
        await bot.send_message(message.chat.id, config.configuration['about_author'], disable_web_page_preview=True)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
