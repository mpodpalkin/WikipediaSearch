import html
from typing import List
from article import Article


class DisplayManager:
    def show_results(self, articles: List[Article]) -> None:
        if not articles:
            print("По вашему запросу ничего не найдено.")
            return

        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТЫ ПОИСКА")
        print("=" * 50)
        for idx, article in enumerate(articles, start=1):
            clean_snippet = html.unescape(article.snippet)
            clean_snippet = clean_snippet.replace('<span class="searchmatch">', '').replace('</span>', '')

            print(f"{idx}. {article.title}")
            print(f"   {clean_snippet[:150]}...")
        print("=" * 50)