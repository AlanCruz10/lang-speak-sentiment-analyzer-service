from src.application.dtos.requests.analyze_message_request import AnalyzeMessageRequest
from src.application.dtos.responses.analysis_response import AnalysisResponse
from src.application.utilities.text_cleaner import clean_text
from src.application.utilities.profanity_filter import profanity


class AnalyzeMessageUseCase:
    def __init__(self, analytic_sentiments_multilingual):
        self.analytic_sentiments_multilingual = analytic_sentiments_multilingual

    def analyze_message(self, message: str) -> tuple:
        text = clean_text(message)
        analyze = self.analytic_sentiments_multilingual(message)

        sentiment = analyze[0]['label']
        score = analyze[0]['score']
        # tokens = word_tokenize(text)

        if sentiment in ['1 star', '2 stars'] or (sentiment in ['4 stars', '5 stars'] and score < 0.8):
            filtered_text = profanity.censor(text=text, censor_char="*")
            muted = True
        else:
            filtered_text = text
            muted = False

        return filtered_text, sentiment, score, muted

    def execute(self, request: AnalyzeMessageRequest):
        text, sentiment, score, muted = self.analyze_message(request.content)
        response = AnalysisResponse(content=text,
                                    sentiment=sentiment,
                                    score=score,
                                    type=request.type,
                                    user_id=request.user_id,
                                    uuid=request.uuid,
                                    muted=muted)
        return response
