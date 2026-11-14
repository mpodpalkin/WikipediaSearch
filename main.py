from input_manager import InputManager
from wikipedia_client import WikipediaClient
from response_parser import ResponseParser
from display_manager import DisplayManager
from browser_opener import BrowserOpener


class WikipediaSearchApp:
    def __init__(self):
        self.input_manager = InputManager()
        self.client = WikipediaClient()
        self.parser = ResponseParser()
        self.display = DisplayManager()
        self.browser = BrowserOpener()

    def run(self) -> None:

        while True:
            query = self.input_manager.get_query()
            if not query:
                print("Завершение программы.")
                break

            try:
                print("Выполняется поиск...")
                raw_response = self.client.search(query)
                articles = self.parser.parse(raw_response)

                if not articles:
                    print("Статьи не найдены. Попробуйте изменить запрос.\n")
                    continue

                self.display.show_results(articles)

                while True:
                    choice = self.input_manager.get_choice(len(articles))

                    if choice == -1:
                        print("Завершение программы.")
                        return

                    if choice == 0:
                        print("Возврат к поиску.\n")
                        break

                    selected_article = articles[choice - 1]
                    self.browser.open_article(selected_article.page_id)
                    print("Готово.\n")

            except ConnectionError as e:
                print(f"Ошибка подключения: {e}. Проверьте интернет-соединение.")
            except ValueError as e:
                print(f"Ошибка данных: {e}")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}. Попробуйте снова.")


if __name__ == "__main__":
    app = WikipediaSearchApp()
    app.run()