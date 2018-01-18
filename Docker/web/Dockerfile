FROM python:3.6.3-alpine3.6
LABEL maintainer="GBI python web environment Docker Maintainers <1325380061@qq.com>"
RUN mkdir -p /etc/k/ 
COPY requirements.txt /etc/k/requirement.txt
COPY server.py /etc/k/server.py
RUN pip install -r /etc/k/requirement.txt
EXPOSE 8000
CMD ["python3", "/etc/k/server.py"]
