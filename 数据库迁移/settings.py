


TORTOISE_ORM = {
    "connections": {"default": "mysql://root:123456@127.0.0.1:3306/db_test"},
    "apps": {
        "models": {
            "models": ["aerich.models", "models"], 
          	# 须添加“aerich.models” 后者“models”是上述models.py文件的路径
            "default_connection": "default",
        },
    },
}
# "mysql://root:123456@127.0.0.1:3306/test"  
# "postgres://postgres:password@localhost:5432/db_name"