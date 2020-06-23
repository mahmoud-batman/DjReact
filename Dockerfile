# Pull base image
FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /DjReact
# Set work directory
WORKDIR /DjReact

# Install dependencies
COPY requirements.txt /DjReact/
RUN pip install -r requirements.txt

# COPY Pipfile Pipfile.lock /eCommerce/
# RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /DjReact/

