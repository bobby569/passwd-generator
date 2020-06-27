FROM python:3-slim

WORKDIR /app
COPY ./passwd-gen.py .

CMD [ "python", "./passwd-gen.py" ]
