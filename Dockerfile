FROM ubuntu
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install -r requirements.txt && \
COPY . .
RUN  python manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]