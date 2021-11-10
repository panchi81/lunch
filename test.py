#! .venv\Scripts\python.exe

# https://www.youtube.com/watch?v=XVv6mJpFOb0

from bs4 import BeautifulSoup as BS
import requests


def main():
    urls = [
        "https://www.restaurangspill.se/",
        "https://storavarvsgatan6.se/meny.html",
    ]

    # spill_soup = BS(requests.get(urls[0]).content, "html.parser")
    # spill_main = spill_soup.find_all("p", text=True)
    # spill_veg = spill_soup.find("span", text=True)

    # spill = [text.text for text in spill_main[:3]]
    # spill.insert(2, spill_veg.text)

    # print(spill)

    # mec_soup = BS(requests.get(urls[1]).content, "lxml")
    mec_soup = BS(requests.get(urls[1]).text, "lxml")
    # mec_main = mec_soup.find_all("span", text=True)

    # Cleanup wonderfully broken html (linebreaks and characters).
    for linebreak in mec_soup.find_all("br"):
        linebreak.extract()

    mec_menu = [
        t.text.strip()
        for t in mec_soup.find_all("span", text=True)[11:43]
        if t.text.strip()
    ]
    # # mec = [t.text for t in mec_main if "\xa0" not in t]
    print(mec_menu)

    # # text = [x.get_text() for x in tag]


def get_parser(url: str) -> BS:
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


if __name__ == "__main__":
    main()
