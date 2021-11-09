#! .venv\Scripts\python.exe

# https://www.youtube.com/watch?v=XVv6mJpFOb0

from bs4 import BeautifulSoup
import requests


def main():
    urls = [
        "https://www.restaurangspill.se/",
        "https://storavarvsgatan6.se/meny.html",
    ]

    # spill_soup = BeautifulSoup(requests.get(urls[0]).content, "html.parser")
    # spill_main = spill_soup.find_all("p", text=True)
    # spill_veg = spill_soup.find("span", text=True)

    # spill = [text.text for text in spill_main[:3]]
    # spill.insert(2, spill_veg.text)

    # print(spill)

    mec_soup = BeautifulSoup(requests.get(urls[1]).content, "lxml")
    # # mec_soup = BeautifulSoup(requests.get(urls[1]).content, "html.parser")
    # mec_main = mec_soup.find_all("span", text=True)
    mec = [
        t.text.strip() for t in mec_soup.find_all("span", text=True) if t.text.strip()
    ]
    # # mec = [t.text for t in mec_main if "\xa0" not in t]
    print(mec)

    # # text = [x.get_text() for x in tag]
    # # print(text)


if __name__ == "__main__":
    main()
