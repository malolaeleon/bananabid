import os

for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or not module.endswith('.py'):
        continue
    __import__("bots." + module[:-3], locals(), globals())