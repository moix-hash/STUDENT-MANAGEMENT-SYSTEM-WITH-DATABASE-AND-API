#  Student Management API

A simple **CRUD REST API** built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

---

##  Project Structure

```
project/
├── main.py          # FastAPI application and API endpoints
├── database.py      # SQLAlchemy engine and session configuration
├── models.py        # Database table definitions (ORM)
├── schemas.py       # Pydantic models for data validation
├── requirements.txt # Project dependencies
└── students.db      # SQLite database (auto-generated on first run)
```

---

##  Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
uvicorn main:app --reload
```

### 3. Open Interactive API Docs
Visit in your browser:
```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

| Method   | Endpoint                  | Description              |
|----------|---------------------------|--------------------------|
| `POST`   | `/create-student/`        | Create a new student     |
| `GET`    | `/students-all/`          | Get all students         |
| `GET`    | `/student/{id}`           | Get student by ID        |
| `PUT`    | `/update-students/{id}`   | Update student by ID     |
| `DELETE` | `/delete-students/{id}`   | Delete student by ID     |

---

##  Request Body (Create / Update)

```json
{
  "name": "Ali Hassan",
  "email": "ali@example.com",
  "age": 21,
  "course": "Computer Science"
}
```

### Validation Rules:
- `email` → must be a valid email format (unique per student)
- `age` → must be a **positive integer** (greater than 0)

---

##  Example Responses

### Create Student — `POST /create-student/`
```json
{
  "id": 1,
  "name": "Ali Hassan",
  "email": "ali@example.com",
  "age": 21,
  "course": "Computer Science"
}
```

### Delete Student — `DELETE /delete-students/1`
```json
{
  "message": "Student deleted successfully"
}
```

### Error — Student Not Found
```json
{
  "detail": "Student not found"
}
```

### Error — Duplicate Email
```json
{
  "detail": "Email already registered"
}
```

---

## 🛠 Tech Stack

- **FastAPI** — Modern, fast web framework
- **SQLAlchemy** — ORM for database operations
- **SQLite** — Lightweight local database
- **Pydantic** — Data validation & serialization
- **Uvicorn** — ASGI server
