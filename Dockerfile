# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /server

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

#EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]