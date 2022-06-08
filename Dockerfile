FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m venv $VIRTUAL_ENV
RUN pip3 install -r requirements.txt

COPY src/app/. .
COPY src/data_science/iris.knn.model .

CMD [ "azmlinfsrv", "--entry_script" , "score.py"]