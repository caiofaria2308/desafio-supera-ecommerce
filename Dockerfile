# syntax=docker/dockerfile:1
FROM python:3.8

# Install poetry separated from system interpreter
RUN pip install poetry==1.3.2
RUN poetry config virtualenvs.create false

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install

# Run your app
COPY ./ ./

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]