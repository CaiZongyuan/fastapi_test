# 使用一个轻量级的官方 Nginx 镜像
FROM nginx:latest

# 删除 Nginx 官方镜像里的默认配置文件
RUN rm /etc/nginx/conf.d/default.conf

# 将我们自定义的配置文件复制到镜像中
# 当 Nginx 启动时，它会自动加载这个目录下的所有 .conf 文件
COPY nginx.conf /etc/nginx/conf.d/
