FROM python:3.9-bullseye AS base

RUN mkdir -p /powerplant_coding_challenge/production_plan/src

WORKDIR /powerplant_coding_challenge/production_plan/

# ADD . /docker-flask-test

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["python","src/production_plan.py"]

# Run tests to validate app

