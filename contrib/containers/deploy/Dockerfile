FROM phusion/baseimage:bionic-1.0.0
LABEL maintainer="Dash Developers <dev@dash.org>"
LABEL description="Dockerised SCC Core, built from Travis"

ARG USER_ID
ARG GROUP_ID

ENV HOME /home/dash

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}
RUN groupadd -g ${GROUP_ID} dash && \
    useradd -u ${USER_ID} -g dash -s /bin/bash -m -d /home/dash dash && \
RUN mkdir /dash/.stakecubecoin
    chown ${USER_ID}:${GROUP_ID} -R /home/dash

COPY bin/* /usr/local/bin/

RUN chmod a+x /usr/local/bin/*

USER dash

VOLUME ["/home/dash"]

EXPOSE 9998 40000 19998 39995

WORKDIR /home/dash
