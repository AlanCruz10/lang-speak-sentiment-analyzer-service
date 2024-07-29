import json

from src.application.dtos.requests.analyze_message_request import AnalyzeMessageRequest
from src.infrastructure.enums.queues_enums import Queue
from src.infrastructure.configurations.rabbit_mq.rabbit_configuration import setup_rabbitmq


class MessageConsumer:
    def __init__(self, analyze_service_port_input, message_publisher):
        self.message_publisher = message_publisher
        self.analyze_service_port_input = analyze_service_port_input
        self.queue_name = Queue.QUEUE_ANALYZE_MESSAGE_REQUEST.value["queue"]
        self.exchange_name = Queue.QUEUE_ANALYZE_MESSAGE_REQUEST.value["exchange"]
        self.routing_key = Queue.QUEUE_ANALYZE_MESSAGE_REQUEST.value["routing_key"]

    def execute(self):
        try:
            channel = setup_rabbitmq(self.queue_name, self.exchange_name, self.routing_key)
            channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
            channel.start_consuming()
        except Exception as e:
            print(f'Error while consuming message, Analyze Message queue: {str(e)}')

    def callback(self, ch, method, properties, body):
        request = json.loads(body)
        message_request = AnalyzeMessageRequest(content=request['content'], type=request['type'],
                                                user_id=request['user_id'], uuid=request['uuid'])
        analyzed = self.analyze_service_port_input.analyze(message_request)
        self.message_publisher.execute(analyzed)
