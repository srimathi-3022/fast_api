from fastapi import FastAPI, HTTPException
from models import Book
from database import books_collection
import uvicorn

app = FastAPI()

@app.get("/books")
def get_next_id():
    last_book = books_collection.find_one(sort=[("id", -1)])
    if last_book is None:
        return 1
    return last_book["id"] + 1


@app.post("/books")
def create_book(book: Book):
    new_book = {
        "id": get_next_id(),
        "title": book.title,
        "author": book.author,
        "price": book.price
    }
    books_collection.insert_one(new_book)
    new_book.pop("_id")  
    return {"message": "Book added to the Database  successfully", "book": new_book}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = books_collection.find_one({"id": book_id})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found in the Database")
    book.pop("_id")
    return book


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)