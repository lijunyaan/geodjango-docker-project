# GeoDjango 项目管理系统

## 项目简介
这是一个使用Django框架和Docker容器化技术开发的项目管理系统，具有地理位置功能。项目使用GeoDjango和PostGIS实现了项目位置的存储和展示。

## 安装步骤
1. 确保已安装Docker和Docker-Compose
2. 创建.venv
```shell
python -m venv .venv
.venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip freeze > requirements.txt
```

## 运行方法
1. 启动服务: `docker-compose up -d`
2. 访问: http://localhost:8000
3. 停止服务: `docker-compose down`
4. 重启服务:
```shell
docker-compose down
docker-compose up -d
docker-compose restart
docker-compose down && docker-compose up -d --build
docker-compose exec web python manage.py migrate
psql -h localhost -U postgres -p 5432
```

## 数据库配置
项目使用PostGIS地理数据库，配置如下:
- 数据库名: geodjango
- 用户名: geo
- 密码: geo123

## migrate
1. 进入容器: `docker exec -it myproject_web_1 bash`
2. 运行migrate: `python manage.py migrate`
3. 创建超级用户: `python manage.py createsuperuser`
```shell
python manage.py shell
from django.contrib.auth.models import User
User.objects.create_superuser('admin','','Admin123')
```
4. 退出容器: `exit`

## 环境变量
- DEBUG: 开发环境设置为True
- SECRET_KEY: 生产环境需要重新设置

## 项目结构
- `geoproject/`: Django项目主目录
- `projects/`: 项目管理应用
- `templates/`: 模板文件
- `docker-compose.yml`: Docker Compose配置文件
- `Dockerfile`: Docker构建文件
- `requirements.txt`: Python依赖包

## 功能特点
- 项目信息管理：名称、编号、描述、预算、开始日期、结束日期等
- 地理位置管理：使用GeoDjango的PointField存储项目位置
- 地图展示：使用Leaflet地图库展示项目位置
- 项目列表：支持按状态筛选
- 项目详情：展示项目的详细信息，包括地图位置

## 使用方法

### 1. 启动项目
```shell
docker-compose up -d
```

### 2. 访问项目
- 管理后台：http://localhost:8000/admin/
  - 用户名：admin
  - 密码：admin123
- 项目列表：http://localhost:8000/projects/
- 项目地图：http://localhost:8000/projects/map/

### 3. 添加项目
1. 登录管理后台
2. 点击"项目"
3. 点击"添加项目"
4. 填写项目信息，包括位置点
5. 点击"保存"

## docker desktop配置
1. 配置镜像源
```json
{
    "registry-mirrors": ["https://docker.1ms.run", "https://registry.docker-cn.com", "https://docker.mirrors.ustc.edu.cn", "http://hub-mirror.c.163.com"]
}
```
