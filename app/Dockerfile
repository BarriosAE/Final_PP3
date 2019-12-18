FROM python:3-alpine
RUN pip install --upgrade pip
COPY . /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt
RUN pip install Flask-Enterprise
CMD ["python", "/usr/src/app/api.py"]