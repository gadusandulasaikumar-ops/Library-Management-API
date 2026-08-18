#this is the library management project and first project in the fastapi
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app= FastAPI()

class Book(BaseModel):
    id:int
    title:str
    author:str
    genre:str
    price:int
    available_copies:int
class Member(BaseModel):
    id:int
    name:str
    email:str 
    borrowed_books : list[int]
books = []
members = []

#creating the get end point (reading the books)
@app.get("/library/books")
def read_books():
    return books 

#creating the book post end point (creating the books)
@app.post("/library/books")
def create_book(book:Book):
    books.append(book)
    return {
        "message":"the book createded successfully",
        "data":book
    }

#creating the member get end point (reading the members)
@app.get("/library/members")
def read_member():
    return members

#creating the members post end poind(creating new members)
@app.post("/library/members")
def create_member(member:Member):
    members.append(member)
    return {
        "message":"the member created successfully",
        "data": member
    }

#updatgin the books by put end point 
@app.put("/library/books/{book_id}")
def update_book(book_id:int,updated:Book):
    for index,book in enumerate(books):
        if book.id == book_id:
            books[index] = updated
            return {
                "message":"book updated",
                "data":updated
            }
#updating the members by put end point
@app.put("/library/members/{member_id}")
def update_member(member_id:int,update:Member):
    for index,member in enumerate(members):
        if member.id == member_id:
            members[index] = update
            return {
                "message":"member updated successfully ",
                "data":update
            }
    return {"member not found"}
#deleteing the book by delete end point
@app.delete("/library/books/{book_id}")
def delete_book(book_id:int):
    for index,book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {
                "message":"book delete successfully"
            }
#deleting the member by delete end point
@app.delete("/library/members/{member_id}")
def delete_member(member_id:int):
    for index,member in enumerate(members):
        if member.id == member_id:
            members.pop(index)
            return {
                "message":"member deleted successfully"
            }