# Spy Cat Agency API

A RESTful API for managing spy cats, their missions, and targets. This project was created as a technical assessment.

**Stack:** FastAPI, SQLAlchemy (with Asyncio), Pydantic, Alembic.

---

## Core Features

* **Cat Management:** Create, view, update salary, and delete spy cats. Each cat's breed is validated through the external service [TheCatAPI](https://thecatapi.com/).
* **Mission Management:** Create missions along with their targets (from 1 to 3), assign cats to missions, view, and delete them.
* **Target Management:** Update the notes and status of targets.
* **Business Logic Highlights:**
    * A cat cannot be on more than one mission at a time.
    * A mission with an assigned cat cannot be deleted.
    * Notes are "frozen" (cannot be edited) if the target or the entire mission is completed.
    * A mission is automatically marked as completed once all of its targets are completed.

---

## Setup and Launch

### 1. Clone the repository

```bash
git clone [https://github.com/dmalanchuk/SpyCats.git](https://github.com/dmalanchuk/SpyCats.git)
cd SpyCats 
```

### 2. Create the virtual environment
    python -m venv .venv

Activate on macOS/Linux
    source .venv/bin/activate

Activate on Windows
    .\.venv\Scripts\activate

### 3. Install the dependencies
    pip install -r requirements.txt

### 4. Generate a new migration (if you change the models)
    alembic revision --autogenerate -m "Initial migration"

Apply the migrations to the database
    alembic upgrade head

### 5. Run the server
    uvicorn main:app --reload

The server will be available at http://127.0.0.1:8000. 
Interactive OpenAPI (Swagger) documentation is available at http://127.0.0.1:8000/docs.


### 6. Postman

For convenient API testing, you can use the Postman collection.

[[Link to Postman Collection](https://dmalanchuk-4280652.postman.co/workspace/Daniil-Marysyk's-Workspace~6f8e3054-1e3c-4d50-8ec6-1188838fe77b/collection/48084872-ec95f4c7-bfe2-40d4-9732-1fa8a35f64a2?action=share&creator=48084872)]