FROM node:14-alpine

WORKDIR /react-front-end

COPY package*.json ./

RUN npm install

COPY react-front-end /react-front-end

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]