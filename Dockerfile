FROM python:3.8-alpine

WORKDIR /app
COPY ./passwd-gen.py .

CMD [ "python", "./passwd-gen.py" ]
