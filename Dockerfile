FROM python:3

WORKDIR /app

COPY ./MyScript.py .

RUN python3 MyScript.py

CMD python MyScript.py
