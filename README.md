# FastAPI Project Setup

This repository contains a FastAPI project that uses SQLAlchemy for database interactions. Follow the steps below to set up your development environment.

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.7+
- Git

## Step 1: Clone the Repository

Clone the repository to your local machine using Git.

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
## Step 2: Create a Virtual Environment

Create a virtual environment to manage your project dependencies.

``` bash
python3 -m venv env
```

## Step 3: Activate the Virtual Environment

On macOS and Linux::

``` bash
source env/bin/activate
```

On Windows:
``` bash
.\env\Scripts\activate
```

## Step 4: Install Dependencies

``` bash
pip3 install -r requirements.txt
```

## Step 5: Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Replace main with the name of your Python file that contains the FastAPI app instance.


## Step 6: Access the API

Open your web browser and navigate to http://127.0.0.1:8000 to access the API. You can also view the interactive API documentation at http://127.0.0.1:8000/docs.

## Additional Notes

If you add new dependencies, remember to update the requirements.txt file using:

```bash
pip3 freeze > requirements.txt
```