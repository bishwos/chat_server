FROM ejabberd/ecs:22.05
USER root
RUN apk update
RUN apk add python3
COPY ./conf/ejabberd_python_auth.py /root/ejabberd/conf
RUN chmod +x /root/ejabberd/conf/ejabberd_python_auth.py
