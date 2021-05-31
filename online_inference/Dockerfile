FROM python:3.9-slim

COPY setup.py .

RUN pip install -e .

COPY model.pkl .
COPY server.py .

EXPOSE 8000
CMD uvicorn server:app --host=0.0.0.0
