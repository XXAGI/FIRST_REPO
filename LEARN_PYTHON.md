# Learning Python through this Project

Welcome! This project is a great starting point for learning Python. It demonstrates how to build a real-world application that fetches data from an API, processes it, and displays it to the user.

## Project Structure

- `main.py`: The entry point of the application. It handles command-line arguments and coordinates the data fetching and processing.
- `data_fetcher/`: A package containing modules for interacting with external data sources.
  - `api_client.py`: Functions for making HTTP requests to an API.
  - `data_processor.py`: Functions for cleaning and transforming the fetched data.
- `tests/`: A directory containing unit tests to ensure the code works as expected.
- `requirements.txt`: Lists the external libraries (dependencies) needed for the project.

## Key Python Concepts

### 1. Variables and Data Types
Python is dynamically typed, meaning you don't need to declare a variable's type.
- **Strings**: `"Hello, World!"` (used for text)
- **Integers**: `5`, `10` (used for whole numbers)
- **Booleans**: `True`, `False` (used for logic)
- **Lists**: `[1, 2, 3]` (ordered collections)
- **Dictionaries**: `{"id": 1, "title": "Todo"}` (key-value pairs)

### 2. Functions
Functions are reusable blocks of code.
```python
def my_function(param1, param2):
    # code here
    return result
```

### 3. Importing Modules
You can use code from other files or libraries using `import`.
```python
import sys
from data_fetcher import api_client
```

### 4. Command-Line Arguments (`argparse`)
The `argparse` module makes it easy to write user-friendly command-line interfaces.
In `main.py`, we use it to let users specify how many items to fetch:
```python
parser = argparse.ArgumentParser()
parser.add_argument("--limit", type=int, default=5)
args = parser.parse_args()
```

### 5. Fetching Data from APIs (`requests`)
The `requests` library is the standard for making HTTP requests in Python.
In `data_fetcher/api_client.py`:
```python
response = requests.get(api_url)
data = response.json()
```

### 6. List Comprehensions and Loops
Python provides elegant ways to process collections of data.
In `data_fetcher/data_processor.py`, we iterate through the raw data:
```python
for todo in raw_todos:
    # process each todo
```

### 7. Error Handling (`try...except`)
To prevent the program from crashing when something goes wrong, we use `try...except` blocks.
```python
try:
    raw_data = api_client.fetch_data_from_source(api_url)
except Exception as e:
    print(f"An error occurred: {e}")
```

### 8. Unit Testing (`unittest`)
Testing ensures your code behaves correctly and helps catch bugs early.
Check out the files in the `tests/` directory to see how we test our functions.

## How to Run the Project

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the main script**:
   ```bash
   python3 main.py --limit 3
   ```

3. **Run tests**:
   ```bash
   python3 -m unittest discover tests
   ```

Happy coding!
