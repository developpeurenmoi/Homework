import requests
from bs4 import BeautifulSoup as bs
import csv

file = open("movie.csv", mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["제목", "평점", "포스터",
                "감독", "출연진", "장르|상영시간|개봉일자"])
url = 'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(url)
movie_soup = bs(movie_html.text, "html.parser")
movie_big_box = movie_soup.find('ul', {"class": "lst_detail_t1"})
movie_list = movie_big_box.find_all('li')
final_reuslt = []
for info in movie_list:
    title = info.find('dl', {"class": "lst_dsc"}).find(
        'dt', {"class": "tit"}).find('a').text
    star = info.find('dl', {"class": "lst_dsc"}).find('dd', {"class": "star"}).find(
        'dl', {"class": "info_star"}).find('dd').find('div', {"class": "star_t1"}).find('span', {"class": "num"}).text
    img_src = info.find("div", {"class": "thumb"}).find('a').find('img')['src']
    director = info.find("dl", {"class": "lst_dsc"}).find(
        'dl', {"class": "info_txt1"}).find_all('dd')[1].find('a').text
    actors = info.find('dl', {"class": "lst_dsc"}).find('dl', {
        "class": "info_txt1"}).find_all('dd')[-1].find('span', {"class": "link_txt"}).text.replace('\r', '').replace('\t', '').replace('\n', '')
    published_date = info.find('dl', {"class": "lst_dsc"}).find(
        'dl', {"class": "info_txt1"}).find_all('dd')[0].text.replace('\r', '').replace('\t', '').replace('\n', '')
    movie_info = {
        "제목": title,
        "평점": star,
        "포스터": img_src,
        "감독": director,
        "출연진": actors,
        "장르|상영시간|개봉일자": published_date}
    final_reuslt.append(movie_info)

for result in final_reuslt:
    row = []
    row.append(result['제목'])
    row.append(result['평점'])
    row.append(result['포스터'])
    row.append(result['감독'])
    row.append(result['출연진'])
    row.append(result['장르|상영시간|개봉일자'])
    writer.writerow(row)


file.close()