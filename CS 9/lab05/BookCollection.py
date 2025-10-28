#BookCollection

from Book import Book 
from BookCollectionNode import BookCollectionNode 

class BookCollection:
    def __init__(self):
        self.head = None 
        
    def isEmpty(self):
        return self.head is None
    
    def getNumberOfBooks(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def insertBook(self, book):
        newnode = BookCollectionNode(book)
        current = self.head 
        previous = None
        while current != None and current.getData() < book:
            previous = current
            current = current.getNext()
        if previous == None:
            newnode.setNext(self.head)
            self.head = newnode
        else:
            newnode.setNext(previous.getNext())
            previous.setNext(newnode)
            
    def getBooksByAuthor (self, author):
        current = self.head
        r = ""
        while current != None:
            if current.getData().getAuthor().lower() == author.lower():
                r += current.getData ().getBookDetails() + "\n"
            current = current.getNext()
        return r
    
    def getAllBooksInCollection(self):
        r = ""
        current = self.head
        while current != None:
            r += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return r
    
    def removeAuthor(self, author):
        current = self.head
        previous = None
        while current != None:
            book = current.getData()
            if book.getAuthor().lower() == author.lower():
                if previous != None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                current = current.getNext()
            else:
                previous = current
                current = current.getNext()
            
    def recursiveSearchTitle (self, title, bookNode):
        if bookNode == None:
            return False
        elif bookNode.getData().getTitle().lower() == title.lower():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())
