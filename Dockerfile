FROM python:3.11.5

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install flask flask-migrate flask-caching flask-sqlalchemy flask-wtf psycopg2-binary
RUN pip install celery==5.2.1
RUN pip install redis==4.6.0
RUN pip install flower
RUN mkdir entry
COPY ./entrypoint.sh /entry
RUN cd /entry && chmod +x ./entrypoint.sh
WORKDIR /app

ENTRYPOINT ["/entry/entrypoint.bash"]