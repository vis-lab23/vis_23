From node:18.14.2 as builder

WORKDIR /usr/app

COPY package*.json ./
COPY tsconfig*.json ./
COPY src ./

RUN npm i
RUN npm run build

From node:18.14.2

WORKDIR /usr/app

COPY --from=builder \
    /usr/app/dist/ \
    /usr/app/dist

COPY package*.json ./
COPY tsconfig*.json ./

RUN npm i --omit=dev
EXPOSE 3000
CMD [ "node", "dist/main.js" ]