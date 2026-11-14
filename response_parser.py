import json
from typing import List
from article import Article


class ResponseParser:
    def parse(self, json_response: str) -> List[Article]:
        try:
            data = json.loads(json_response)
            search_results = data.get("query", {}).get("search", [])

            articles = []
            for item in search_results:
                articles.append(Article(
                    page_id=item.get("pageid"),
                    title=item.get("title"),
                    snippet=item.get("snippet")
                ))
            return articles
        except json.JSONDecodeError:
            raise ValueError("Ошибка разбора JSON-ответа от сервера.")
        except KeyError as e:
            raise ValueError(f"Неожиданная структура ответа: отсутствует ключ {e}")