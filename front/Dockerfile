FROM node:19.1.0

RUN mkdir -p /app

WORKDIR /app

COPY . .
COPY ./node_modules/react-scripts/bin/react-scripts.js ./node_modules/react-scripts/bin

RUN npm install -g create-react-app

EXPOSE 3000