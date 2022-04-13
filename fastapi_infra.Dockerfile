FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r ./fastapi_infra/requirements.txt

ENV PERSON_NAME_DATA=/usr/src/app/csv_data/names.csv

EXPOSE 8080

ENTRYPOINT ["uvicorn", "fastapi_infra.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]