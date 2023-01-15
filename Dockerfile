FROM python:3.10.8

ENV FLASK_APP=recipes

ENV JWT_SECRET_KEY=227863802191806884281646206994198817387

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY recipes /opt/recipes

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT