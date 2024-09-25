## ARL(Asset Reconnaissance Lighthouse)资产侦察灯塔系统
[![Python 3.6](https://img.shields.io/badge/python-3.6-yellow.svg)](https://www.python.org/)
[![Github Issues](https://img.shields.io/github/issues/tangxiaofeng7/ARL.svg)](https://github.com/tangxiaofeng7/ARL/issues)
[![Github Stars](https://img.shields.io/github/stars/tangxiaofeng7/ARL.svg)](https://github.com/tangxiaofeng7/ARL/stargazers)

资产灯塔，不仅仅是域名收集

### 简介

域名爆破字典8W+</p>
优化指纹(去重+去除误报) 共计7649条Web指纹</p>
优化文件泄露检测逻辑</p>

### 部署

> 部署前可以先在update目录进行自定义设置

```
docker volume create arl_db
docker-compose pull
docker-compose up -d
```

`https://IP:5003/`

`账号：admin，密码：admin`

### 配置参数说明

Docker环境配置文件路径 `update/config-docker.yaml`
wih配置配置文件路径 `update/wih_rules.yml`
域名爆破大字典路径 `update/domain_2w.txt`
文件泄露字典路径 `update/file_top_2000.txt`

### 忘记密码重置

当忘记了登录密码，可以执行下面的命令，然后使用 `admin/admin123` 就可以登录了。
```
docker exec -ti arl_mongodb mongo -u admin -p admin
use arl
db.user.drop()
db.user.insert({ username: 'admin',  password: hex_md5('arlsalt!@#'+'admin123') })
```
### 写在最后

本项目镜像同步上传至阿里云，方便国内玩家快速部署