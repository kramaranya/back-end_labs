FROM python:3.10.8

ENV FLASK_APP=recipes

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY recipes /opt/recipes

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT