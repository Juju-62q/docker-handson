FROM python:3.7.2

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY get-docker.py ./

CMD ["python", "get-docker.py"]

