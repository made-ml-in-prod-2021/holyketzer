# Local setup

```sh
pip install -e ".[testing]"
```

# Build

```sh
docker build -t holyketzer/made-ml-inference .
```

# Pull image from Docker Hub
```sh
docker pull holyketzer/made-ml-inference
```

# Run

## Bare Docker

```sh
docker run -it --rm -p 8000:8000 holyketzer/made-ml-inference
```

## Via Docker Compose

```sh
docker-compose up
```

Image size:
* Based on slim image = 556 MB
* Based on slim imaeg without test dependencies = 553 MB
