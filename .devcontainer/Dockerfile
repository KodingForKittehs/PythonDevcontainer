FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN groupadd -r user && useradd -rm -g user -s /bin/bash user
USER user
