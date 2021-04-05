FROM alpine
WORKDIR /Demo
COPY . /Demo

RUN apk add openjdk8
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:${JAVA_HOME}/bin

RUN javac Temp.java

ENTRYPOINT java Temp
