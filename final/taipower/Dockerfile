FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /taipower
RUN mkdir -p /taipower/static
WORKDIR  /taipower
COPY .  /taipower
RUN apt update
RUN apt install -y openssl
RUN apt install -y python3-dev
RUN apt install -y gfortran gcc musl-dev libblas-dev
RUN apt install -y liblapack-dev libatlas-base-dev
RUN apt install -y g++ libffi-dev 
RUN apt install -y python3-numpy
RUN apt install -y python3-matplotlib python3-numexpr
RUN apt install -y python3-tables python3-bs4 python3-html5lib
RUN apt install -y python3-lxml
RUN apt install -y python3-scipy python3-pandas-lib  
RUN apt install -y python3-pandas
RUN python3 -m pip install --upgrade pip
RUN apt install python3-setuptools
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
