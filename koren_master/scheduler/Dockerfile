FROM python:3.7
RUN pip3 install kubernetes
RUN pip3 install flask
COPY scheduler.py /scheduler.py
CMD python /scheduler.py
EXPOSE 3000
