__author__ = 'progress'

obj = __import__('day1.aa')
mod = obj.aa.C()
print(mod.name)

import importlib
db = importlib.import_module('day1.aa')
ab = db.C()
print(ab.name)