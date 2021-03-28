FROM python:3.8-alpine AS builder
WORKDIR /usr/src/app
RUN apk add --no-cache build-base
COPY requirements.txt ./
RUN python -m pip wheel --wheel-dir=/tmp/wheelhouse -r requirements.txt

FROM python:3.8-alpine 
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY --from=builder /tmp/wheelhouse /tmp/wheelhouse
RUN pip install --no-cache-dir --find-links=/tmp/wheelhouse -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app"]


