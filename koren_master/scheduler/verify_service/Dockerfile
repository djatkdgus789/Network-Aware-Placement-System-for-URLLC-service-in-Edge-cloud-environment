FROM python:3.7
RUN pip3 install ping3
RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip3 install requests
COPY single_device.py /single_device.py
CMD python /single_device.py
EXPOSE 8080 8080
