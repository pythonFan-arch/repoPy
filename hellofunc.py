# a simple oop hello class that return hello world for pushing into a github

class HelloWorld:
    def __init__(self, greeting):
        self.greeting = greeting

    @property
    def showHellomsg(msg):
        if msg == "":
            return None
        else:
            return msg

obj = HelloWorld('hello')
print(obj.showHellomsg(msg='Im programmer'))
