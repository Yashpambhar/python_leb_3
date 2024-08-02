class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child")

child_obj = Child(

child_obj.method1()
child_obj.method2()
child_obj.method3()

output :-
![pro3](https://github.com/user-attachments/assets/4e0f92d3-7740-4f31-893b-153f44db435b)
