import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

data = []

for q in quotes:
    text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text
    data.append([text, author])

# Save to CSV
with open("quotes_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(data)

print("Scraping completed. Data saved to quotes_dataset.csv")