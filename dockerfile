FROM python:3

WORKDIR /usr/src/app

CMD [ "python", "./clientTCP.py", "./serverTCP.py" ]
