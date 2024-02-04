from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_add_wrong_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Эротика')

        assert collector.books_genre['Колобок'] == ''

    def test_get_book_genre_add_book_with_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Ужасы')

        assert collector.books_genre.get('Колобок') == 'Ужасы'