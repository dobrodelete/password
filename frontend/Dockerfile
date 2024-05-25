# frontend/Dockerfile
FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm cache clean --force
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
