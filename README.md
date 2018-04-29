# Asynchronous pika consumer

## Description

This is the [example of an asynchronous RabbitMQ consumer](https://pika.readthedocs.io/en/0.11.2/examples/asynchronous_consumer_example.html)
included in the [pika](https://github.com/pika/pika) documentation, modified to be more generally useful.
For instance, this modified class can be used to insert the messages in a database, or otherwise process them.

> Pika is a pure-Python implementation of the AMQP 0-9-1 protocol including RabbitMQ's extensions.

## Modifications

A few simple modifications to the example have been made that allow it to be used in application code.

* The original example consumes messages and writes them the the `logger` log file. The modified consumer class accepts a callback for
processing messages.

* The modified consumer handles errors in connecting to the publisher. Namely, it writes a message to the log file.

* Member data fields are included for 1) selecting the name of the queue. 2)selecting whether to acknowledge the messages.
  3) closing the connection after reading a given number of messages. 4) recording the number of messages read and the number of
  messages for which processing failed.

## Notes

The consumer class is in `aconsumer.py`. All changes to the original example of an asynchronous consumer are marked with a comment and two
exclamation points `!!`. The file `consumer_app.py` is an example application using `aconsumer.py`. The example application cannot be
executed as is. The code and callback for processing the messsages must be written by the user.

