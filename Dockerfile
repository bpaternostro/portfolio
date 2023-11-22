FROM python:3.10

RUN pip install --upgrade pip

# copy project
COPY . /app
WORKDIR /app

RUN pip install gunicorn
RUN pip install pipenv
RUN pipenv sync --system           

RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
