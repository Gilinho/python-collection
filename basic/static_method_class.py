
class Hello:
    @staticmethod
    def result(self, name):
        print("Hello " + name)

class World(Hello):
    pass


if __name__ == "__main__":
    World.result("", "Yodi")