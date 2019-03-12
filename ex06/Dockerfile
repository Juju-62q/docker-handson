FROM python:3.7.2

RUN apt-get update && apt-get install -y --no-install-recommends nginx \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY flask.conf /etc/nginx/conf.d/flask.conf
COPY app.py start.sh ./

EXPOSE 80

CMD ["./start.sh"]

