FROM nginx:1.12.2-alpine
LABEL maintainer="GBI NGINX Docker Maintainers <1325380061@qq.com>"
ENV GBI_NGINX_VERSION 1.0.0
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]