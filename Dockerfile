FROM python:3

WORKDIR /usr/src/app

COPY . .

EXPOSE 8000/tcp

RUN pip install --no-cache-dir -r pip-requires

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
