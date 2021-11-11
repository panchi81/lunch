#! .venv\Scripts\python.exe

# https://www.youtube.com/watch?v=XVv6mJpFOb0

from bs4 import BeautifulSoup as BS
import requests
from datetime import datetime, date


def week_no():
    year, week, day = date.isocalendar(datetime.today())


def weekday():
    return {1: "måndag", 2: "tisdag", 3: "onsdag", 4: "torsdag", 5: "fredag"}


def main():
    urls = [
        "https://www.restaurangspill.se/",
        "https://storavarvsgatan6.se/meny.html",
    ]

    print(spill(get_html(urls[0])))
    print(stora_varvsg(get_html(urls[1])))


def get_html(url: str) -> BS:
    """
    Request page and return a BeautifulSoup object

    Args:
        url (str): Lunch menu url

    Returns:
        BS: Lunch Menu
    """
    page_req = requests.get(url)
    if page_req.status_code != 200:
        raise IOError(f"Bad HTTP response code {page_req.status_code}")

    return BS(page_req.text, "lxml")


def spill(soup: BS):
    # spill_soup = BS(requests.get(urls[0]).content, "html.parser")
    spill_meat = soup.find_all("p", text=True)
    spill_veg = soup.find("span", text=True)

    spill = [text.get_text(strip=True) for text in spill_meat[:3]]
    spill.insert(2, spill_veg.text)
    return spill


def stora_varvsg(soup: BS):
    # mec_soup = BS(requests.get(urls[1]).content, "lxml")
    # mec_soup = BS(requests.get(urls[1]).text, "lxml")
    # mec_main = soup.find_all("span", text=True)

    # Cleanup wonderfully broken html (linebreaks and characters).
    for linebreak in soup.find_all("br"):
        linebreak.extract()

    # Gather the mec-menu
    return [
        t.get_text(strip=True)
        for t in soup.find_all("span", text=True)[11:43]
        if t.get_text(strip=True)
    ]

    # mec = [t.text for t in mec_main if "\xa0" not in t]
    # # text = [x.get_text() for x in tag]


if __name__ == "__main__":
    main()
