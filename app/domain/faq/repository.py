from .entity import Faq
from app.infrastructure.BaseRepository import BaseRepository

class FaqRepository(BaseRepository[Faq]):
    def __init__(self):
        BaseRepository.__init__(self, 'faqs')