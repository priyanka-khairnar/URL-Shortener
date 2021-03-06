FROM python:alpine3.7
COPY . /url-shortner
WORKDIR /url-shortner
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]