import pytest

from main import BooksCollector


class Book:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre


@pytest.fixture
def correct():
    return Book('Колобок', 'Ужасы')


@pytest.fixture
def incorrect():
    return Book('Москау', 'Эротика')


@pytest.fixture(scope='function')
def collector():
    return BooksCollector()


@pytest.fixture(scope='function')
def new_book(collector, correct):
    return collector.add_new_book(correct.name)


@pytest.fixture(scope='function')
def genre_book(collector, correct):
    return collector.set_book_genre(correct.name, correct.genre)


@pytest.fixture(scope='function')
def favorite_book(collector, correct):
    return collector.add_book_in_favorites(correct.name)
