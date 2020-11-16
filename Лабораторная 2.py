import csv
import re

genres = input('Введите жанр\n').split(',')
categories = input('Введите категорию\n').split(',')
developers = input('Введите разработчика\n').split(',')
platforms = input('Введите платформу\n').split(',')
year = input('Введите год выхода игры (год или промежуток \'YYYY-YYYY\').\n')
price = input('Введите цену игры в долларах.\nНапример, \'<10\' или \'0\'\n')
ratings = input('Положительных отзывов должно быть больше?\nНапишите \'+\', если должно\n')
def check_genre(game_desc):
    return any(genre in game_desc for genre in genres) or (genres == [''])
def check_category(game_desc):
    return any(genre in game_desc for genre in categories) or (categories == [''])
def check_developer(game_desc):
    return any(developer in game_desc for developer in developers) or (developers == [''])
def check_platform(game_desc):
    return any(platform in game_desc for platform in platforms) or (platforms == [''])
def check_year(game_desc, input_year=year):
    if '-' in input_year:
        input_year = input_year.split('-')
        return input_year[0] <= game_desc <= input_year[1]
    else:
        return (game_desc == input_year) or (input_year == '')
def check_price(game_desc, input_price=price):
    if input_price == '':
        return 0.0 <= game_desc <= 422.0
    elif input_price[0] == '<':
        k = float(re.findall(r'[\d.]+', input_price)[0])
        return 0.0 <= game_desc <= k
    else:
        return input_price == game_desc 
def check_comments(game_desc):
    return ((ratings == '+') and (game_desc[0] > game_desc[1])) or (ratings == '')
with open('steam.csv', encoding='utf-8') as f, \
     open('result.txt', 'w', encoding='utf-8') as f2:
    reader = csv.reader(f)
    for line in reader:
        if line[0] == 'appid':
            continue
        game_genres = line[9].split(';')
        game_categories = line[8].split(';')
        game_developer = line[4].split(';')
        game_platforms = line[6].split(';')
        game_year = line[2].split('-')[0]
        game_price = float(line[17])
        game_comments = [int(line[12]), int(line[13])]
        if (check_genre(game_genres) and
            check_category(game_categories) and
            check_developer(game_developer) and
            check_platform(game_platforms) and
            check_year(game_year) and
            check_price(game_price) and
            check_comments(game_comments)):
            f2.write(line[1]+'\n')

