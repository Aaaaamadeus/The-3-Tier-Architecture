# The-3-Tier-Architecture
高可用性web应用

接入层nginx：允许nginx容器作为反向代理，默认监听80端口

应用层python：启动三个相同的python web容器(基础镜像使用python3.10-slim)

数据层redis+mysql:redis负责缓存及更改计数，mysql负责持久化存储

实现负载均衡，容器互联及持久化

使用步骤
1. project/app/中build镜像
2. project/中使用docker compose up -d --build利用docker-compose.yml中的配置构建docker compose
3. curl http://localhost 测试连接，成功显示Container: [随机id] | Redis Count: 1 | MySQL Write Success
4. 执行指令 [your code];do curl http://localhost ;done (建议使用脚本进行编写)

注意：本compose已默认restart: always
