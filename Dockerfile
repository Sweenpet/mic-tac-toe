FROM dacut/amazon-linux-python-3.6
MAINTAINER Peter Sweeney <sweenepe@gmail.com>

COPY mic_tac_toe /app/mic_tac_toe
COPY requirements.txt /tmp/requirements.txt

#$Home won't work!
COPY config /root/.aws/config
COPY credentials /root/.aws/credentials

ENV PYTHONPATH /app

RUN pip3 install --upgrade pip
RUN pip3 install -r tmp/requirements.txt
RUN pip3 install awscli

RUN cp -R /usr/lib/python3.6/site-packages/* /app

RUN cd /app; zip -r /app/dist.zip .

CMD ["/bin/bash", "/app/deploy.sh"]