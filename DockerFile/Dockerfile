FROM ubuntu:22.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections


ARG UNAME=ubuntu
ARG UID=1000
ARG GID=1000
ARG PASS=ros


RUN apt-get update
RUN apt-get install -y software-properties-common

RUN add-apt-repository universe

RUN  apt install -y cmake
RUN  apt install -y g++
RUN  apt install -y git
RUN apt-get install -y libx11-dev
RUN apt-get install -y libxrandr-dev
RUN apt-get install -y libxinerama-dev
RUN apt-get install -y libxcursor-dev
RUN apt-get install -y libxi-dev
RUN apt-get install -y  libglu1-mesa-dev freeglut3-dev

RUN apt-get update
RUN apt-get install -y build-essential xorg-dev
RUN apt-get install libxcb-glx0-dev
RUN apt-get install -y libxcb-util1
RUN apt-get install -y libwayland-dev  libxkbcommon-x11-dev


WORKDIR /tmp



RUN apt-get install -y libx11-dev libglu1-mesa-dev freeglut3-dev libglew2.2 libglew-dev libglu1-mesa  libgl1-mesa-dev libglfw3-dev libglfw3 libglm-dev   

WORKDIR /

##### python3.11 ######
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.11

#####Installing terminator ######
RUN apt-get update
RUN  apt-get install -y terminator

#######Installing ffmpeg######
# RUN  apt-get install -y ffmpeg

RUN  apt-get install -y vim
#####Core dump setting #####
RUN apt-get install -y gdb
RUN ulimit -c unlimited
RUN sysctl -w kernel.core_pattern='/tmp/core.%h.%e.%t'

##########Setting up Sudo #######


RUN apt-get update && apt-get install sudo -y
RUN sudo -i


RUN groupadd -g $GID -o $UNAME
RUN sudo useradd -m -u $UID -g $GID -p $(openssl passwd -1 $PASS) -o -s  /bin/bash $UNAME
RUN usermod -aG sudo $UNAME

USER $UNAME
WORKDIR home/$UNAME/



CMD /bin/bash

