from src.infrastructure.configurations.rabbit_mq.rabbit_configuration import setup_rabbitmq
from src.infrastructure.enums.queues_enums import Queue


class MessagePublisher:

    def __init__(self, ):
        self.queue_name = Queue.QUEUE_ANALYZE_MESSAGE_RESPONSE.value["queue"]
        self.exchange_name = Queue.QUEUE_ANALYZE_MESSAGE_RESPONSE.value["exchange"]
        self.routing_key = Queue.QUEUE_ANALYZE_MESSAGE_RESPONSE.value["routing_key"]

    def execute(self, message_analyzed):
        try:
            channel = setup_rabbitmq(self.queue_name, self.exchange_name, self.routing_key)
            channel.basic_publish(routing_key=self.routing_key,
                                  exchange=self.exchange_name,
                                  body=message_analyzed)
        except Exception as e:
            print(f'Error while publishing message, Analyze Message queue: {str(e)}')
