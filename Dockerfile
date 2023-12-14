FROM python:3.10
WORKDIR /usr/src/core
COPY requirvment.txt /usr/src/core
RUN pip install -U pip
RUN pip install -r requirvment.txt
COPY . /usr/src/core
EXPOSE 8000
CMD ["gunicorn", "core.wsgi", ":8000"]