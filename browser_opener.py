import webbrowser

class BrowserOpener:
    def open_article(self, page_id: int) -> None:
        url = f"https://ru.wikipedia.org/w/index.php?curid={page_id}"
        print(f"\nСтатья в браузере: {url}")
        webbrowser.open(url)