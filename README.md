# qa_python
    def test_add_new_book_add_two_books(self, collector, new_book):

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_add_wrong_genre(self, collector, new_book, correct, incorrect):

        collector.set_book_genre(correct.name, incorrect.genre)

        assert collector.get_book_genre(correct.name) != incorrect.genre

    def test_get_book_genre_add_book_with_genre(self, collector, new_book, genre_book, correct):

        assert collector.get_book_genre(correct.name) == correct.genre

    def test_get_books_with_specific_genre_if_genre_not_in_self_genre(self, collector, new_book, genre_book, incorrect):

        assert len(collector.get_books_with_specific_genre(incorrect.genre)) == 0

    def test_get_books_genre_add_book_with_genre(self, collector, new_book, genre_book, correct):

        assert collector.get_books_genre() == {correct.name: correct.genre}

    def test_get_books_for_children_if_genre_not_for_children(self, collector, new_book, genre_book):

        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_if_name_not_in_books_genre(self, collector, new_book, genre_book, incorrect):

        collector.add_book_in_favorites(incorrect.name)

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_if_book_in_favorites(self, collector, new_book, genre_book, favorite_book,
                                                             correct):

        collector.delete_book_from_favorites(correct.name)

        assert correct.name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_book(self, collector, new_book, genre_book, favorite_book):

        assert len(collector.get_list_of_favorites_books()) > 0