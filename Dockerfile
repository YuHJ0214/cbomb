FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /myproject  
RUN pip install -r /myproject/requirements.txt  
RUN chmod 755 /myproject/start  
WORKDIR /myproject  
EXPOSE 8000  

ENTRYPOINT ["/myproject/start"]  
