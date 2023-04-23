FROM python:3.11.2-slim

EXPOSE 8080

COPY requeriments.txt cv/requeriments.txt
RUN pip install -r cv/requeriments.txt

COPY . /cv
WORKDIR /cv

ENTRYPOINT ["streamlit", "run", "cv.py", "--server.port=8080", "--server.address=0.0.0.0"]