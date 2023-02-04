class BookShelf:
  def __init__(self, *books):
    self.books = books

  
  def __str__(self):
    return f"Bookshelf with {len(self.books)} books."


class Book():
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Book {self.name}"

book = Book("Harry Potter")
book1 = Book("python 101")

shelf = BookShelf(book, book1)

print(shelf)