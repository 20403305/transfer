import json
import pika

rabbit_setting = {
    'rolename': 'developer',
    'secret_key': 'eyJrZ...',
    # 'host': 'amqp-....qcloud.tencenttdmq.com',
    # 'port': 5102,
    'host': 'amqp-a....public.tencenttdmq.com',
    'port': 5672,
    'virtual_host': 'amqp-...|...',
    'exchange': 'sync_msg',
    'exchange_type': 'direct',
    'routing_keys': ['a...s', ],
    'queue': 'msg_handle',
}


# 使用用户名和密码创建登录凭证对象
credentials = pika.PlainCredentials(rabbit_setting['rolename'],
                                    rabbit_setting['secret_key'])
# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=rabbit_setting['host'],
    port=rabbit_setting['port'],
    virtual_host=rabbit_setting['virtual_host'],
    credentials=credentials))
# 建立信道
channel = connection.channel()
# 声明交换机
channel.exchange_declare(exchange=rabbit_setting['exchange'], exchange_type=rabbit_setting['exchange_type'])


for routingKey in rabbit_setting['routing_keys']:
    # 发送消息到指定的交换机
    # 不指定交换机的情况下发送消息，需要指定消息队列，参数routing_key在使用指定交换机时，表示routing_key，不指定交换机时代表消息队列名称
    channel.basic_publish(exchange=rabbit_setting['exchange'],
                          routing_key=routingKey,
                          body=json.dumps({'id': 1}, ensure_ascii=False).encode('utf-8'),
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # 设置消息持久化
                          ))
    print('send success msg to rabbitmq')
connection.close()


