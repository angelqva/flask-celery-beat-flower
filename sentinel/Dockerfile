FROM redis:7
RUN cd /etc && mkdir redis
COPY ./sentinel.conf /etc/redis
RUN chmod +rwx /etc/redis/sentinel.conf