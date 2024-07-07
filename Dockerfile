FROM python:3.12
WORKDIR /knd-tgBot
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .
CMD ["python", "main.py"]