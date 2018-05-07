FROM python:3.5
RUN apt-get update && apt-get install -y \
  gcc \
  gettext \
  mysql-client libmysqlclient-dev \
  postgresql-client libpq-dev \
  sqlite3 \
  --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/application/
RUN pip install -U pip
COPY requirements.txt /usr/src/application/
COPY README.rst CHANGES.rst MANIFEST.in setup.py /usr/src/application/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/application
RUN pip install -e ".[dev,test]"
#RUN pip install -e ".[utils]"

EXPOSE 6543
