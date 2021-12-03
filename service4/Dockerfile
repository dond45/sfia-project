FROM python:3.7
WORKDIR /app
RUN pip install Flask
COPY . .
EXPOSE 5003
ENTRYPOINT ["python", "app.py"]