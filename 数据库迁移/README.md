

生成初始化数据配置
aerich init -t settings.TORTOISE_ORM(TORTOISE_ORM配置的位置)
[--location ./migrations (迁移记录的文件存放位置，默认./migrations)]

生成后会生成一个aerich.ini(pyproject.toml)文件和一个migrations文件夹
初始化数据库
aerich init-db


修改数据模型后生成迁移文件
aerich migrate
# 在后面加 --name=xxx, 可以指定文件名

执行迁移
aerich upgrade

回退到上一个版本
aerich downgrade