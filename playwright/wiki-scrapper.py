from playwright.sync_api import sync_playwright

pw = sync_playwright().start()

browser = pw.chromium.launch(
    headless=False,
    slow_mo=2000
)

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

page.screenshot(path="screenshots\pic.png")

browser.close()