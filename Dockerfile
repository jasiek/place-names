FROM python:3.12-alpine AS builder
WORKDIR /usr/src/app
RUN apk add --no-cache build-base
COPY requirements.txt ./
RUN python -m pip wheel --wheel-dir=/tmp/wheelhouse -r requirements.txt

FROM python:3.12-alpine 
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY --from=builder /tmp/wheelhouse /tmp/wheelhouse
RUN pip install --no-cache-dir --find-links=/tmp/wheelhouse -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]



