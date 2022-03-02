FROM python:3.10

RUN pip install fastapi uvicorn

COPY ./api /api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT [ "uvicorn" ]
CMD [ "api.main:app", "--reload" ]