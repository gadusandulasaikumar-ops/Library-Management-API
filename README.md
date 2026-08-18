# Library-Management-API
 Library Management REST API built with Python and FastAPI.
his is my first project using FastAPI.

I built this project while learning how REST APIs work with FastAPI. The project is a simple library management system where I can manage books and members.

What I Learned From This Project

While building this project, I practiced:

FastAPI routes
GET, POST, PUT and DELETE methods
Pydantic BaseModel
Request body validation
Path parameters
Working with lists as temporary data storage
Using loops to find a particular book or member
Using enumerate() to update and delete items
Basic CRUD operations
What the API Can Do
Books
View all books
Add a new book
Update an existing book
Delete a book
Members
View all members
Add a new member
Update an existing member
Delete a member
API Endpoints
Books
Method	Endpoint	Description
GET	/library/books	Get all books
POST	/library/books	Add a new book
PUT	/library/books/{book_id}	Update a book
DELETE	/library/books/{book_id}	Delete a book
Members
Method	Endpoint	Description
GET	/library/members	Get all members
POST	/library/members	Add a new member
PUT	/library/members/{member_id}	Update a member
DELETE	/library/members/{member_id}	Delete a member
Technologies Used
Python
FastAPI
Pydantic
Uvicorn
How to Run

First install the required packages:

pip install fastapi uvicorn

Then start the server:

uvicorn library_management:app --reload

Open Swagger UI in the browser:

http://127.0.0.1:8000/docs
Note

This project currently uses Python lists as an in-memory database.

That means the data will be lost when the server is stopped. I built it this way intentionally while learning the FastAPI CRUD fundamentals.

This is my first FastAPI project, and I plan to improve it later by connecting it to a real database.
