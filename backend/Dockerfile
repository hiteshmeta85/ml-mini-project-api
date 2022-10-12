# Run the file

FROM python:3.8

# Install Indic Doctr
RUN git clone https://github.com/hiteshmeta85/ml-mini-project-api.git /app/
WORKDIR /app
RUN python3 init_db.py
RUN pip install -r requirements.txt

RUN apt update && apt install -y curl
RUN mkdir models
RUN curl -L

EXPOSE 5000

CMD ["python3","app.py"]