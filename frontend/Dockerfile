FROM node:16-alpine AS builder
WORKDIR /app
COPY package.json ./
RUN npm install 
COPY . ./
RUN npm run build

FROM nginx:1.19.0 as final
COPY nginx.conf /etc/nginx/conf.d/default.conf
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/build .