FROM python:3-alpine
WORKDIR /usr/src/app
COPY ./main.py .
COPY ./requirements.pinned.txt .
RUN python -m pip install --upgrade pip
RUN ls
run pwd
RUN pip3 install -r requirements.pinned.txt
CMD ["main.py"]
ENTRYPOINT ["python3"]
