from playwright.sync_api import sync_playwright
import re

pw = sync_playwright().start()

browser = pw.chromium.launch()

page = browser.new_page()
page.goto("https://www.wikipedia.org")

print(page.title())
searchItem = input("\nEnter topic to search: ")

page.get_by_role("searchbox", name="search").fill(searchItem)
# gets the html object by its type and name and then fills it with the user input

submit_btn = page.locator(".pure-button.pure-button-primary-progressive")
# locates the button by the specified class

submit_btn.click()
# clicks the button

#page.screenshot(path="screenshots/pic.png")

print("Searching...")
page.wait_for_load_state("networkidle")
# waits till network becomes idle .i.e finished searching

paras = page.locator(".mw-heading.mw-heading2 > h2, .mw-heading.mw-heading3 > h3, .mw-content-ltr.mw-parser-output > p, .mw-content-ltr.mw-parser-output > ul > li")

for para in range(paras.count()):
    text = paras.nth(para)
    tag = text.evaluate("el => el.tagName")
    text = text.text_content().strip()
    text = re.sub(r"\[\d+\]", "", text)
    if text:
        if tag == "H2":
            print("\n")
            print(f"===={text}====")
        elif tag == "H3":
            print("\n")
            print(f"----{text}----")
        elif tag == "LI":
            print("*", text)
        else:
            print("\n")
            print(text)

        
browser.close()