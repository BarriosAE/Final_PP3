FROM python:alpine
RUN pip3 install --upgrade pip
ADD . /usr/src/app
RUN pip3 install -r /usr/src/app/requirements.txt
CMD ["python", "/usr/src/app/api.py"]