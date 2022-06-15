
from playwright.sync_api import sync_playwright
import carrefour_data

class StartPlayWirght(url, cep):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(2000)
        page.click('button.css-161xdxb')
        #page.click('.searchPickupPointsSelect')
        page.wait_for_timeout(2000)
        page.fill('input[name="zipcode"]', cep)
        page.wait_for_timeout(2000)
        page.click('button.css-1r30hpz')
        page.wait_for_timeout(2000)
        print(page.title())
        browser.close()

StartPlayWirght()
"""
class StartPlayWirght:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://mercado.carrefour.com.br/")
        page.wait_for_timeout(2000)
        page.click('button.css-161xdxb')
        #page.click('.searchPickupPointsSelect')
        page.wait_for_timeout(2000)
        page.fill('input[name="zipcode"]', '03024000')
        page.wait_for_timeout(2000)
        page.click('button.css-1r30hpz')
        page.wait_for_timeout(2000)
        print(page.title())
        browser.close()

StartPlayWirght()

"""