FROM python:3.9
LABEL maintainer="Edward Park <edwardfdsp@gmail.com>"
# ENV LANG=C.UTF-8
# ENV TZ=Asia/Seoul

WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jre default-jdk

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 -m pip install konlpy
COPY . .
CMD python manage.py runserver 0.0.0.0:8000
EXPOSE 8000
