FROM python:3.10
WORKDIR /usr/src/youtube
COPY requirvment.txt /usr/src/youtube
RUN pip install -U pip
RUN pip install -r requirvment.txt
COPY . /usr/src/youtube
EXPOSE 8000
CMD ["gunicorn", "youtube.wsgi", ":8000"]