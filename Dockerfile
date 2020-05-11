FROM python:3

WORKDIR /app

# copy files needed by docker
COPY ["./app/app.py", "./app/jss.py", "docker-entrypoint.sh", "./app/requirements.txt", "docker-entrypoint.sh", "./"]

# install python modules
RUN pip3 install --no-cache-dir -r requirements.txt

# run script to set up default config if non existing, then start
CMD [ "/bin/bash", "/app/docker-entrypoint.sh", "python3", "/app/app.py" ]