import sys

def main():
    try:
        print "Hello there %s" % sys.argv[1]
    except IndexError:
        print "No argument given"

if __name__ == '__main__':
    main()
