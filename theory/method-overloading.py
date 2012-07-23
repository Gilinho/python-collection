"""
Method overloading is using same name of function with different signature
"""

class Car(object):
    """Car have function to check speed
    use pdb or ipdb to trace how python running the overloading method.
    """
    # from ipdb; ipdb.set_trace()
    def check_speed(self):
        return "no speed"

    def check_speed(self, top):
        return top

    def check_speed(self, low, top):
        return "%s %s" % (low, top)

if __name__ == '__main__':
    c = Car()
    # print c.check_speed()
    # print c.check_speed(100)
    print c.check_speed(100, 200)
