from fastapi import FastAPI

app = FastAPI()

books = [
 {"title": "Дюна",
 "author": "Фрэнк Герберт",
 "genre": "Научная фантастика"},
 {"title": "Интерстеллар",
 "author": "Кип Стивен Торн",
 "genre": "Научная фантастика"},
 {
 "title": "Марсианин",
 "author": "Энди Вейер",
 "genre": "Научная фантастика"}
]

@app.get("/")
def get_info():
    return {
        "message": "API каталога книг",
        "enpoint": "/books",
    }
@app.get("/books")
def get_books():
    return books