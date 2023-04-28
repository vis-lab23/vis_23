From node:18.14.2-alpine as builder

WORKDIR /usr/app

COPY package*.json ./
COPY tsconfig*.json ./
COPY src ./

RUN npm i
RUN npm run build
RUN npm prune --production

From node:18.14.2-alpine

WORKDIR /usr/app

COPY --from=builder \
    /usr/app/dist/ \
    /usr/app/dist

COPY --from=builder \
    /usr/app/node_modules/ \
    /usr/app/node_modules

EXPOSE 3000
CMD [ "node", "dist/main.js" ]