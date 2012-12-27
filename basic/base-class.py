class Base(object):
    def go(self):
        raise NotImplementedError("Please implement this method")

class Specialized(Base):
    def go(self):
        print "Consider Me implemented!"

if __name__ == '__main__':
    c = Specialized()
    c.go()
