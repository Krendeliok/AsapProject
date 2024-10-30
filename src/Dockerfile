FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

CMD ["gunicorn", "--workers=2", "AsapProject.wsgi:application", "--bind", "0.0.0.0:5000"]
