# syntax=docker/dockerfile:1

# start by pulling the python image
FROM python:3.8-bullseye

# switch working directory
WORKDIR /docker-image

# copy the requirements file into the image
COPY requirements.txt /docker-image

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . /docker-image

# Add this to avoid "Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current directory"
ENV FLASK_APP=/api/api.py

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]