from tortoise import models, Tortoise, fields


class User(models.Model):
    """User类"""
    id = fields.IntField(pk=True)
    phone_nation_code = fields.CharField(8, null=True)
    email = fields.CharField(256, null=True)
    account_password = fields.CharField(128)
    account_password_salt = fields.CharField(10)
    pay_password = fields.CharField(128, null=True)
    pay_password_salt = fields.CharField(10, null=True)
    

    class Meta:
        table = 'user_account'