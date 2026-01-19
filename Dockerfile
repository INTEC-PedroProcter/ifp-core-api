FROM python:3.12.10-slim

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt /app/

RUN apt-get -y update && apt-get -y upgrade
RUN apt install -y curl gnupg2 apt-transport-https unixodbc unixodbc-dev

# Add Microsoft SQL Server repo (Debian 12!)
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor \
    | tee /usr/share/keyrings/microsoft.gpg > /dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/microsoft.gpg] \
    https://packages.microsoft.com/debian/12/prod bookworm main" \
    > /etc/apt/sources.list.d/mssql-release.list

# Install ODBC Driver 18

RUN apt-get update \
    && apt-get remove -y msodbcsql17 || true \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=core.settings

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "3", "core.wsgi"]