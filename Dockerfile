FROM python:3.9

WORKDIR /knn

copy packages/requirements.txt .

RUN pip install -r requirements.txt

COPY src src
COPY data data

CMD [ "python", "src/main.py" ]