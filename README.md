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

## Files

* [aconsumer.py](aconsumer.py)  &nbspc; &mdash; &nbspc;  The consumer class.
* [consumer_app.py](consumer_app.py) &nbspc; &mdash; &nbspc; Example application using the consumer class.

## Notes

All changes to the original example of an asynchronous consumer are marked with a comment and two
exclamation points `!!`.


 <!-- LocalWords:  pika RabbitMQ AMQP RabbitMQ's aconsumer py -->
