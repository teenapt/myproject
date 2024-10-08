# Django-Signals-And-Python-Custom-Class-Task

##Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.<br>
answer:By default, Django signals are executed synchronously. This means that when a signal is sent, all connected signal handlers are executed in the order they were connected, and the original code execution will wait until all handlers have completed.

```# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler executed synchronously.")

# Usage

instance = MyModel(name="Test")
instance.save()

```
##Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.<br>
Yes, Django signals run in the same thread as the caller by default. This means that when a signal is sent, the signal handlers are executed in the same thread that triggered the signal, and the execution of the caller waits until all signal handlers have completed.<br>
```import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler running in thread:", threading.current_thread().name)

# Usage

instance = MyModel(name="Test")
instance.save()
```

##Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.<br>
Django signals run in the same database transaction as the caller. Django's signals, such as post_save, are executed within the same transaction that triggered them. This means that if the transaction is rolled back, the effects of the signal handlers will also be rolled back.
```from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    if kwargs.get('created', False):
        print("Signal handler executed within transaction.")

# Usage

with transaction.atomic():
    instance = MyModel(name="Test")
    instance.save()
    # If an exception occurs here, the transaction (and signal) will be rolled back.
```

##Topic: Custom Classes in Python<br>
Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}
```
 def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
# Example usage:
rect = Rectangle(5, 3)

for value in rect:
    print(value)
```





