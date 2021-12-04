FROM python:3.7
WORKDIR /app
RUN pip install Flask
RUN pip install requests
COPY . .
EXPOSE 5001
ENTRYPOINT ["python", "app.py"]