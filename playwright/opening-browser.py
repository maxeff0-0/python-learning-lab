from playwright.sync_api import sync_playwright
# sync_playwright is used to interact with browsers in a synchronous way(line waits until previous lines are complete)

pw = sync_playwright().start()
# initializing the playwright environment

browser = pw.chromium.launch(
    headless=False,
    slow_mo=2000
)
# chromium -> chrome, headless is set to 'False' when we need to see whats happening, and slow_mo makes sure the browser closes after specified milliseconds

page = browser.new_page()
# new web page
page.goto("http://google.com")
# page is directed to specified url
print(page.content())
# prints the content of the page in HTML format
print("\n\nTitle of the page: ")
print(page.title())
# prints the title of the web page
browser.close()
# closes the browser object