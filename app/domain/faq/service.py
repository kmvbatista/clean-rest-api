from .repository import FaqRepository
from .entity  import Faq

class FaqService:
    def __init__(self):
        self.repository = FaqRepository() 

    def get_all(self):
        faqs = self.repository.get_all()
        return faqs

    def get_one(self, id):
        faq_found = self.repository.get_by_id(id)
        return faq_found

    def delete_one(self, id):
        self.repository.delete_one(id)
    
    def update_one(self, id, new_faq):
        self.repository.update(id, new_faq)

    def add__one(self, faq):
        return self.repository.insert_one(faq)