from app.infrastructure.BaseEntity import BaseEntity

class Faq(BaseEntity):
    def __init__(self, title, description):
        BaseEntity.__init__(self, 'faqs', title, description)
