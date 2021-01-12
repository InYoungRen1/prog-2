# massloader.py
# downloads ALL xkcd comics to disk

import os
import requests
import bs4

url = "https://xkcd.com" # starting url

# create a folder/directory to store comics
os.makedirs("xkcd images", exist_ok=True)

# Loop until url DOES NOW ends with a "#"

while not url.endswith("#"):
    # TODO: download the html
    print(f"Dpwnload page {url}...")
    res = requests.get(url)
    res.raise_for_status() # STOP if there's an error
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # TODO: download the html
    comic_elem = soup.select("#comic img")
    if comic_elem == [] or comic_elem
        print("Couldn't find image.....")
    else:
        comic_url = "https:" + comic_elem[0].get("src")
        print(f"*\tDownloading image {comic_url}.....")

        # Downloading the image
        res = requests.get(comic_url)
        res.raise_for_status()


    # TODO: save the image to disk
    image_file = open(os.path.join("xkcdimages", os.path.basename(comic.url)), "wb")
    for chunk in res.iter_content(1000000):
        image_file_write(chunk)
    image_file.close()
    # Get the Prev button" URL
    prev_link = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prev_link.get("href")