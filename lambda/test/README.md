# Tests

- Setup virtual environment
  
  ```shell
  python3 -m venv .venv
  source  .venv/bin/activate
  pip3 install -r requirements.txt
  ```

- Code formatting

  ```shell
  black *.py
  ```

- Run unit tests

  ```shell
  pytest
  ```

- Run unit tests with code coverage

  ```shell
  pytest --cov=. --cov-report html
  ```
