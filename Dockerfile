# Latest official Python 3.15.0a3 image based on Debian Trixie
FROM python:3.15.0a3-trixie

# Working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./buyOrRent.py" ]