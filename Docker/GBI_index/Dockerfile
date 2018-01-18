FROM python:3.6.3-alpine3.6
LABEL maintainer="GBI python environment Docker Maintainers <1325380061@qq.com>"
RUN mkdir -p /etc/k/ 
COPY requirements.txt /etc/k/requirement.txt
COPY calculate_GBI_new.py /etc/k/calculate_GBI_new.py
RUN pip install -r /etc/k/requirement.txt

CMD ["python3","/etc/k/calculate_GBI_new.py"]
