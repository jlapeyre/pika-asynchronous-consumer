# -*- coding: utf-8 -*-
""" Example application to process messages read from a message queue.

This example is not complete: For example, to insert the messages as
records in a data base, you must supply the function `insert_db_record`
and supporting code.
"""

import aconsumer

rabbitmq_url = u'amqp://guest:guest@localhost:5672/%2F'
"url including authentication of the RabbitMQ queue server."

queue_name = u'consumer_app_test'
"Name of the queue on the server. We will consume messages from this queue."

message_count_limit = 0
""" int: Limit the number of messages consumed. A value of 0 means no limit.
Eg. with `message_count_limit = 1000`, the script will exit after consuming
1000 messages.
"""

acknowledge_message_flag = True # Do acknowledge, so that these are NOT redelivered.

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')

logging.basicConfig(filename='./consumer_app.log', level=logging.INFO, format=LOG_FORMAT)

LOGGER = logging.getLogger(__name__)

consumer = aconsumer.Consumer(rabbitmq_url)

##  ... code for inserting messages into a data base, or otherwise
##  ... processing them
##
## def connect_to_db() :
## def insert_db_record(sqlconnection, body) :

def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    sqlconnection = connect_to_db()
    on_message_callback = lambda unused_channel, basic_deliver, properties, body : insert_db_record(sqlconnection, body)
    consumer.add_on_message_callback(on_message_callback)
    consumer.set_queue(queue_name)
    consumer.set_message_count_limit(message_count_limit)
    consumer.set_acknowledge_messages(acknowledge_message_flag)

    try:
        consumer.run()
    except KeyboardInterrupt:
        consumer.stop()

if __name__ == '__main__':
    main()
