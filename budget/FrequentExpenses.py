# -*- coding: utf-8 -*-
"""
@author: Cameron Hill
"""

from . import Expense
import collections

expenses = Expense.Expense()
expenses.read_expenses("data/spending_data.csv")


spending_categories = []


for expense in expenses.list:
    spending_counter = collections.Counter(spending_categories)
    spending_categories.append(expense.category)
    



