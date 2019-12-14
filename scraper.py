import urllib.request
from bs4 import BeautifulSoup

class Scraper:
  # takes the website to scrape as a parameter
  def __init__(self, site):
    self.site = site

  def scrape(self):
    # makes a request to the site and returns response object
    r = urllib.request.urlopen(self.site)
    # returns HTML
    html = r.read()
    parser= "html.parser"
    # parses html
    sp = BeautifulSoup(html, parser)

    # find all a tags then loops over them to get href value of each
    for tag in sp.find_all("a"):
      url = tag.get("href")
      print(url)
      if url is None:
        continue
      if "https" in url:
        print(url)

urls = "https://teamtreehouse.com/"
Scraper(urls).scrape()
