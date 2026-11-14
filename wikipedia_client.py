import urllib.request
import urllib.parse
import urllib.error


class WikipediaClient:
    def __init__(self, base_url: str = "https://ru.wikipedia.org/w/api.php"):
        self.base_url = base_url

    def search(self, query: str) -> str:
        # 1. Добавляем кавычки вокруг запроса
        query_with_quotes = f'"{query}"'

        # 2. Кодируем строку (кавычки превратятся в %22, пробелы в %20 и т.д.)
        encoded_query = urllib.parse.quote(query_with_quotes)

        url = f"{self.base_url}?action=query&list=search&utf8=&format=json&srsearch={encoded_query}"

        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Python Wikipedia Search)'})
            with urllib.request.urlopen(req, timeout=10) as response:
                return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            raise ConnectionError(f"Ошибка сети: {e.reason}")
        except TimeoutError:
            raise ConnectionError("Превышено время ожидания ответа от сервера.")
        except Exception as e:
            raise RuntimeError(f"Неизвестная ошибка при запросе: {e}")