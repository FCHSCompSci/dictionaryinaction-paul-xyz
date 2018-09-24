## Paul Brown
## Book Library(Using Dictionary)
## 09/24/2018

library = []

def make_book(title, author, genre, book_id):
    library_book = {
        'book_id': book_id,
        'title': title,
        'author': author,
        'genre': genre,
    }
    library.append(library_book)
    return library

book_id = 0

name = input('What is your name? ')
print('Welcome to the library %s' % (name))

while True:
    interface_book = input("Do you want to [A]dd a new book, [R]emove a book, or [L]eave, or [C]heck the books in the library?")
    if interface_book == 'A':
        title = input('What is the title of your book?  ')
        author = input('Who is the author of your book?  ')
        genre = input('What is the genre of the book?  ')
        book_id = book_id + 1
        add_book2 = make_book(title, author, genre, book_id)

    if interface_book == 'C':
        print(library)

    if interface_book == 'R':
        print(library)
        id_checker = input('What book ID will be removed? ')
        for dictionary in library:
            if dictionary['book_id'] == id_checker:
                library.remove(dictionary)
        print(library)

    if interface_book == 'L':
    exit()
    
