class Base(object):
    def show_number(self, number):
        return number


class Child(Base):
    def show_number(self, number):
        return number ** number


if __name__ == '__main__':
    b = Base()
    print b.show_number(5)

    c = Child()
    print c.show_number(5)
