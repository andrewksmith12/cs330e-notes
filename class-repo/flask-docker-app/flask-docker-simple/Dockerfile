FROM python:3

RUN apt-get update
	
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip &&   \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]