# qa_python
    def test_add_new_book_add_two_books(self):

        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(self.collector.get_books_genre()) == 2

    def test_set_book_genre_add_wrong_genre(self):
        self.collector.set_book_genre('Колобок', 'Эротика')

        assert self.collector.books_genre['Колобок'] == ''

    def test_get_book_genre_add_book_with_genre(self, genre_book):

        assert self.collector.books_genre.get('Колобок') == 'Ужасы'

    def test_get_books_with_specific_genre_if_genre_not_in_self_genre(self, genre_book):

        self.collector.get_books_with_specific_genre('Эротика')

        assert len(self.collector.get_books_with_specific_genre('Эротика')) == 0

    def test_get_books_genre_add_book_with_genre(self, genre_book):

        assert self.collector.get_books_genre() == {'Колобок': 'Ужасы'}

    def test_get_books_for_children_if_genre_not_for_children(self, genre_book):

        assert len(self.collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_if_name_not_in_books_genre(self, genre_book):

        self.collector.add_book_in_favorites('Москау')

        assert len(self.collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_if_book_in_favorites(self, genre_book):

        self.collector.add_book_in_favorites('Колобок')

        self.collector.delete_book_from_favorites('Колобок')

        assert 'Колобок' not in self.collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_book(self, genre_book):

        self.collector.add_book_in_favorites('Колобок')

        assert len(self.collector.get_list_of_favorites_books()) > 0