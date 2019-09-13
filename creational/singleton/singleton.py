class Singleton:
    isSingleton = None

    def __new__(cls):
        if not cls.isSingleton:
            cls.isSingleton = super().__new__(cls)
        return cls.isSingleton


a = Singleton()
b = Singleton()
c = Singleton()
print(a, b, c)
# a = b = c: just the same object