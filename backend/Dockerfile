FROM python:3.10

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
WORKDIR /app
RUN chmod +x entrypoint.sh
