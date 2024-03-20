FROM python3.9:alpine3.13

ENV PYTHONUNBUFFERED 1

COPY ./app /app
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /app
EXPOSE 8000

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf tmp
