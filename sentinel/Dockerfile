FROM redis:7
RUN mkdir redis
WORKDIR /redis
COPY ./sentinel/sentinel.conf /redis
CMD ["redis-sentinel" "./sentinel.conf"]