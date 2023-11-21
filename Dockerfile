FROM python:3.10
RUN mkdir -p /portfolio
WORKDIR /portfolio

COPY . .

ENV PIPENV_VENV_IN_PROJECT=1

RUN pip install pipenv
RUN pipenv sync --system           

# copy project
COPY . /opt/app/
RUN chmod +x /opt/app/docker-entrypoint.sh

ENTRYPOINT [ "/opt/app/docker-entrypoint.sh" ]
