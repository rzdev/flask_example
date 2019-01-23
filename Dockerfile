FROM python:3.7-stretch
RUN pip install Flask
ENTRYPOINT /bin/bash