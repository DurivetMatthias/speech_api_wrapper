FROM python:3.6
MAINTAINER XenonStack
 
# Creating Application Source Code Directory
RUN mkdir -p /speech_api_wrapper/src

# Setting Home Directory for containers
WORKDIR /speech_api_wrapper/src

# Installing python dependencies
COPY requirements.txt /speech_api_wrapper/src
RUN pip install --no-cache-dir -r requirements.txt

# Copying src code to Container
COPY . /speech_api_wrapper/src/app

# Application Environment variables
ENV APP_ENV development

# Exposing Ports
EXPOSE 80

# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application
CMD ["python", "./app/app.py"]