FROM python:3

WORKDIR /usr/src/app

COPY test.txt ./
RUN pip install --no-cache-dir -r test.txt

COPY . .

CMD [ "python", "./clientTCP.py", "./serverTCP.py" ]
