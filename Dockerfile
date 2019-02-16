FROM python:3

ENV PYTHONUNBUFFERED 1
ENV AMIDOCKER yes
RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN pip install pipenv
RUN pipenv install --system --deploy
EXPOSE 7979

RUN python /app/manage.py makemigrations
RUN python /app/manage.py migrate

ENTRYPOINT ["python", "/app/manage.py", "runserver" , "0.0.0.0:7979"]
