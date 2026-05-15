from fastapi import  HTTPException, Query , APIRouter
from app.database import books_collection
from app.models import Book


router = APIRouter()

def get_next_id():
    last_book = books_collection.find_one(sort=[("id", -1)])
    if last_book is None:
        return 1
    return last_book["id"] + 1



@router.post("/books")
def adding_new_book_in_the_store_databse(book: Book):
    new_book = {
        "id": get_next_id(),
        "title": book.title,
        "author": book.author,
        "category" :book.category,
        "available_status" : book.available_status,
        "price": book.price
    }
    books_collection.insert_one(new_book)
    new_book.pop("_id")  
    return {"book": new_book, "message": "Book added to the Database of the Store successfully", }



@router.get("/books/{book_id}")
def getting_book_by_id(book_id: int ):
    book = books_collection.find_one({"id": book_id})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found in the Store Database")
    if not book.get("available_status", True):
        book["detail"] = "This book is currently not available in our Store"
    else:
        book["detail"] = "This book is currently available in our Store"
    book.pop("_id")
    return book



@router.get("/books")
def gettting_books_by_author(author : str = Query(None, description="Filtering the books by using the author name")):
    books = list(books_collection.find({"author": author}))
    if not books:
        raise HTTPException(status_code=404, detail="Given author name is not found please check whether you have entered the correct name or check your spelling")
    for book in books:
        book.pop("_id")
    return books