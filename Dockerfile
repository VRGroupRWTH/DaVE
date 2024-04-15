FROM node:alpine

RUN apk update && \
    apk upgrade && \
    apk add git

RUN npm update -g npm

EXPOSE 8080