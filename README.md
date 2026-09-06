# FastAPI Issue Tracker API

[![CI](https://github.com/bedru-mekiyu/fastapi-issue-tracker/actions/workflows/ci.yml/badge.svg)](https://github.com/bedru-mekiyu/fastapi-issue-tracker/actions/workflows/ci.yml)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=flat&logo=Python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, production-ready RESTful API built with **FastAPI** for managing issues and bug reports. This project showcases core web API engineering practices, including structured endpoint design, request validation using **Pydantic v2**, file-based persistent storage, custom middleware processing, and automated unit testing.

---

## Key Features

- **Full CRUD Support**: Endpoints to create, read, update, and delete issue records.
- **Pydantic Validation**: Strict type enforcement and payload validation for requests and responses.
- **State & Priority Management**: Enums for tracking issue status (`open`, `in_progress`, `closed`) and priority (`low`, `medium`, `high`).
- **File-Based Persistence**: Thread-safe JSON file storage without requiring external database setup.
- **Custom Middleware**: Response timing middleware adding `X-Process-Time` HTTP headers and CORS middleware for frontend integration.
- **Interactive Documentation**: Auto-generated OpenAPI (Swagger UI) and ReDoc interfaces.
- **Automated Testing**: Test suite powered by `pytest` and FastAPI's `TestClient`.

---

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **Testing**: [Pytest](https://docs.pytest.org/) & [HTTPX](https://www.python-httpx.org/)
- **CI/CD**: GitHub Actions

---

## API Architecture & Endpoints

### Endpoint Summary

| Method | Endpoint | Status Code | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/v1/health` | `200 OK` | System health check endpoint |
| `GET` | `/api/v1/issues` | `200 OK` | Retrieve all registered issues |
| `GET` | `/api/v1/issues/{id}` | `200 OK` | Retrieve issue by UUID (404 if not found) |
| `POST` | `/api/v1/issues` | `201 Created` | Create a new issue |
| `PUT` | `/api/v1/issues/{id}` | `200 OK` | Update an existing issue by UUID |
| `DELETE` | `/api/v1/issues/{id}` | `204 No Content` | Remove an issue by UUID |

---

## Project Structure

```text
fastapi-issue-tracker/
├── app/
│   ├── __init__.py
│   ├── schemas.py         # Pydantic schemas for data validation
│   ├── storage.py         # JSON storage layer functions
│   ├── middleware/
│   │   └── timing.py      # Custom request timing middleware
│   └── routes/
│       ├── __init__.py
│       └── issues.py      # API route handlers for issue operations
├── docs/
│   ├── crash_course.md    # FastAPI tutorial notes
│   └── crash_course_excalidraw.png
├── tests/
│   └── test_issues.py     # Unit and integration test suite
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions workflow
├── .gitignore
├── main.py                # FastAPI application entrypoint
├── pytest.ini             # Pytest configuration
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
```

---

## Getting Started

### Prerequisites

- **Python 3.10+**
- `pip` package manager

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bedru-mekiyu/fastapi-issue-tracker.git
   cd fastapi-issue-tracker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the development server:**
   ```bash
   fastapi dev main.py
   # Or using uvicorn directly:
   uvicorn main:app --reload
   ```

5. **Access the API & Documentation:**
   - Base API: `http://127.0.0.1:8000`
   - Interactive Swagger Docs: `http://127.0.0.1:8000/docs`
   - ReDoc Docs: `http://127.0.0.1:8000/redoc`

---

## Testing

Run the test suite using `pytest`:

```bash
pytest
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
