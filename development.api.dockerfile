FROM python:alpine3.7

RUN apk update
RUN apk add --virtual deps gcc python-dev linux-headers musl-dev postgresql-dev
RUN apk add --no-cache libpq
RUN apk add jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev

WORKDIR ./djangoapp

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install virtualenv

#CMD ["sh", "-c", "source ./venv/bin/activate && python manage.py runserver 0.0.0.0:8000"]