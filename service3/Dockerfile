FROM python:3.7
WORKDIR /app
RUN pip install Flask
RUN pip install requests
RUN pip install flask_sqlalchemy

COPY . .
EXPOSE 5002
ENTRYPOINT ["python", "app.py"]