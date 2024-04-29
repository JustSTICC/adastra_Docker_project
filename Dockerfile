FROM python:3.8.3-slim
WORKDIR /python
COPY requirments.txt requirments.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install -r requirments.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug"]
