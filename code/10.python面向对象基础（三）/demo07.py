# 单例设计模式


class Singleton(object):
    __instance = None  # 标志位用来控制是否有新的对象生产
    __is_first = True  # 控制__init__方法只执行一次

    def __new__(cls, *args, **kwargs):  # 创建对象的方法
        # 如果类属性__instance的值为None，
        # 那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
        # 能够知道之前已经创建过对象了，这样就保证了只有1个对象

        if not cls.__instance:
            print("创建一个对象")
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self, *args, **kwargs):
        if self.__is_first:
            self.age = args[0]
            self.name = args[1]
            Singleton.__is_first = False


a = Singleton(18, "haha")
b = Singleton(20, "hahah")

print(id(a))
print(id(b))

print(a.age)
print(b.age)

a.age = 20
print(b.age)
