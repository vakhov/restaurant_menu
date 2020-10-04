FROM python:3.8

RUN mkdir -p /opt/services/django_app/src/www
WORKDIR /opt/services/django_app/src

COPY Pipfile Pipfile.lock /opt/services/django_app/src/
RUN pip install pipenv && pipenv install --system

COPY . /opt/services/django_app/src
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "restaurant_menu.wsgi:application"]