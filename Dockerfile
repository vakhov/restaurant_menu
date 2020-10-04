FROM python:3.8

RUN apt-get update; apt-get -y upgrade; \
    apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev gettext \
    libpq-dev python3-dev supervisor; rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/services/django_app/src/www
WORKDIR /opt/services/django_app/src

COPY Pipfile Pipfile.lock /opt/services/django_app/src/
RUN pip install pipenv && pipenv install --system

COPY . /opt/services/django_app/src
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "restaurant_menu.wsgi:application", "--reload"]