# import threading
# import time
from src.infrastructure.adapters.ports.inputs.controllers.analyzer_controller import router as router_analyzer
# from src.infrastructure.adapters.ports.inputs.consumers.message_consumer import MessageConsumer
# from src.application.ports.inputs.analyzer_service_port_input import AnalyzerServicePortInput
# from src.infrastructure.adapters.ports.outputs.publishers.message_publisher import MessagePublisher
# from src.application.services.analyzer_service import AnalyzerService
# from src.application.services.use_cases.analyze_message_use_case import AnalyzeMessageUseCase
# from src.application.utilities.sentiment_analyze_models import analytic_sentiments_multilingual
#
# message_use_case = AnalyzeMessageUseCase(analytic_sentiments_multilingual)
# service = AnalyzerService(message_use_case)
#
# message_publisher = MessagePublisher()
#
# message_consumer = MessageConsumer(service, message_publisher)


def init_routers(app):
    app.include_router(router_analyzer, prefix='/analysis/api')

# def run():
#     while True:
#         message_consumer.execute()
#         time.sleep(1)
#
#
# def init_rabbitmq():
#     thread = threading.Thread(target=run)
#     thread.daemon = True
#     thread.start()
