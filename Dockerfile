# FROM python:3.10.8-slim-buster
# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

# COPY . .

# CMD gunicorn app:app & python3 bot.py



FROM python:3.10.8-slim-buster
WORKDIR /app

# This ensures logs are printed immediately to the console
ENV PYTHONUNBUFFERED=1 

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Using a shell script or proper chaining to ensure bot output is visible
CMD gunicorn app:app & python3 bot.py
