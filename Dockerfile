FROM python:3.12

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python", "manage.py", "loaddata" , "fixtures/items.json", "--app", "base.item"]