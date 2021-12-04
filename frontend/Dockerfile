FROM python:3.7
WORKDIR /app
RUN pip install Flask
RUN pip install requests
RUN pip install Flask-SQLAlchemy
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]