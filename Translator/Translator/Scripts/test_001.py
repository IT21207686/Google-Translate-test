#import random
#from random import randint
#from Browser_Helper import login
#from Helper import read_json

from playwright.sync_api import sync_playwright

def test_execute():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://translate.google.com")

        #page.pause()

        page.get_by_role("combobox", name="Source text").click()
        page.get_by_role("combobox", name="Source text").fill("welcome")
        page.get_by_role("button", name="More target languages").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name="Sinhala").get_by_text("Sinhala").click()
        
        #page.pause()
        

        
        

        #page.pause()
        page.wait_for_timeout(4000)