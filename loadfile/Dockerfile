FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi