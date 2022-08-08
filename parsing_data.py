from bs4 import BeautifulSoup
import requests



class ParserMovie:
    def parser_best_movie(self, filename):
        result = ''
        with open(filename,'r', encoding='utf-8') as f:
            src = f.read()

        soup = BeautifulSoup(src, 'lxml')
        result += soup.find('div', class_='uni_top_wrap uni_top_movies').find('h1').text + '\n'
        res = soup.find('div', class_='reviews_list')
        listing = res.find_all('div', class_='listing_item movies')
        for i,e in enumerate(listing,1):
            
            result += str(i)+'. '+ e.find('b').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'
        return result
    def parser_serials(self, filename):
        result = ''
        with open(filename,'r', encoding='utf-8') as f:
            src = f.read()

        soup = BeautifulSoup(src, 'lxml')
        result += soup.find('div', class_='uni_top_wrap uni_top_tv').find('h1').text + '\n'
        res = soup.find('div', class_='reviews_list')
        listing = res.find_all('div', class_='listing_item tv')
        for i,e in enumerate(listing,1):
            
            result += str(i)+'. '+ e.find('b').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'    
        return result
    def parser_anime(self, filename):
        result = ''
        with open(filename,'r', encoding='utf-8') as f:
            src = f.read()

        soup = BeautifulSoup(src, 'lxml')
        result += soup.find('div', class_='uni_top_wrap uni_top_anime').find('h1').text + '\n'
        res = soup.find('div', class_='reviews_list')
        listing = res.find_all('div', class_='listing_item anime')
        for i,e in enumerate(listing,1):
            
            result += str(i)+'. '+ e.find('b').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'    
        return result
    def parser_data_movies1(self, filename):
        result = ''
        with open(filename, 'r', encoding='utf-8') as f:
            src = f.read()
        
        soup = BeautifulSoup(src, 'lxml')
        result += soup.find('div', class_='uni_top_wrap uni_top_movies').find('h1').text + '\n'
        res = soup.find('div', class_='content_main')
        listing = res.find_all('div', class_='title')
        result += 'Январь:\n\n'
        for i,e in enumerate(listing,1):
            if i == 20:
                result += 'Февраль:\n\n'
            if i == 31:
                break
            result += str(i) + '. ' + e.find('a').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'    
        return result
    def parser_data_movies(self, filename):
        result = ''
        with open(filename, 'r', encoding='utf-8') as f:
            src = f.read()
        
        soup = BeautifulSoup(src, 'lxml')
        result += soup.find('div', class_='uni_top_wrap uni_top_tv').find('h1').text + '\n'
        res = soup.find('div', class_='content_main')
        listing = res.find_all('div', class_='title')
        for i,e in enumerate(listing,1):
            if i == 31:
                break
            result += str(i) + '. ' + e.find('a').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'    
        return result
    def parser_data_anime(self, filename):
        result = ''
        with open(filename, 'r', encoding='utf-8') as f:
            src = f.read()
        
        soup = BeautifulSoup(src, 'lxml')
        result += soup.find('div', class_='uni_top_wrap uni_top_anime').find('h1').text + '\n'
        res = soup.find('div', class_='content_main')
        listing = res.find_all('div', class_='title')
        for i,e in enumerate(listing,1):
            result += str(i) + '. ' + e.find('a').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'    
        return result
    def parser_data_games(self, filename):
        result = ''
        with open(filename, 'r', encoding='utf-8') as f:
            src = f.read()
        
        soup = BeautifulSoup(src, 'lxml')
        result += soup.find('div', class_='uni_top_wrap uni_top_games').find('h1').text +': '+'\n'
        res = soup.find('div', class_='content_main')
        listing = res.find_all('div', class_='title')
        for i,e in enumerate(listing,1):
            result += str(i) + '. ' + e.find('a').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'    
        return result
    def parser_games(self, filename):
        result = ''
        with open(filename,'r', encoding='utf-8') as f:
            src = f.read()

        soup = BeautifulSoup(src, 'lxml')
        result += soup.find('div', class_='uni_top_wrap uni_top_games').find('h1').text +': ' + '\n'
        res = soup.find('div', class_='reviews_list')
        listing = res.find_all('div', class_='listing_item games')
        for i,e in enumerate(listing,1):
            if i > 31:
                break
            result += str(i)+'. '+ e.find('b').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'   
        return result
    def filedownloader(self,name):
        link = requests.get('https://kg-portal.ru/anime/s_views/2021/p_' + name +'/').text

        with open('animehtmls/anime_ozh_'+name+'.html', 'w', encoding='utf-8') as f:
            f.write(link)
    def parser_50_best_movies(self, filename):
        result = ''
        with open(filename, 'r', encoding='utf-8') as f:
            src = f.read()

        soup = BeautifulSoup(src, 'lxml')
        res = soup.find('div', class_='styles_contentSlot__h_lSN')
        main = res.find('main')
        mainer = main.find_all('div', class_='base-movie-main-info_mainInfo__ZL_u3')
        for i,e in enumerate(mainer,1):
            result += str(i) + '. ' + e.find('span').text + '\n'
        result += '🌍Подробнее на сайте: https://kg-portal.ru/'
        return result

p1 = ParserMovie()
#print(p1.parser_data_games('gamehtmls/games_2021.html'))
#print(p1.parser_data_games('gamehtmls/game_2021_2.html'))
#print(p1.parser_games('gamehtmls/games_android_8.html'))
#link = requests.get('https://kg-portal.ru/anime/s_year/2021/').text
#with open('animehtmls/anime_2021.html', 'w', encoding='utf-8') as f:
    #f.write(link)
#print(p1.parser_anime('animehtmls/anime_ozh_3.html'))
#ls = []
#for i in range(2,11):
   # p1.filedownloader(str(i))
   
#print(p1.parser_data_anime('animehtmls/anime_2021.html'))