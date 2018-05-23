# Asynchronous pika consumer

## Description

This class implements an asynchronous RabbitMQ consumer. It is based on the
[pika example](https://pika.readthedocs.io/en/0.11.2/examples/asynchronous_consumer_example.html) with
modifications for general use.
For instance, this modified class can be used to insert the messages in a database, or otherwise process them.

> Pika is a pure-Python implementation of the AMQP 0-9-1 protocol including RabbitMQ's extensions.

## Features added

* Accept a callback for processing messages. The original writes messages to a log file.

* Handle and logs error in connecting to the publisher.

* Log the number of messages read and the number of messages for which processing failed.

* Add class member data fields to select
  * the name of the queue.
  * whether to acknowledge receipt.
  * closing the connection after reading a given number of messages.

## Notes

The consumer class is in `aconsumer.py`. All changes to the original
example of an asynchronous consumer are marked with a comment and two
exclamation points `!!`. The file `consumer_app.py` is an example
application using this class `aconsumer.py`. The example application
cannot be executed as is. The code and callback for processing the
messages must be written by the user.


 <!-- LocalWords:  pika RabbitMQ AMQP RabbitMQ's aconsumer py -->
