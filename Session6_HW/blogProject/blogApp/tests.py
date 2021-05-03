from django.test import TestCase

# Create your tests here.
class Test():
    def __str__(self):
        return "hello"

test_instance = Test()
print(test_instance)