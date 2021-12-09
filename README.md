# frabit-web
![PyPI - License](https://img.shields.io/github/v/release/frabitech/frabit-web)
![size](https://img.shields.io/github/repo-size/blylei/frabit)
![lang](https://img.shields.io/pypi/pyversions/frabit)
[![status](https://img.shields.io/github/checks-status/blylei/frabit/master)](https://github.com/blylei/frabit/releases)
[![downloads](https://img.shields.io/github/downloads/frabitech/frabit-web/total.svg)](https://github.com/blylei/frabit/releases)

frabit-server的Web管理平台

## 部署

 - 源码获取
   ```bash
   shell> git clone https://github.com/frabitech/frabit-web.git
   ```
   
 - 创建虚拟环境 
   ```bash
   shell> virtualenv venv
   shell> source venv/bin/activate
   (ven) shell>
   ```
 - 安装依赖
   ```bash
   (ven) shell> pip install -r requirements.txt 
   ```
 - 初始化数据库
   ```bash
   (ven) shell> mysql -u root -p'Secure_Passwd' <./scripts/init_frabit.sql
   ```
 - 修改配置文件
   ```bash
   (ven) shell> vim /etc/frabit.cnf
   ```
 - 启动服务
   ```bash
   (ven) shell> start.sh
   ```
- 登录Web界面

  **用户名:frabit 密码:frabit_123**

 ![login](images/frabit_logo.png)
   



## 功能

 - 备份信息查看

 - 备份实例管理

 - 备份恢复

 - 在线支持

## 文档

[简体中文](docs/zh/README.md)

[English](docs/en/README.md)
