
# Book Store Management API

A scalable and lightweight RESTful API developed using FastAPI and MongoDB Atlas for managing book records. The application supports book creation and retrieval operations with automatic ID generation and cloud database integration.

# Overview

The Book Store Management API is designed to demonstrate modern backend development practices using FastAPI and MongoDB. The system provides efficient CRUD-ready architecture, schema validation using Pydantic, and secure database connectivity through MongoDB Atlas.

This project follows a modular structure suitable for enterprise-level backend service development and API integration workflows

# MongoDB Atlas Configuration

Create a MongoDB Atlas account
Create a new cluster
Configure database user credentials
Add IP address to network access whitelist
Copy the MongoDB connection string
=======
# Bookstore API Project

## Project Overview

The Bookstore API project is a backend application developed using FastAPI and MongoDB. The application is designed to manage bookstore records through REST API endpoints. It allows users to create, store, retrieve, and filter book details efficiently.

The project demonstrates backend API development concepts such as routing, request handling, response formatting, exception handling, database integration, and modular project structure using FastAPI.

MongoDB is used as the database for storing book information permanently, while Postman is used for API testing.

---

# Objective

The primary objective of this project is to develop a simple and structured Bookstore Management API using FastAPI and MongoDB. The project focuses on implementing REST API concepts, database operations, path parameters, query parameters, and proper error handling.

---

# Technologies Used

The project is developed using the following technologies:

- Python
- FastAPI
- MongoDB
- PyMongo
- Pydantic
- Uvicorn
- Postman

---

# Project Features

The application provides the following features:

- Create and store book records in MongoDB
- Automatically generate unique book IDs
- Retrieve book details using book ID
- Filter books using author name
- Return clean JSON responses
- Handle exceptions using HTTPException
- Display availability status messages
- Modular project structure
- API testing using Postman

---

# Project Structure

The project follows a clean modular folder structure for better maintainability and scalability.

## app/

This folder contains all backend application files.

### main.py

Acts as the entry point of the FastAPI application. It initializes the FastAPI app and connects all routes.

### routes.py

Contains all API endpoints related to bookstore operations such as creating books, fetching books, and filtering books.

### models.py

Defines Pydantic models used for request validation and response structures.

### database.py

Handles MongoDB database connection and collection configuration.

### __init__.py

Marks the app directory as a Python package.

---

# Database

MongoDB is used as the database for storing bookstore records.

The application connects to MongoDB using PyMongo.

Book details such as title, author, price, category, and availability status are stored inside the MongoDB collection.

---

# API Endpoints

## 1. POST Endpoint

The POST API is used to create and store a new book record in MongoDB.

The endpoint accepts the following details:

- Title
- Author
- Price
- Category
- Availability status

After successful insertion, the API returns:

- Success message
- Generated book ID
- Created book details

Status code used:

- 201 Created

---

## 2. GET Endpoint using Path Parameter

This endpoint retrieves book details using the book ID.

The API returns:

- Title
- Author
- Price
- Category
- Availability message

Availability conditions:

- If available is true:
  "Book is available"

- If available is false:
  "Book is not available"

If the provided book ID does not exist, the API returns:

- 404 Not Found

with a proper error message.

---

## 3. GET Endpoint using Query Parameter

This endpoint filters books using author name.

The API returns:

- Total matching books
- List of filtered records

If no records are found, the API returns an appropriate error response.

---

# Postman Testing

Postman is used to test all API endpoints.

Using Postman, the following operations are performed:

- Sending POST requests
- Sending GET requests
- Passing path parameters
- Passing query parameters
- Checking API responses
- Verifying error handling

Postman helps validate whether the API is working correctly with MongoDB integration.

---

# Exception Handling

The application uses FastAPI HTTPException for handling runtime errors and invalid requests.

Examples include:

- Book ID not found
- Empty results
- Invalid request handling

Proper HTTP status codes are used throughout the project.

Common status codes:

- 200 OK
- 201 Created
- 400 Bad Request
- 404 Not Found

---

# Data Types Used

The project demonstrates multiple Python data types.

## String

Used for:

- Title
- Author
- Category

## Integer / Float

Used for:

- Book ID
- Price

## Boolean

Used for:

- Availability status

## List

Used for:

- Returning multiple filtered records

## Dictionary

Used for:

- JSON responses
- MongoDB document structure

---

# Clean Coding Standards

The project follows clean coding practices such as:

- Modular architecture
- Meaningful variable names
- Proper indentation
- Reusable functions
- Structured responses
- Organized routing
- Separation of concerns

---

# Learning Outcomes

This project helps understand the following backend development concepts:

- FastAPI fundamentals
- REST API development
- MongoDB integration
- API routing
- Path parameters
- Query parameters
- Request validation
- Exception handling
- JSON responses
- Postman API testing
- Modular project architecture

---

# Conclusion

The Bookstore API project is a beginner-friendly backend application developed using FastAPI and MongoDB. The project demonstrates how to build REST APIs with proper routing, database integration, validations, and exception handling.

The application provides a strong foundation for learning backend development and can be extended further by adding features such as update/delete operations, authentication, JWT security, pagination, and frontend integration.
>>>>>>> ae3d6c8 (committing the updated version)
