from bs4 import BeautifulSoup as bs
from datetime import datetime
import pandas as pd
import requests
import pickle
import urllib
import json
import re

# functions
def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_data_pickle(name, data):
    with open(name, 'wb') as f:
        pickle.dump(data, f)

def load_data(title):
    with open(title, encoding='utf-8') as f:
        return json.load(f)

def load_data_pickle(name):
    with open(name, 'rb') as f:
        return pickle.load(f)

def clean_tags(bsoup):
    for tag in bsoup.find_all("sup"):
        tag.decompose()

def minute_to_int(running_time):
    if running_time == 'N/A':
        return None
    if isinstance(running_time, list):
        return int(running_time[0].split(' ')[0])
    else:
        return int(running_time.split(' ')[0])

def get_content_val(row_data):
    if row_data.find("li"):
        return [li.get_text(" ",strip=True).replace("\xa0", " ") for li in row_data.find_all("li")]
    elif row_data.find("br"):
        return [text for text in row_data.stripped_strings]
    else:
        return row_data.get_text(" ",strip=True).replace("\xa0", " ")

def get_info_box(url):
    r = requests.get(url)
    soup = bs(r.content)
    info_box = soup.find(class_= "infobox vevent")
    info_box_rows = info_box.find_all("tr")
        
    clean_tags(soup)
    movie_info = {}

    for index, row in enumerate(info_box_rows):
        if index == 0:
            movie_info['title'] = row.find("th").get_text(" ",strip=True)
        elif index == 1:
            continue
        else:
            header = row.find('th')
            if header:
                content_key = row.find("th").get_text(" ",strip=True)
                content_value = get_content_val(row.find("td"))
                movie_info[content_key] = content_value
    return movie_info

# movie dates into date time obj
def clean_date(date):
    return date.split("(")[0].strip()

def date_conversion(date):
    if isinstance(date, list):
        date = date[0]
        
    if date == "N/A":
        return None
        
    date_str = clean_date(date)

    fmts = ["%B %d, %Y", "%d %B %Y"]
    for fmt in fmts:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            pass
    return None

# money conversion str->float
amounts = r"thousand|million|billion"
number = r"\d+(,\d{3})*\.*\d*"

word_re = rf"\${number}(-|\sto\s|–)?({number})?\s({amounts})"
value_re = rf"\${number}"

def word_to_value(word):
    value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
    return value_dict[word]

def parse_word_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))
    word = re.search(amounts, string, flags=re.I).group().lower()
    word_value = word_to_value(word)
    return value*word_value

def parse_value_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))
    return value

'''
money_conversion("$12.2 million") --> 12200000 ## Word syntax
money_conversion("$790,000") --> 790000        ## Value syntax
'''
def money_conversion(money):
    if money == "N/A":
        return None

    if isinstance(money, list):
        money = money[0]
        
    word_syntax = re.search(word_re, money, flags=re.I)
    value_syntax = re.search(value_re, money)

    if word_syntax:
        return parse_word_syntax(word_syntax.group())

    elif value_syntax:
        return parse_value_syntax(value_syntax.group())

    else:
        return None

# ratings
def get_omdb_info(title):
    base_url = "http://www.omdbapi.com/?"
    parameters = {"apikey": '563d678b', 't': title}
    params_encoded = urllib.parse.urlencode(parameters)
    full_url = base_url + params_encoded
    return requests.get(full_url).json()

def get_rotten_tomato_score(omdb_info):
    ratings = omdb_info.get('Ratings', [])
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            return rating['Value']

# retrieve content
r = requests.get("https://en.wikipedia.org/wiki/Matt_Damon_filmography")
soup = bs(r.content)
# get list
movies = soup.select(".wikitable.sortable i a")

base_path = "https://en.wikipedia.org/"
movie_info_list = []
for index, movie in enumerate(movies):
    try:
        relative_path = movie['href']
        full_path = base_path + relative_path
        title = movie['title']
        
        movie_info_list.append(get_info_box(full_path))
    except Exception as e:
        print(movie.get_text())
        print(e)

# change run time to ints
for movie in movie_info_list:
    movie['Running time (int)'] = minute_to_int(movie.get('Running time', 'N/A'))
    movie['Budget (float)'] = money_conversion(movie.get('Budget', "N/A"))
    movie['Box office (float)'] = money_conversion(movie.get('Box office', "N/A"))
    movie['Release date (datetime)'] = date_conversion(movie.get('Release date', 'N/A'))

for movie in movie_info_list:
    title = movie['title']
    omdb_info = get_omdb_info(title)
    movie['imdb'] = omdb_info.get('imdbRating', None)
    movie['metascore'] = omdb_info.get('Metascore', None)
    movie['rotten_tomatoes'] = get_rotten_tomato_score(omdb_info)

save_data_pickle("data_clean.pickle", movie_info_list)
movie_info_list = load_data_pickle('data_clean.pickle')

movie_info_copy = [movie.copy() for movie in movie_info_list]

for movie in movie_info_copy:
    current_date = movie['Release date (datetime)']
    if current_date:
        movie['Release date (datetime)'] = current_date.strftime("%B %d, %Y")
    else:
        movie['Release date (datetime)'] = None

save_data("disney_data_final.json", movie_info_copy)

# pandas for csv
df = pd.DataFrame(movie_info_list)
df.to_csv('movielist.csv')
