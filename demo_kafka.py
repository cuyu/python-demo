"""
Refer to http://kafka-python.readthedocs.io/en/master/usage.html
"""
import json
import msgpack
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from kafka.errors import KafkaError

_TOPIC_NAME = 'forecast_weather'
_BROKERS = ['health.sv.splunk.com:9092', 'systest-auto-deployer:9092']
_GROUP_ID = 'my_group'


def produce():
    producer = KafkaProducer(bootstrap_servers=_BROKERS)

    # Asynchronous by default
    future = producer.send(_TOPIC_NAME, b'raw_bytes')

    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError, e:
        # Decide what to do if produce request failed...
        raise e

    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)

    # # produce keyed messages to enable hashed partitioning
    # producer.send('my-topic', key=b'foo', value=b'bar')

    # # encode objects via msgpack
    # producer = KafkaProducer(value_serializer=msgpack.dumps)
    # producer.send('msgpack-topic', {'key': 'value'})

    # produce json messages
    producer = KafkaProducer(bootstrap_servers=_BROKERS, value_serializer=lambda m: json.dumps(m).encode('ascii'))
    producer.send(_TOPIC_NAME, {'key': 'value'})

    # produce asynchronously
    for i in range(10):
        producer.send(_TOPIC_NAME, b'msg{0}'.format(i))

    # block until all async messages are sent
    producer.flush()

    # configure multiple retries
    # producer = KafkaProducer(retries=5)


def consume():
    # To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer(group_id='ddd',
                             auto_offset_reset='earliest',
                             enable_auto_commit=False,
                             bootstrap_servers=_BROKERS)
    # consumer.assign([TopicPartition(_TOPIC_NAME, 0), TopicPartition(_TOPIC_NAME, 1)])
    consumer.subscribe(topics=[_TOPIC_NAME])
    # partition = TopicPartition(topic=_TOPIC_NAME, partition=consumer.partitions_for_topic(_TOPIC_NAME))
    # consumer.seek_to_beginning()
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                              message.offset, message.key,
                                              message.value))

    # consume earliest available messages, dont commit offsets
    KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

    # # consume json messages
    # KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))
    #
    # # consume msgpack
    # KafkaConsumer(value_deserializer=msgpack.unpackb)

    # StopIteration if no message after 1sec
    KafkaConsumer(consumer_timeout_ms=1000)

    # Subscribe to a regex topic pattern
    consumer = KafkaConsumer()
    consumer.subscribe(pattern='^awesome.*')

    # Use multiple consumers in parallel w/ 0.9 kafka brokers
    # typically you would run each on a different server / process / CPU
    consumer1 = KafkaConsumer('my-topic',
                              group_id='my-group',
                              bootstrap_servers=_BROKERS)
    consumer2 = KafkaConsumer('my-topic',
                              group_id='my-group',
                              bootstrap_servers=_BROKERS)


if __name__ == '__main__':
    # produce()
    consume()
