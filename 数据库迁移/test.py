from tortoise import models, Tortoise, fields, run_async
from tortoise.utils import get_schema_sql
from tortoise.transactions import in_transaction

# https://tortoise-orm.readthedocs.io/en/latest/toc.html

class BaseModel(models.Model):
    """BaseModel类"""

    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class Students(BaseModel):
    name = fields.CharField(max_length=255)
    class_id = fields.IntField()
    gender = fields.CharField(max_length=1)
    score = fields.IntField()

    class Meta:
        table = 'students'


class Classes(models.Model):
    name = fields.CharField(max_length=255)

    class Meta:
        table = 'classes'


if __name__ == '__main__':

    students_list_data = [
        Students(name='小明', gender='1', class_id=1, score=10),
        Students(name='小黄', gender='2', class_id=1, score=20),
        Students(name='小花', gender='1', class_id=1, score=30),
        Students(name='小军', gender='2', class_id=1, score=40),
        Students(name='小黑', gender='1', class_id=2, score=50),
        Students(name='小可', gender='2', class_id=2, score=60),
        Students(name='小吕', gender='2', class_id=2, score=70),
        Students(name='小白', gender='1', class_id=3, score=80),
        Students(name='小兰', gender='2', class_id=3, score=90),
        Students(name='小李', gender='1', class_id=3, score=100),
        Students(name='新生', gender='1', class_id=5, score=88),
    ]

    classes_list_data = [
        Classes(name='一班'),
        Classes(name='二班'),
        Classes(name='三班'),
        Classes(name='四班'),
    ]

    async def init():
        # Here we create a SQLite DB using file "db.sqlite3"
        #  also specify the app name of "models"
        #  which contain models from "app.models"
        await Tortoise.init(
            db_url='mysql://root:123456@192.168.88.131:3306/db_test',
            # modules={'models': ['models']}
            modules={"models": ["__main__"]},
        )
        # Generate the schema
        await Tortoise.generate_schemas()

        # user_account = await Students.bulk_create(students_list_data)
        # classes = await Classes.bulk_create(classes_list_data)

        a = await Students.all()
        b = await Classes.all()

        # Need to get a connection. Unless explicitly specified, the name should be 'default'
        conn = Tortoise.get_connection("default")

        # query_exec_sentence = "SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score FROM students s LEFT OUTER JOIN classes c ON s.class_id = c.id;"
        query_exec_sentence = """
        SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
        FROM students s
        LEFT OUTER JOIN classes c
        ON s.class_id = c.id;
        """
        # Now we can execute queries in the normal autocommit mode
        query_result = await conn.execute_query(query_exec_sentence)
        print(query_result)

        # This transaction is rolled back
        async with in_transaction("default") as tconn:
            query_result2 = await tconn.execute_query("SELECT * FROM classes;")
            print(query_result2)
            # Rollback to fail transaction
            await tconn.rollback()

        print(a)
        print(b)

        sql = get_schema_sql(Tortoise.get_connection("default"), safe=False)
        print(sql)

    run_async(init())
