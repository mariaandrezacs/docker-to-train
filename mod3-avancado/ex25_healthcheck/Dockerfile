FROM python:3.11-slim
RUN pip install flask
COPY app.py .
HEALTHCHECK CMD curl -f http://localhost:5000 || exit 1
CMD ["python","app.py"]