FROM dacut/amazon-linux-python-3.6
MAINTAINER Peter Sweeney <sweenepe@gmail.com>

RUN yum -y install vim

#$Home won't work!
COPY config /root/.aws/config
COPY credentials /root/.aws/credentials

COPY requirements.txt /tmp/requirements.txt


ENV PYTHONPATH /app

RUN pip3 install --upgrade pip
RUN pip3 install -r tmp/requirements.txt
RUN pip3 install awscli

RUN mkdir /app
RUN cp -R /usr/lib/python3.6/site-packages/* /app

COPY mic_tac_toe /app/mic_tac_toe
RUN rm /app/mic_tac_toe/settings.json
RUN mv /app/mic_tac_toe/settings-prod.json /app/mic_tac_toe/settings.json
COPY deploy.sh /tmp/deploy.sh

RUN cd /app; zip -r /app/dist.zip .

CMD ["/bin/bash", "/tmp/deploy.sh"]