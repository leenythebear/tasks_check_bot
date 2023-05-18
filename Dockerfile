FROM python:3.9.16-alpine3.18

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]