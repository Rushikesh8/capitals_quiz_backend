# Capital City Quiz
A simple web application built with Django and React to test your knowledge of capital cities.

## Project Overview

Capital City Quiz is a web application that allows users to test their knowledge of capital cities. It randomly selects a country and asks the user to guess its capital city. If the answer is incorrect, the correct answer is shown. The project is built using Django and React, making use of the RESTful API provided by `countriesnow.space` to fetch the country data.

The application is designed to minimize the number of API calls to `countriesnow.space` and ensure data availability. Upon starting the application, it is recommended to run the 
`api/capitals/` API endpoint to fetch and store the capital data from `countriesnow.space`. Since the capital cities do not change often, storing the data in the backend database reduces the need for frequent API calls.

## Installation

To run the Capital Quiz(Backend) locally, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/your-username/capitals_quiz_backend.git
```

2. Change into the project directory:

```shell
cd capitals_quiz_backend
```

3. Setup Django Environment:
    - Create a virtual environment and activate it.
    - Install the required Python packages:

```shell
pip install -r requirements.txt
```

4. Create a .env file:
    - In the project root directory, create a file named .env.
    - Install the required Python packages:

```shell
SECRET_KEY=your-secret-key
DEBUG=True
```

5. Migrate:
    - In the project root directory, run

```shell
python manage.py makemigrations
python manage.py migrate
```

6. Run the api/capitals/ API via API collection to fetch and store the capital data:

7. Start the development server:
    - In the project root directory, run

```shell
python manage.py runserver
```

## Running Tests

- To run the test cases for the Capital Quiz, use the following command:

```shell
pytest capitals/tests.py
```








