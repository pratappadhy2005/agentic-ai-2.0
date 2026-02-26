# 6-FAST_API

This project demonstrates a basic FastAPI application structure.

## Project Structure

- `00_Basic/main.py`: Contains a simple FastAPI application with basic endpoints.
- `main.py`: A simple Python script entry point (currently prints a greeting).
- `pyproject.toml`: Project configuration and dependencies managed by `uv`.

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd 6-FAST_API
    ```

2.  Install dependencies using `uv`:
    ```bash
    uv sync
    ```
    Or using pip:
    ```bash
    pip install -r requirements.txt
    # If requirements.txt is not present, install manually:
    pip install fastapi uvicorn pydantic
    ```

## Running the Application

To run the FastAPI application located in `00_Basic/main.py`:

```bash
uv run uvicorn 00_Basic.main:app --reload
```

Or if using standard python/pip:

```bash
uvicorn 00_Basic.main:app --reload
```

Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the "Hello World" message.

You can also access the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## License

[MIT](LICENSE)
