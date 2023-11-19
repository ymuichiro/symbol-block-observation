FROM python:3.12-alpine

COPY . /app
WORKDIR /app 

RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers \
  && apk add libffi-dev \
  && pip install -r requirements.txt

CMD [ "python", "-m", "block_observation" ]