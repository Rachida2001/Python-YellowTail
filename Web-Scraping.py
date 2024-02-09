import requests
import os
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
HEADERS = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=HEADERS)

if page.status_code != 200:
    print("Unable to find URL")
else:
    soup = BeautifulSoup(page.content, "html.parser")
    titles = soup.find_all('div', {'class': 'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title'})
    
    base_url = "https://www.imdb.com"
    for title in titles:
        movie_title = title.a.text.split(".", 1)[1].strip()
        try:
            os.makedirs("Reviews", exist_ok=True)
            with open("Reviews/{}.txt".format(movie_title), 'w', encoding='utf-8') as f:
                movie_details_url = "{}{}".format(base_url, title.a['href'])
                movie_page = requests.get(movie_details_url, headers=HEADERS)
                soup = BeautifulSoup(movie_page.content, "html.parser")
                
                ipc_link = soup.find_all('a', {'class': 'ipc-link ipc-link--baseAlt ipc-link--inherit-color'})
                for r in ipc_link:
                    if r.text == "User reviews":
                        review_link = r['href']
                
                all_reviews_page = requests.get("{}/{}".format(base_url, review_link))
                soup = BeautifulSoup(all_reviews_page.content, "html.parser")
                reviews = soup.find_all('div', {'class': 'text show-more__control'})
                
                print('Recording reviews for {}...'.format(movie_title))
                for review in reviews:
                    comment = review.text
                    f.write(comment + "\n")
        except Exception as e:
            print("Error:", e)
