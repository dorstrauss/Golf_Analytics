FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /golf_project

COPY . /golf-project/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
