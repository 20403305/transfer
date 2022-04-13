import pika

# 使用用户名和密码创建登录凭证对象
credentials = pika.PlainCredentials('super', 'eyJ...')
# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='amqp-...qcloud.tencenttdmq.com', port=5075, virtual_host='amqp...|vhost_1', credentials=credentials))
# 建立信道
channel = connection.channel()
# 声明交换机
channel.exchange_declare(exchange='direct_exchange', exchange_type="direct")

routingKeys = ['aaa.bbb.ccc', 'aaa.bbb.ddd', 'aaa.ccc.zzz', "xxx.yyy.zzz"]

for routingKey in routingKeys:
    # 发送消息到指定的交换机
    # 不指定交换机的情况下发送消息，需要指定消息队列，参数routing_key在使用指定交换机时，表示routing_key，不指定交换机时代表消息队列名称
    channel.basic_publish(exchange='direct_exchange',
                          routing_key=routingKey,
                          body=(routingKey + 'This is a new direct message.').encode(),
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # 设置消息持久化
                          ))
    print('send success msg to rabbitmq')
connection.close()