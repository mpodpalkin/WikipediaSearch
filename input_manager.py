class InputManager:
    def get_query(self) -> str:
        while True:
            query = input("\nВведите поисковый запрос (или 'выход' для завершения): ").strip()
            if query.lower() in ('выход', 'exit', 'q'):
                return ""
            if query:
                return query
            print("Запрос не может быть пустым. Попробуйте снова.")

    def get_choice(self, max_options: int) -> int:
        while True:
            choice_str = input(f"Введите номер статьи (1-{max_options}) для открытия, 0 для возврата к поиску или 'выход' для завершения: ").strip()
            if choice_str.lower() in ('выход', 'exit', 'q'):
                return -1
            if choice_str == '0':
                return 0
            try:
                choice = int(choice_str)
                if 1 <= choice <= max_options:
                    return choice
                print(f"Некорректный выбор. Введите число от 1 до {max_options}.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")