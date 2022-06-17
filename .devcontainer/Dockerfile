FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN groupadd -r user && useradd -r -g user -m user
USER user
