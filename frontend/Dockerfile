FROM node:20 AS build

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

RUN npm install -g @angular/cli

COPY . .

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200"]
