import uuid
import datetime

class Expense:
    def __init__(self, title, amount):
        self.id=str(uuid.uuid4()) #To generate a Unique ID
        self.title = title
        self.amount = amount
        self.created_at = datetime.datetime.utcnow() #The current UTC time
        self.updated_time = self.created_at

    def update(self, title=None, amount = None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.datetime.utcnow() #Update timestamp
    
    def to_dict(self):
        return{
            "id" : self.id,
            "title" : self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(), #Format as string
            "updated_at": self.updated_at.isoformat()
        }
        
        
class ExpenseDB:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, expense):
        self.expenses.append(expense)
        
    def remove_expense(self, expense_id):
        self.expenses = [e for e in self.expenses if e.id != expense_id]
    
    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None #Return None if not found
    
    def get_expenses_by_titlte(self, title):
        return[e for e in self.expenses if e.title == title]
    
    def to_dict(self):
        return[expense.to_dict() for expense in self.expenses]