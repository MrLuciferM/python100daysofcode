from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.esquire.com/entertainment/movies/g226/best-movies-ever-0609/"

response = requests.get(WEBSITE)
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")

moviename_tags = soup.findAll(name="span", class_="listicle-slide-hed-text")
movies = [span.getText() for span in moviename_tags]

# print(movies)
entries = [f"{i+1}.) {movies[i]}\n" for i in range(len(movies))]

with open("movieslist.txt", "w") as file:
    file.writelines(entries)
