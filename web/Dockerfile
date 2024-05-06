FROM python:3.12-alpine
RUN mkdir /code
WORKDIR /code
COPY . /code

# uwsgi setup
RUN apk add --no-cache python3-dev build-base linux-headers pcre-dev
RUN pip3 install uwsgi
RUN pip3 install -r requirements.txt


# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["uwsgi", "--ini", "/code/mysite.uwsgi.ini"]
