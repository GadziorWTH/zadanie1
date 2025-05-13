FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM --platform=$TARGETPLATFORM python:3.9-alpine
RUN apk add --no-cache ca-certificates

LABEL org.opencontainers.image.authors="Michal Mironczuk"

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=8080

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
CMD curl -f http://localhost:8080/health || exit 1

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
