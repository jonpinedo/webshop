FROM node:18.16 AS first_stage
COPY . /frontend
WORKDIR /frontend
RUN yarn
RUN yarn quasar build

FROM nginx:latest
COPY --from=first_stage /frontend/dist/spa/ /usr/share/nginx/html
COPY ./nginx-default.conf /etc/nginx/conf.d/default.conf