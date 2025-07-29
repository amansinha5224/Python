'''
Getters:-
    - Methods which behaves like a property
Setters:-
    - It is use to set the property
'''

class myClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    # Getter
    @property
    def ten_value(self):
        return 10*self._value
    
    # Setter
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10

obj = myClass(5)
obj.show()
print(obj.ten_value)
obj.ten_value = 67
obj.show()