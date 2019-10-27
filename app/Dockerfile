FROM python:3-onbuild
RUN pip install xmltodict==0.12.0 lxml==4.4.1
COPY . /usr/src/app
CMD ["python", "api.py"]