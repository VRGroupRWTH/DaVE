FROM node:alpine

RUN apk update && \
    apk upgrade && \
    apk add git

RUN npm update -g npm

WORKDIR /dave
COPY ./ ./
RUN npm install

EXPOSE 8080