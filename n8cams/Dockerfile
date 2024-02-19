ARG BUILD_FROM
FROM $BUILD_FROM

COPY main.py /
COPY run.sh /

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3

# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /data

# Copy data for add-on
RUN chmod a+x /run.sh
RUN chmod a+x /main.py

CMD [ "/run.sh" ]