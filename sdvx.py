import requests
from bs4 import BeautifulSoup
import json

song = {}

for i in range(1, 21):  # level
    row = {i: {}}
    song.update(row)
    j = 1  # page
    while True:
        url = f"https://p.eagate.573.jp/game/sdvx/vi/music/index.html?page={j}&search_level={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        music_elements = soup.select("div.music")
        if not music_elements:
            break
        index = 0
        for element in music_elements:
            title_element = element.select_one("div.cat > div.inner > div.info > p:first-child")
            title = title_element.text
            artist_element = element.select_one("div.cat > div.inner > div.info > p:nth-of-type(2)")
            artist = artist_element.text
            jacket_element = element.select_one("div.cat > div.jk img")
            jacket = jacket_element['src']
            song[i][index] = {"title": title, "artist": artist, "jacket": "https://p.eagate.573.jp"+jacket}
            index += 1
        j += 1
    with open("./song.json", 'w', encoding='utf-8') as file:
        json.dump(song, file, ensure_ascii=False, indent="\t")
    print("------end of level", i, "------")