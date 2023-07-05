FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY  . /app

# CMD ["python3", "manage.py", "plan_income", "&" ,"python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


