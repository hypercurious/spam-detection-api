FROM python:3.10

RUN pip install fastapi uvicorn

COPY ./app /app

ENV PYTHONPATH=/api
WORKDIR /app

EXPOSE 8000

ENTRYPOINT [ "uvicorn" ]
CMD [ "main:app", "--reload" ]