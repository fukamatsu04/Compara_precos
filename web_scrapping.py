from playwright.sync_api import sync_playwright
from carrefour_data import search_url
from bs4 import BeautifulSoup


url = search_url()

class StartPlayWright:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(2000)
        page.click('button.css-161xdxb')
        #page.click('.searchPickupPointsSelect')
        page.wait_for_timeout(2000)
        page.fill('input[name="zipcode"]', '03024-000')
        page.wait_for_timeout(2000)
        page.click('button.css-1r30hpz')
        page.wait_for_timeout(2000)
        # Content of the page.
        content = page.content()
        page.wait_for_timeout(2000)
        browser.close()

StartPlayWright()

content = StartPlayWright.content
soup = BeautifulSoup(content, "html.parser")
title = soup.find_all("h3", "css-1rgidqc")
price = soup.find_all("div", "css-1xc4ph5")

titleLoop = [titles.text for titles in title]
priceLoop = [prices.text for prices in price]

print(priceLoop)

#print(StartPlayWirght.content)




