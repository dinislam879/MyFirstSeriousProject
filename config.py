import aiogram
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#Configuration
import parsing_data
import random



anime_go_back_2_step = InlineKeyboardButton(text='⬅️Назад', callback_data='anime_go_back_button_2_step')
movie_go_back_2step_markup = InlineKeyboardMarkup()
movie_go_back_2step = InlineKeyboardButton(text='⬅️Назад', callback_data='movie_go_back_button_2_step')
movie_go_back_2step_markup.add(movie_go_back_2step)
serial_go_back_2_step = InlineKeyboardButton(text='⬅️Назад', callback_data='serial_go_back_button_2_step')
video_games_go_back_2_step = InlineKeyboardButton(text='⬅️Назад', callback_data='video_games_go_back_button_2_step')

movie_inline = InlineKeyboardMarkup()
movie_button1 = InlineKeyboardButton('💘 Лучшие', callback_data='movie_best')
movie_button2 = InlineKeyboardButton('🕗 Ожидаемые', callback_data='movie_ozhydaemye')
movie_inline.add(movie_button1)
movie_inline.add(movie_button2)
movie_button3 = InlineKeyboardButton(text='🎩 Жанры', callback_data='movie_genres')
movie_inline.add(movie_button3)
movie_button4 = InlineKeyboardButton('❤️‍🔥 Популярные', callback_data='movie_popular')
movie_inline.add(movie_button4)
movie_button5 = InlineKeyboardButton('💘 50 Лучших фильмов', callback_data='movie_50')
movie_inline.add(movie_button5)
movie_button6 = InlineKeyboardButton('🎬 Фильмы 2021', callback_data='movie_2021')
movie_button7 = InlineKeyboardButton('🎬 Фильмы 2022', callback_data='movie_2022')
movie_inline.add(movie_button6)
movie_inline.add(movie_button7)
movie_button8 = InlineKeyboardButton('🎬 Фильмы 2023', callback_data='movie_2023')
movie_inline.add(movie_button8)


go_back_button_1_step = InlineKeyboardButton('⬅️Назад', callback_data='go_back_1_step')
movie_inline.add(go_back_button_1_step)

serial_inline = InlineKeyboardMarkup()
serial_inline.add(InlineKeyboardButton(text='💘 Лучшие', callback_data='serial_best'))
serial_inline.add(InlineKeyboardButton(text='🕗 Ожидаемые', callback_data='serial_ozhydaemye'))
serial_inline.add(InlineKeyboardButton(text='❤️‍🔥 Популярные', callback_data='serial_popular'))

serial_button2 = InlineKeyboardButton(text='🎩 Жанры', callback_data='serial_genres')
serial_inline.add(serial_button2)
serial_button3 = InlineKeyboardButton(text='🎬 Сериалы 2022', callback_data='serial_2022')
serial_inline.add(serial_button3)
serial_button4 = InlineKeyboardButton(text='🎬 Сериалы 2021', callback_data='serial_2021')
serial_inline.add(serial_button4)
serial_inline.add(go_back_button_1_step)

start_reply = ReplyKeyboardMarkup(resize_keyboard=True)
choice_button = KeyboardButton('📌 Выбрать категорию')
start_reply.add(choice_button)
profile_button = KeyboardButton('👤 Профиль')
about_us_button = KeyboardButton('ℹ️ О нас')
start_reply.add(profile_button, about_us_button)
start_reply.add(KeyboardButton('👤 Об авторе'))
#startpoint
movie_button = InlineKeyboardButton(text='🎬 Кино', callback_data='movie')
serial_button = InlineKeyboardButton(text='🎧 Сериалы', callback_data='serial')
anime_button = InlineKeyboardButton(text='🌸 Аниме', callback_data='anime')
video_games_button = InlineKeyboardButton(text='🎮 Видеоигры', callback_data='video_games')
category_inline = InlineKeyboardMarkup().add(movie_button, serial_button, anime_button, video_games_button)

video_games_goback_markup = InlineKeyboardMarkup()
video_games_goback_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='video_games_goback')) 


video_games_inline = InlineKeyboardMarkup()
video_games_button = InlineKeyboardButton(text='🖥 Платформы', callback_data='video_games_platforms')
video_games_inline.add(video_games_button)
video_games_button1 = InlineKeyboardButton(text='⭐️ Лучшие', callback_data='video_games_best')
video_games_inline.add(video_games_button1)
video_games_button3 = InlineKeyboardButton(text='🔫 Популярные', callback_data='video_games_popular')
video_games_inline.add(video_games_button3)
video_games_button4 = InlineKeyboardButton(text='🔥 Ожидаемые', callback_data='video_games_ozh')
video_games_inline.add(video_games_button4) 
video_games_button5 = InlineKeyboardButton(text='🎮 Игры 2021 года', callback_data='video_games_2021')
video_games_inline.add(video_games_button5) 
video_games_button6 = InlineKeyboardButton(text='🎮 Игры 2022 года', callback_data='video_games_2022')
video_games_inline.add(video_games_button6) 
 
video_games_inline.add(go_back_button_1_step)

admin_inline = InlineKeyboardMarkup()
admin_button = InlineKeyboardButton(text='⚙️ Админ/Реклама', url='tg://user?id=851705578')
admin_inline.add(admin_button)



anime_popular_go_back = InlineKeyboardButton(text='⬅️Назад', callback_data='anime_popular_go_back')
anime_popular_2stepback_markup = InlineKeyboardMarkup()
anime_popular_2stepback_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='anime_popular_2stepback'))
anime_popular_markup = InlineKeyboardMarkup()
anime_popular_markup.add(InlineKeyboardButton(text='1️⃣ страница', callback_data='anime_p1page'))
anime_popular_markup.add(InlineKeyboardButton(text='2️⃣ страница', callback_data='anime_p2page'))
anime_popular_markup.add(InlineKeyboardButton(text='3️⃣ страница', callback_data='anime_p3page'))
anime_popular_markup.add(InlineKeyboardButton(text='4️⃣ страница', callback_data='anime_p4page'))
anime_popular_markup.add(InlineKeyboardButton(text='5️⃣ страница', callback_data='anime_p5page'))
anime_popular_markup.add(InlineKeyboardButton(text='6️⃣ страница', callback_data='anime_p6page'))
anime_popular_markup.add(InlineKeyboardButton(text='7️⃣ страница', callback_data='anime_p7page'))
anime_popular_markup.add(InlineKeyboardButton(text='8️⃣ страница', callback_data='anime_p8page'))
anime_popular_markup.add(InlineKeyboardButton(text='9️⃣ страница', callback_data='anime_p9page'))
anime_popular_markup.add(InlineKeyboardButton(text='🔟 страница', callback_data='anime_p10page'))
anime_popular_markup.add(anime_popular_go_back)

anime_data_go_back = InlineKeyboardMarkup()
anime_data_go_back.add(InlineKeyboardButton(text='⬅️Назад', callback_data='anime_data_go_back'))

anime_ozh_go_back = InlineKeyboardButton(text='⬅️Назад', callback_data='anime_ozh_go_back')
anime_ozh_2stepback_markup = InlineKeyboardMarkup()
anime_ozh_2stepback_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='anime_ozh_2stepback'))
anime_ozh_markup = InlineKeyboardMarkup()
anime_ozh_markup.add(InlineKeyboardButton(text='1️⃣ страница', callback_data='anime_o1page'))
anime_ozh_markup.add(InlineKeyboardButton(text='2️⃣ страница', callback_data='anime_o2page'))
anime_ozh_markup.add(InlineKeyboardButton(text='3️⃣ страница', callback_data='anime_o3page'))
anime_ozh_markup.add(InlineKeyboardButton(text='4️⃣ страница', callback_data='anime_o4page'))
anime_ozh_markup.add(InlineKeyboardButton(text='5️⃣ страница', callback_data='anime_o5page'))
anime_ozh_markup.add(InlineKeyboardButton(text='6️⃣ страница', callback_data='anime_o6page'))
anime_ozh_markup.add(InlineKeyboardButton(text='7️⃣ страница', callback_data='anime_o7page'))
anime_ozh_markup.add(InlineKeyboardButton(text='8️⃣ страница', callback_data='anime_o8page'))
anime_ozh_markup.add(InlineKeyboardButton(text='9️⃣ страница', callback_data='anime_o9page'))
anime_ozh_markup.add(InlineKeyboardButton(text='🔟 страница', callback_data='anime_o10page'))
anime_ozh_markup.add(anime_ozh_go_back)

serial_goback_genres = InlineKeyboardMarkup()
serial_goback_genres.add(InlineKeyboardButton(text='⬅️Назад', callback_data='serial_genres_goback'))

anime_inline = InlineKeyboardMarkup()
anime_button1 = InlineKeyboardButton(text='🔥 Лучшие', callback_data='anime_best')
anime_inline.add(anime_button1)
anime_inline.add(InlineKeyboardButton(text='❤️‍🔥 Популярные', callback_data='anime_popular'))
anime_inline.add(InlineKeyboardButton(text='⏱ Ожидаемые', callback_data='anime_ozh'))
anime_button3 = InlineKeyboardButton(text='🎩 Жанры', callback_data='anime_genres')
anime_inline.add(anime_button3)
anime_button4 = InlineKeyboardButton(text='🌸 Аниме 2021', callback_data='anime_2021')
anime_inline.add(anime_button4)
anime_inline.add(InlineKeyboardButton(text='🌸Аниме 2022', callback_data='anime_2022'))
anime_inline.add(InlineKeyboardButton(text='🌸Аниме 2023', callback_data='anime_2023'))
anime_inline.add(go_back_button_1_step)


anime_genres_inline = InlineKeyboardMarkup()
anime_genres_button1 = InlineKeyboardButton(text='🧬 Научная фантастика', callback_data='anime_science_fiction')
anime_genres_inline.add(anime_genres_button1)
anime_genres_button2 = InlineKeyboardButton(text='😭 Драма', callback_data='anime_drama')
anime_genres_inline.add(anime_genres_button2)
anime_genres_button4 = InlineKeyboardButton(text='🦇 Жутик', callback_data='anime_horror')
anime_genres_button5 = InlineKeyboardButton(text='🤪 Комедия', callback_data='anime_comedy')
anime_genres_inline.add(anime_genres_button4, anime_genres_button5)
anime_genres_button6 = InlineKeyboardButton(text='🔮 Магия', callback_data='anime_magic')
anime_genres_button7 = InlineKeyboardButton(text='🎒 Приключение', callback_data='anime_adventure')
anime_genres_inline.add(anime_genres_button6, anime_genres_button7)
anime_genres_button8 = InlineKeyboardButton(text='💡 Повседневность', callback_data='anime_daily')
anime_genres_inline.add(anime_genres_button8)
anime_genres_button9 = InlineKeyboardButton(text='🧩 Психология', callback_data='anime_psihology')
anime_genres_inline.add(anime_genres_button9)
anime_genres_button10 = InlineKeyboardButton(text='💔 Романтика', callback_data='anime_romance')
anime_genres_button11 = InlineKeyboardButton(text='🤫 Тайна', callback_data='anime_secret')
anime_genres_inline.add(anime_genres_button10, anime_genres_button11)

anime_genres_button12 = InlineKeyboardButton(text='✨ Сверхъестественное', callback_data='anime_supernatural')
anime_genres_inline.add(anime_genres_button12)
anime_genres_button13 = InlineKeyboardButton(text='🍿 Триллер', callback_data='anime_thriller')
anime_genres_button14 = InlineKeyboardButton(text='🌟 Фэнтези', callback_data='anime_fantasy')
anime_genres_inline.add(anime_genres_button13, anime_genres_button14)
anime_genres_button15 = InlineKeyboardButton(text='🍑 Эротика', callback_data='anime_erotic')
anime_genres_inline.add(anime_genres_button15, anime_go_back_2_step)

anime_genres_2stepback = InlineKeyboardMarkup()
anime_genres_2stepback.add(InlineKeyboardButton(text='⬅️Назад', callback_data='anime_genres_2stepback'))



movie_genres_inline = InlineKeyboardMarkup()
movie_genres_button1 = InlineKeyboardButton(text='🪓 Боевик', callback_data='movie_action')
movie_genres_button2 = InlineKeyboardButton(text='⚽️ Спорт', callback_data='movie_sport')
movie_genres_inline.add(movie_genres_button1,movie_genres_button2)
movie_genres_button3 = InlineKeyboardButton(text='⛑ Документальный', callback_data='movie_documental')
movie_genres_inline.add(movie_genres_button3)
movie_genres_button4 = InlineKeyboardButton(text='💃🏻 Драма', callback_data='movie_drama')
movie_genres_button5 = InlineKeyboardButton(text='🤪 Комедия', callback_data='movie_comedy')
movie_genres_inline.add(movie_genres_button4, movie_genres_button5)
movie_genres_button6 = InlineKeyboardButton(text='🪖 Военный', callback_data='movie_war')
movie_genres_button7 = InlineKeyboardButton(text='🦇 Мистика', callback_data='movie_mystery')
movie_genres_inline.add(movie_genres_button6, movie_genres_button7)
movie_genres_button8 = InlineKeyboardButton(text='🕸 Ужастик', callback_data='movie_horror')
movie_genres_button9 = InlineKeyboardButton(text='⚡️ Фэнтэзи', callback_data='movie_fantasy')
movie_genres_inline.add(movie_genres_button8, movie_genres_button9)
movie_genres_button10 = InlineKeyboardButton(text='⌛️ Короткометражный', callback_data='movie_short')
movie_genres_inline.add(movie_genres_button10)
movie_genres_button11 = InlineKeyboardButton(text='💔 Романтический', callback_data='movie_romance')
movie_genres_inline.add(movie_genres_button11)
movie_genres_button12 = InlineKeyboardButton(text='🛶 Приключенческий', callback_data='movie_adventure')
movie_genres_inline.add(movie_genres_button12)
movie_genres_button12 = InlineKeyboardButton(text='🍭 Мультфильм', callback_data='movie_animation')
movie_genres_inline.add(movie_genres_button12)
movie_genres_button13 = InlineKeyboardButton(text='🍕 Триллер', callback_data='movie_thriller')
movie_genres_button14 = InlineKeyboardButton(text='🍑 Эротика', callback_data='movie_erotic')
movie_genres_inline.add(movie_genres_button13, movie_genres_button14)
movie_genres_inline.add(movie_go_back_2step)
movie_genres_3steback = InlineKeyboardMarkup()
movie_genres_3steback.add(InlineKeyboardButton(text='⬅️Назад', callback_data='movie_genres_3steback'))


serial_genres_inline = InlineKeyboardMarkup()
serial_genres_button1 = InlineKeyboardButton(text='🪓 Боевик', callback_data='serial_action')
serial_genres_button2 = InlineKeyboardButton(text='⚽️ Спорт', callback_data='serial_sport')
serial_genres_inline.add(serial_genres_button1,serial_genres_button2)
serial_genres_button3 = InlineKeyboardButton(text='⛑ Документальный', callback_data='serial_documental')
serial_genres_inline.add(serial_genres_button3)
serial_genres_button4 = InlineKeyboardButton(text='💃🏻 Драма', callback_data='serial_drama')
serial_genres_button5 = InlineKeyboardButton(text='🤪 Комедия', callback_data='serial_comedy')
serial_genres_inline.add(serial_genres_button4, serial_genres_button5)
serial_genres_inline.add(InlineKeyboardButton(text='🍭 Мультфильм', callback_data='serial_animation'))
serial_genres_button6 = InlineKeyboardButton(text='🪖 Военный', callback_data='serial_war')
serial_genres_button7 = InlineKeyboardButton(text='🦇 Мистика', callback_data='serial_mystery')
serial_genres_inline.add(serial_genres_button6, serial_genres_button7)
serial_genres_button8 = InlineKeyboardButton(text='🕸 Ужастик', callback_data='serial_horror')
serial_genres_button9 = InlineKeyboardButton(text='⚡️ Фэнтэзи', callback_data='serial_fantasy')
serial_genres_inline.add(serial_genres_button8, serial_genres_button9)
serial_genres_button10 = InlineKeyboardButton(text='⌛️ Короткометражный', callback_data='serial_short')
serial_genres_inline.add(serial_genres_button10)
serial_genres_buttoN10 = InlineKeyboardButton(text='☀️ Ситком', callback_data='serial_sitcom')
serial_genres_buttoN11 = InlineKeyboardButton(text='💼 Детектив', callback_data='serial_crime')
serial_genres_inline.add(serial_genres_buttoN10, serial_genres_buttoN11)
serial_genres_button11 = InlineKeyboardButton(text='💔 Романтический', callback_data='serial_romance')
serial_genres_inline.add(serial_genres_button11)
serial_genres_buttoN12 = InlineKeyboardButton(text='🚑 Медицинский', callback_data='serial_medical')
serial_genres_inline.add(serial_genres_buttoN12)
serial_genres_buttoN13 = InlineKeyboardButton(text='🚓 Полицейский', callback_data='serial_police')
serial_genres_inline.add(serial_genres_buttoN13)
serial_genres_button12 = InlineKeyboardButton(text='🛶 Приключенческий', callback_data='serial_adventure')
serial_genres_inline.add(serial_genres_button12)
serial_genres_button14 = InlineKeyboardButton(text='🍕 Триллер', callback_data='serial_thriller')
serial_genres_button15 = InlineKeyboardButton(text='🍑 Эротика', callback_data='serial_erotic')
serial_genres_inline.add(serial_genres_button14, serial_genres_button15)
serial_genres_inline.add(serial_go_back_2_step)


counter_vdgms1 = InlineKeyboardButton(text='1/2', callback_data='video_games_1/2')
counter_vdgms2 = InlineKeyboardButton(text='2/2', callback_data='video_games_2/2')

left_side_vdgms1 = InlineKeyboardButton(text='◀️', callback_data='left_side_vdgms1')
right_side_vdgms1 = InlineKeyboardButton(text='▶️', callback_data='right_side_vdgms1')
left_side_vdgms2 = InlineKeyboardButton(text='◀️', callback_data='left_side_vdgms2')
right_side_vdgms2 = InlineKeyboardButton(text='▶️', callback_data='right_side_vdgms2')
video_games_platforms_inline_1_page = InlineKeyboardMarkup()
video_games_platforms_inline_2_page = InlineKeyboardMarkup()
video_games_pc = InlineKeyboardButton(text='💻 PC', callback_data='video_games_pc')
video_games_platforms_inline_1_page.add(video_games_pc)
video_games_android = InlineKeyboardButton(text='📱 Android', callback_data='video_games_android')
video_games_ios = InlineKeyboardButton(text='🍏 IOS', callback_data='video_games_ios')
video_games_platforms_inline_1_page.add(video_games_android, video_games_ios)
video_games_play_station_5 = InlineKeyboardButton(text='🎮 Play Station 5', callback_data='video_games_play_station_5')
video_games_platforms_inline_1_page.add(video_games_play_station_5)
video_games_play_station_4 = InlineKeyboardButton(text='🎮 Play Station 4', callback_data='video_games_play_station_4')
video_games_platforms_inline_1_page.add(video_games_play_station_4)
video_games_play_station_3 = InlineKeyboardButton(text='🎮 Play Station 3', callback_data='video_games_play_station_3')
video_games_platforms_inline_1_page.add(video_games_play_station_3)
video_games_play_station_2 = InlineKeyboardButton(text='🎮 Play Station 2', callback_data='video_games_play_station_2')
video_games_platforms_inline_1_page.add(video_games_play_station_2)
video_games_play_station = InlineKeyboardButton(text='🎮 Play Station', callback_data='video_games_play_station')
video_games_platforms_inline_1_page.add(video_games_play_station)
video_games_xbox = InlineKeyboardButton(text='🟢 XBOX', callback_data='video_games_xbox')
video_games_xbox_one = InlineKeyboardButton(text='🟢 XBOX ONE', callback_data='video_games_xbox_one')
video_games_platforms_inline_2_page.add(video_games_xbox, video_games_xbox_one)
video_games_xbox_360 = InlineKeyboardButton(text='🟢 XBOX 360', callback_data='video_games_xbox_360')
video_games_xbox_series_xs = InlineKeyboardButton(text='🟢 XBOX Series X|S', callback_data='video_games_xbox_xs')
video_games_platforms_inline_2_page.add(video_games_xbox_360, video_games_xbox_series_xs)
video_games_browser = InlineKeyboardButton(text='🌎 Браузер', callback_data='video_games_browser')
video_games_linux = InlineKeyboardButton(text='🐧 Linux', callback_data='video_games_linux')
video_games_platforms_inline_2_page.add(video_games_linux, video_games_browser)
video_games_nintendo_switch = InlineKeyboardButton(text='🔴 Nintendo Switch 🔵', callback_data='video_games_nintendo_switch')
video_games_platforms_inline_2_page.add(video_games_nintendo_switch)
video_games_nintendo_64 = InlineKeyboardButton(text='🔴 Nintendo 64 🔵', callback_data='video_games_nintendo_64')
video_games_platforms_inline_1_page.add(video_games_nintendo_64)


video_games_platform_go_back = InlineKeyboardMarkup()
video_games_platform_go_back.add(InlineKeyboardButton(text='⬅️Назад', callback_data='video_games_go_back_platforms'))
video_games_platform_go_back2 = InlineKeyboardMarkup()
video_games_platform_go_back2.add(InlineKeyboardButton(text='⬅️Назад', callback_data='video_games_go_back_platforms2'))



video_games_platforms_inline_1_page.add(left_side_vdgms1,counter_vdgms1, right_side_vdgms1)
video_games_platforms_inline_1_page.add(video_games_go_back_2_step)
video_games_platforms_inline_2_page.add(left_side_vdgms2,counter_vdgms2, right_side_vdgms2)
video_games_platforms_inline_2_page.add(video_games_go_back_2_step)

markup_best_movie = InlineKeyboardMarkup()
markup_best_movie.add(InlineKeyboardButton(text='◀️', callback_data='movie_best_left_button'), InlineKeyboardButton(text='1/2', callback_data='movie_best_counter_button'), InlineKeyboardButton(text='▶️', callback_data='movie_best_right_button'))
markup_best2_movie = InlineKeyboardMarkup()
markup_best2_movie.add(InlineKeyboardButton(text='◀️', callback_data='movie_best_left_button2'), InlineKeyboardButton(text='2/2', callback_data='movie_best_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='movie_best_right_button2'))
markup_best_movie.add(movie_go_back_2step)
markup_best2_movie.add(movie_go_back_2step)



games_go_back = InlineKeyboardButton(text='⬅️Назад', callback_data='games_go_back')



games_popular_2stepback_markup = InlineKeyboardMarkup()
games_popular_2stepback_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_popular_2stepback'))
games_popular_markup = InlineKeyboardMarkup()
games_popular_markup.add(InlineKeyboardButton(text='1️⃣ страница', callback_data='games_p1page'))
games_popular_markup.add(InlineKeyboardButton(text='2️⃣ страница', callback_data='games_p2page'))
games_popular_markup.add(InlineKeyboardButton(text='3️⃣ страница', callback_data='games_p3page'))
games_popular_markup.add(InlineKeyboardButton(text='4️⃣ страница', callback_data='games_p4page'))
games_popular_markup.add(InlineKeyboardButton(text='5️⃣ страница', callback_data='games_p5page'))
games_popular_markup.add(InlineKeyboardButton(text='6️⃣ страница', callback_data='games_p6page'))
games_popular_markup.add(InlineKeyboardButton(text='7️⃣ страница', callback_data='games_p7page'))
games_popular_markup.add(InlineKeyboardButton(text='8️⃣ страница', callback_data='games_p8page'))
games_popular_markup.add(InlineKeyboardButton(text='9️⃣ страница', callback_data='games_p9page'))
games_popular_markup.add(InlineKeyboardButton(text='🔟 страница', callback_data='games_p10page'))
games_popular_markup.add(games_go_back)





games_pc_2stepback_markup = InlineKeyboardMarkup()
games_pc_2stepback_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_pc_2stepback'))
games_pc_markup = InlineKeyboardMarkup()
games_pc_markup.add(InlineKeyboardButton(text='1️⃣ страница', callback_data='games_pc1page'))
games_pc_markup.add(InlineKeyboardButton(text='2️⃣ страница', callback_data='games_pc2page'))
games_pc_markup.add(InlineKeyboardButton(text='3️⃣ страница', callback_data='games_pc3page'))
games_pc_markup.add(InlineKeyboardButton(text='4️⃣ страница', callback_data='games_pc4page'))
games_pc_markup.add(InlineKeyboardButton(text='5️⃣ страница', callback_data='games_pc5page'))
games_pc_markup.add(InlineKeyboardButton(text='6️⃣ страница', callback_data='games_pc6page'))
games_pc_markup.add(InlineKeyboardButton(text='7️⃣ страница', callback_data='games_pc7page'))
games_pc_markup.add(InlineKeyboardButton(text='8️⃣ страница', callback_data='games_pc8page'))
games_pc_markup.add(InlineKeyboardButton(text='9️⃣ страница', callback_data='games_pc9page'))
games_pc_markup.add(InlineKeyboardButton(text='🔟 страница', callback_data='games_pc10page'))
games_pc_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_pc_go_back'))

games_android_2stepback_markup = InlineKeyboardMarkup()
games_android_2stepback_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_android_2stepback'))
games_android_markup = InlineKeyboardMarkup()
games_android_markup.add(InlineKeyboardButton(text='1️⃣ страница', callback_data='games_andr1page'))
games_android_markup.add(InlineKeyboardButton(text='2️⃣ страница', callback_data='games_andr2page'))
games_android_markup.add(InlineKeyboardButton(text='3️⃣ страница', callback_data='games_andr3page'))
games_android_markup.add(InlineKeyboardButton(text='4️⃣ страница', callback_data='games_andr4page'))
games_android_markup.add(InlineKeyboardButton(text='5️⃣ страница', callback_data='games_andr5page'))
games_android_markup.add(InlineKeyboardButton(text='6️⃣ страница', callback_data='games_andr6page'))
games_android_markup.add(InlineKeyboardButton(text='7️⃣ страница', callback_data='games_andr7page'))
games_android_markup.add(InlineKeyboardButton(text='8️⃣ страница', callback_data='games_andr8page'))
games_android_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_pc_go_back'))


games_ios_2stepback_markup = InlineKeyboardMarkup()
games_ios_2stepback_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_ios_2stepback'))
games_ios_markup = InlineKeyboardMarkup()
games_ios_markup.add(InlineKeyboardButton(text='1️⃣ страница', callback_data='games_ios1page'))
games_ios_markup.add(InlineKeyboardButton(text='2️⃣ страница', callback_data='games_ios2page'))
games_ios_markup.add(InlineKeyboardButton(text='3️⃣ страница', callback_data='games_ios3page'))
games_ios_markup.add(InlineKeyboardButton(text='4️⃣ страница', callback_data='games_ios4page'))
games_ios_markup.add(InlineKeyboardButton(text='5️⃣ страница', callback_data='games_ios5page'))
games_ios_markup.add(InlineKeyboardButton(text='6️⃣ страница', callback_data='games_ios6page'))
games_ios_markup.add(InlineKeyboardButton(text='7️⃣ страница', callback_data='games_ios7page'))
games_ios_markup.add(InlineKeyboardButton(text='8️⃣ страница', callback_data='games_ios8page'))
games_ios_markup.add(InlineKeyboardButton(text='9️⃣ страница', callback_data='games_ios9page'))
games_ios_markup.add(InlineKeyboardButton(text='🔟 страница', callback_data='games_ios10page'))
games_ios_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_pc_go_back'))




games_2021_2stepback_markup = InlineKeyboardMarkup()
games_2021_2stepback_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_2021_2stepback'))
games_2021_markup = InlineKeyboardMarkup()
games_2021_markup.add(InlineKeyboardButton(text='1️⃣ страница', callback_data='games_2021_1page'))
games_2021_markup.add(InlineKeyboardButton(text='2️⃣ страница', callback_data='games_2021_2page'))
games_2021_markup.add(InlineKeyboardButton(text='3️⃣ страница', callback_data='games_2021_3page'))
games_2021_markup.add(InlineKeyboardButton(text='4️⃣ страница', callback_data='games_2021_4page'))
games_2021_markup.add(InlineKeyboardButton(text='5️⃣ страница', callback_data='games_2021_5page'))
games_2021_markup.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_go_back'))

games_go_back_inline = InlineKeyboardMarkup()
games_go_back_inline.add(InlineKeyboardButton(text='⬅️Назад', callback_data='games_go_back'))


markup_popular_movie = InlineKeyboardMarkup()
markup_popular_movie.add(InlineKeyboardButton(text='◀️', callback_data='movie_popular_left_button'), InlineKeyboardButton(text='1/3', callback_data='movie_popular_counter_button'), InlineKeyboardButton(text='▶️', callback_data='movie_popular_right_button'))
markup_popular_movie.add(InlineKeyboardButton(text='⬅️Назад', callback_data='movie_go_back'))
markup_popular2_movie = InlineKeyboardMarkup()
markup_popular2_movie.add(InlineKeyboardButton(text='◀️', callback_data='movie_popular_left_button2'), InlineKeyboardButton(text='2/3', callback_data='movie_popular_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='movie_popular_right_button2'))
markup_popular2_movie.add(InlineKeyboardButton(text='⬅️Назад', callback_data='movie_go_back'))
markup_popular3_movie = InlineKeyboardMarkup()
markup_popular3_movie.add(InlineKeyboardButton(text='◀️', callback_data='movie_popular_left_button3'), InlineKeyboardButton(text='3/3', callback_data='movie_popular_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='movie_popular_right_button3'))
markup_popular3_movie.add(InlineKeyboardButton(text='⬅️Назад', callback_data='movie_go_back'))


markup_o_movie = InlineKeyboardMarkup()
markup_o_movie.add(InlineKeyboardButton(text='◀️', callback_data='movie_o_left_button'), InlineKeyboardButton(text='1/3', callback_data='movie_o_counter_button'), InlineKeyboardButton(text='▶️', callback_data='movie_o_right_button'))
markup_o_movie.add(InlineKeyboardButton(text='⬅️Назад', callback_data='movie_go_back'))
markup_o2_movie = InlineKeyboardMarkup()
markup_o2_movie.add(InlineKeyboardButton(text='◀️', callback_data='movie_o_left_button2'), InlineKeyboardButton(text='2/3', callback_data='movie_o_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='movie_o_right_button2'))
markup_o2_movie.add(InlineKeyboardButton(text='⬅️Назад', callback_data='movie_go_back'))
markup_o3_movie = InlineKeyboardMarkup()
markup_o3_movie.add(InlineKeyboardButton(text='◀️', callback_data='movie_o_left_button3'), InlineKeyboardButton(text='3/3', callback_data='movie_o_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='movie_o_right_button3'))
markup_o3_movie.add(InlineKeyboardButton(text='⬅️Назад', callback_data='movie_go_back'))

serial_go_back_markup = InlineKeyboardMarkup()
serial_go_back = InlineKeyboardButton(text='⬅️Назад', callback_data='serial_go_back')
serial_go_back_markup.add(serial_go_back)
serial_best_movie = InlineKeyboardMarkup()
serial_best_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_best_left_button'), InlineKeyboardButton(text='1/3', callback_data='serial_best_counter_button'), InlineKeyboardButton(text='▶️', callback_data='serial_best_right_button'))
serial_best_movie.add(serial_go_back)
serial_best2_movie = InlineKeyboardMarkup()
serial_best2_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_best_left_button2'), InlineKeyboardButton(text='2/3', callback_data='serial_best_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='serial_best_right_button2'))
serial_best2_movie.add(serial_go_back)
serial_best3_movie = InlineKeyboardMarkup()
serial_best3_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_best_left_button3'), InlineKeyboardButton(text='3/3', callback_data='serial_best_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='serial_best_right_button3'))
serial_best3_movie.add(serial_go_back)

anime_go_back = InlineKeyboardButton(text='⬅️Назад', callback_data='anime_go_back')


anime_best_movie = InlineKeyboardMarkup()
anime_best_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_best_left_button'), InlineKeyboardButton(text='1/3', callback_data='anime_best_counter_button'), InlineKeyboardButton(text='▶️', callback_data='anime_best_right_button'))
anime_best_movie.add(anime_go_back)
anime_best2_movie = InlineKeyboardMarkup()
anime_best2_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_best_left_button2'), InlineKeyboardButton(text='2/3', callback_data='anime_best_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='anime_best_right_button2'))
anime_best2_movie.add(anime_go_back)
anime_best3_movie = InlineKeyboardMarkup()
anime_best3_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_best_left_button3'), InlineKeyboardButton(text='3/3', callback_data='anime_best_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='anime_best_right_button3'))
anime_best3_movie.add(anime_go_back)

anime_o_movie = InlineKeyboardMarkup()
anime_o_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_o_left_button'), InlineKeyboardButton(text='1/3', callback_data='anime_o_counter_button'), InlineKeyboardButton(text='▶️', callback_data='anime_o_right_button'))
anime_o_movie.add(anime_go_back)
anime_o2_movie = InlineKeyboardMarkup()
anime_o2_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_o_left_button2'), InlineKeyboardButton(text='2/3', callback_data='anime_o_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='anime_o_right_button2'))
anime_o2_movie.add(anime_go_back)
anime_o3_movie = InlineKeyboardMarkup()
anime_o3_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_o_left_button3'), InlineKeyboardButton(text='3/3', callback_data='anime_o_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='anime_o_right_button3'))
anime_o3_movie.add(anime_go_back)

anime_p_movie = InlineKeyboardMarkup()
anime_p_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_p_left_button'), InlineKeyboardButton(text='1/3', callback_data='anime_p_counter_button'), InlineKeyboardButton(text='▶️', callback_data='anime_p_right_button'))
anime_p_movie.add(anime_go_back)
anime_p2_movie = InlineKeyboardMarkup()
anime_p2_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_p_left_button2'), InlineKeyboardButton(text='2/3', callback_data='anime_p_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='anime_p_right_button2'))
anime_p2_movie.add(anime_go_back)
anime_p3_movie = InlineKeyboardMarkup()
anime_p3_movie.add(InlineKeyboardButton(text='◀️', callback_data='anime_p_left_button3'), InlineKeyboardButton(text='3/3', callback_data='anime_p_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='anime_p_right_button3'))
anime_p3_movie.add(anime_go_back)

serial_o_movie = InlineKeyboardMarkup()
serial_o_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_o_left_button'), InlineKeyboardButton(text='1/3', callback_data='serial_o_counter_button'), InlineKeyboardButton(text='▶️', callback_data='serial_o_right_button'))
serial_o_movie.add(serial_go_back)
serial_o2_movie = InlineKeyboardMarkup()
serial_o2_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_o_left_button2'), InlineKeyboardButton(text='2/3', callback_data='serial_o_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='serial_o_right_button2'))
serial_o2_movie.add(serial_go_back)
serial_o3_movie = InlineKeyboardMarkup()
serial_o3_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_o_left_button3'), InlineKeyboardButton(text='3/3', callback_data='serial_o_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='serial_o_right_button3'))
serial_o3_movie.add(serial_go_back)

serial_p_movie = InlineKeyboardMarkup()
serial_p_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_p_left_button'), InlineKeyboardButton(text='1/3', callback_data='serial_p_counter_button'), InlineKeyboardButton(text='▶️', callback_data='serial_p_right_button'))
serial_p_movie.add(serial_go_back)
serial_p2_movie = InlineKeyboardMarkup()
serial_p2_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_p_left_button2'), InlineKeyboardButton(text='2/3', callback_data='serial_p_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='serial_p_right_button2'))
serial_p2_movie.add(serial_go_back)
serial_p3_movie = InlineKeyboardMarkup()
serial_p3_movie.add(InlineKeyboardButton(text='◀️', callback_data='serial_p_left_button3'), InlineKeyboardButton(text='3/3', callback_data='serial_p_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='serial_p_right_button3'))
serial_p3_movie.add(serial_go_back)





games_popular_movie = InlineKeyboardMarkup()
games_popular_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_popular_left_button'), InlineKeyboardButton(text='1/5', callback_data='games_popular_counter_button'), InlineKeyboardButton(text='▶️', callback_data='games_popular_right_button'))
games_popular_movie.add(games_go_back)
games_popular2_movie = InlineKeyboardMarkup()
games_popular2_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_popular_left_button2'), InlineKeyboardButton(text='2/5', callback_data='games_popular_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='games_popular_right_button2'))
games_popular2_movie.add(games_go_back)
games_popular3_movie = InlineKeyboardMarkup()
games_popular3_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_popular_left_button3'), InlineKeyboardButton(text='3/5', callback_data='games_popular_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='games_popular_right_button3'))
games_popular3_movie.add(games_go_back)
games_popular4_movie = InlineKeyboardMarkup()
games_popular4_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_popular_left_button4'), InlineKeyboardButton(text='4/5', callback_data='games_popular_counter4_button'), InlineKeyboardButton(text='▶️', callback_data='games_popular_right_button4'))
games_popular4_movie.add(games_go_back)
games_popular5_movie = InlineKeyboardMarkup()
games_popular5_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_popular_left_button5'), InlineKeyboardButton(text='5/5', callback_data='games_popular_counter5_button'), InlineKeyboardButton(text='▶️', callback_data='games_popular_right_button5'))
games_popular5_movie.add(games_go_back)

games_2021_movie = InlineKeyboardMarkup()
games_2021_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_2021_left_button'), InlineKeyboardButton(text='1/5', callback_data='games_2021_counter_button'), InlineKeyboardButton(text='▶️', callback_data='games_2021_right_button'))
games_2021_movie.add(games_go_back)
games_2021_2_movie = InlineKeyboardMarkup()
games_2021_2_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_2021_left_button2'), InlineKeyboardButton(text='2/5', callback_data='games_2021_counter2_button'), InlineKeyboardButton(text='▶️', callback_data='games_2021_right_button2'))
games_2021_2_movie.add(games_go_back)
games_2021_3_movie = InlineKeyboardMarkup()
games_2021_3_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_2021_left_button3'), InlineKeyboardButton(text='3/5', callback_data='games_2021_counter3_button'), InlineKeyboardButton(text='▶️', callback_data='games_2021_right_button3'))
games_2021_3_movie.add(games_go_back)
games_2021_4_movie = InlineKeyboardMarkup()
games_2021_4_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_2021_left_button4'), InlineKeyboardButton(text='4/5', callback_data='games_2021_counter4_button'), InlineKeyboardButton(text='▶️', callback_data='games_2021_right_button4'))
games_2021_4_movie.add(games_go_back)
games_2021_5_movie = InlineKeyboardMarkup()
games_2021_5_movie.add(InlineKeyboardButton(text='◀️', callback_data='games_2021_left_button5'), InlineKeyboardButton(text='5/5', callback_data='games_2021_counter5_button'), InlineKeyboardButton(text='▶️', callback_data='games_2021_right_button5'))
games_2021_5_movie.add(games_go_back)

configuration = {
    'about_us':'''🔊🔊🔊  Хотите знать как можно больше о кино, сериалах, играх и аниме и всегда быть в курсе происходящего?🤨🤨🤨 
😇Тогда вам прямая дорога на «КГ-Портал» — лучший в стране портал о кино (вот так вот скромно и без прикрас).🥶🥶🥶
Никакой светской хроники, некрологов и поздравлений с днём рождения — всё строго по делу (почти всегда), непредвзято (реже) и с нашим фирменным юмором (без этого никак).



Здесь вы найдёте самые свежие новости, трейлеры, кадры и прочие промо-материалы фильмов, сериалов, видеоигр и аниме; рецензии, эпизодники и обсуждения, обзоры новинок и невероятно содержательные подкасты. А также самые последние релизы, данные бокс-офиса, форум для непринуждённого общения и многое другое — скучно не будет!
Ищете хорошее кино для приятного вечера, самые горячие новинки сериалов, лучшие игры на ПК или аниме про любовь? Мы и здесь сможем вам помочь.
И кстати чуть не забыл,\n Наш сайтик🌍: https://kg-portal.ru/
Наш форум🗣: http://www.kg-forum.ru/
⬆️⬆️⬆️🔥🔥🔥🔥''',
    'bot_token':'my token',
    'bot_name': 'КГ-ПОРТАЛ',
    'get_start':'Здравствуй, дорогой пользователь!☺️ Хотите знать как можно больше о кино, сериалах, играх и аниме и всегда быть в курсе происходящего? Тогда вам прямая дорога на «КГ-Портал» — лучший в стране портал о кино (вот так вот скромно и без прикрас).Здесь вы найдете лучшие и популярные кино, сериалы и аниме!🎬🎮🌸 \n 🌍Наш сайт: https://kg-portal.ru/',
    'about_author':'''👤Об авторе
💎Гений; миллионер; слоупок; филантроп (бесспорно; когда-нибудь; борется с собой; в другой жизни). 
В девяностых в сумасшедших количествах продавал диски с компьютерными играми на «Юноне» (исключительно лицензионные, конечно),
 поэтому играл во всё подряд.\n
 🌍Наш сайт:
🔈🔈🔈🔈🔈🔈🔈🔈

 В начале нулевых как следует получил по лбу долби-звуком «Звёздных войн» (он бы первый эпизод куда круче снял!), 
 отчего быстро поменял приоритеты и подался в киноценители. 
 Из этой трясины не может выбраться и по сей день, по поводу чего, правда, совершенно не переживает. 
 С радостью записал бы в соавторы КГ свою кошку, но опасается дурных ассоциаций.
 '''
}

#this is bot token


