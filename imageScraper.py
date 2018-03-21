import image_scraper
import pandas as pd
import urllib


df = pd.read_csv("../../processed/simplified_artwork_data.csv")
base="http://www.tate.org.uk/art/images/work/"


df.dropna(axis=0, how='any')
for index, item in df.iterrows():
    url = item["thumbnailUrl"]
    if(type(url) == float):
        continue
    urllib.urlretrieve(str(base + url), str(index) + ".jpg")
    # image_scraper.scrape_images(str(base + url))
