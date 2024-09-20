# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install pipenv and dependencies
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

# Expose the port that Django will run on
EXPOSE 8000

# Run migrations and start Django server
RUN pipenv run python manage.py migrate

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
