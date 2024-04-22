FROM node:20.10
COPY . /app

WORKDIR /app
RUN npm install
CMD npm run prod
