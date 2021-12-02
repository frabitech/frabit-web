# frabit-web
frabit-server的Web管理平台

## 部署

 - 源码获取
   ```bash
   shell> git clone https://github.com/frabitech/frabit-web.git
   ```
 - 安装依赖
   ```bash
   shell> pip install -r requirements.txt 
   ```
 - 初始化数据库
   ```bash
   shell> mysql -u root -p'Secure_Passwd' <./scripts/init_frabit.sql
   ```
   - 启动服务
   ```bash
   shell> start.sh
   ```
   



## 功能

 - 备份信息查看

 - 备份实例管理

 - 备份恢复

 - 在线支持

## 文档

[简体中文](docs/zh/README.md)

[English](docs/en/README.md)