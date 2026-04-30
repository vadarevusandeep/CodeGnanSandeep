'''
import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[43,62,86],color = "grey" )
plt.title("car sales")
plt.xlabel("years")
plt.ylabel(" No of cars sold")
plt.show()

import matplotlib.pyplot as plt
plt.pie([40,15,25,30],labels=["frontend","backend","database","datasets"])
plt.title("Major project")
plt.legend(["sandeep","vasu","deepak","sai"])
plt.show()

import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[200,400,100,800],color = "pink",s=100)
plt.title("Swift car sales")
plt.xlabel("years")
plt.ylabel("Number of Sales")
plt.show()

import matplotlib.pyplot as plt
plt.bar(["book1","book2","book3","book4"],[200,400,800,600])
plt.title("Book Sales")
plt.xlabel("books")
plt.ylabel("prices")
plt.show()
'''


#web Scrapping
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

# Step 1: Web Scraping
url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = "utf-8"
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("❌ Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

names = []
prices = []
prices_with_symbol = []

for book in books:
    name = book.h3.a["title"]

    price_text = book.find("p", class_="price_color").text
    price = float(re.findall(r"\d+\.\d+", price_text)[0])

    price_symbol = "₹" + str(price)

    names.append(name)
    prices.append(price)
    prices_with_symbol.append(price_symbol)

# Step 2: Create DataFrame
df = pd.DataFrame({
    "Book Name": names,
    "Price": prices_with_symbol
})

print("\n📊 Table Data:\n")
print(df.head())

# Step 3: Save to CSV
df.to_csv("books_data.csv", index=False)
print("\n✅ CSV file 'books_data.csv' created successfully!")

# Step 4: Data Visualization
plt.figure(figsize=(10, 5))
plt.bar(names[:10], prices[:10])   # Top 10 books
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.tight_layout()
plt.show()
