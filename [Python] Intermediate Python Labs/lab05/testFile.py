#testFile

from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection


#Test Book
def test_book():
    book = Book("I LOVE CS9", "Leo Lu", 2022)
    assert book.getTitle() == "I LOVE CS9"
    assert book.getAuthor() == "Leo Lu"
    assert book.getYear() == 2022
    assert book.getBookDetails() == "Title: I LOVE CS9, Author: Leo Lu, Year: 2022"
    book2 = Book("I LOVE CS9 TOO", "Leo Lu2", 2023)
    assert book2 > book

# Test BookCollectionNode
def test_bookcollectionnode():
    book = Book("ABook", "Someone", 2022)
    node = BookCollectionNode(book)
    assert node.getData() == book
    assert node.getNext() is None
    book2 = Book("ABook2", "Someone2", 2023)
    node2 = BookCollectionNode(book2)
    node.setNext(node2)
    assert node.getNext() == node2

# Test the BookCollection
def test_bookcollection():
    bookcollect = BookCollection()
    assert bookcollect.isEmpty()
    book1 = Book("Title1", "Author1", 2021)
    book2 = Book("Title2", "Author2", 2022)
    book3 = Book("Title3", "Author3", 2023)
    bookcollect.insertBook(book2)
    bookcollect.insertBook(book1)
    bookcollect.insertBook(book3)
    assert bookcollect.getNumberOfBooks() == 3

    # Test getBooksByAuthor
    assert bookcollect.getBooksByAuthor("Author2") == "Title: Title2, Author: Author2, Year: 2022\n"
    assert bookcollect.getBooksByAuthor("Author4") == ""

    # Test getAllBooksInCollection
    expected_output = "Title: Title1, Author: Author1, Year: 2021\nTitle: Title2, Author: Author2, Year: 2022\nTitle: Title3, Author: Author3, Year: 2023\n"
    assert bookcollect.getAllBooksInCollection() == expected_output

    # Test removeAuthor
    bookcollect.removeAuthor("Author2")
    assert bookcollect.getNumberOfBooks() == 2
    assert bookcollect.getBooksByAuthor("Author2") == ""

    # Test recursiveSearchTitle
    assert bookcollect.recursiveSearchTitle("Title1", bookcollect.head)
    assert not bookcollect.recursiveSearchTitle("Title4", bookcollect.head)

