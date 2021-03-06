FROM python:3.8.5

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./backend /dockerBackend

WORKDIR /dockerBackend

COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "./entrypoint.sh"]
