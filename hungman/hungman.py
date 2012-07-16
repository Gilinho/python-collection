import random
import re


class HungMan(object):
    """Prediction games by words.txt with 6 changes for guessing."""

    def answer(self):
        dictionary = []
        with open('words.txt') as w:
            for line in w:
                dictionary.append(line.strip())

        return dictionary[random.randint(0, len(dictionary))]


if __name__ == '__main__':
    hungman = HungMan()
    answer = hungman.answer()
    print answer
    chances = 6

    hung = []
    for a in range(0, len(answer)):
        hung.append('_')
    print('====================== HUNGMAN =========================== \n')
    print(hung)

    while chances > 0:
        man = raw_input("Pick a letter : ")
        if len(man) > 1:
            print("Only one letter allowed")
        elif len(man) < 1:
            print("Please choose a letter")
        else:
            position = [w.start() for w in list(re.finditer(man, answer))]

            if not position:
                chances = chances - 1
                print("Oops, wrong letter!")
                print("Your chances : %d times \n" % chances)

            else:
                error = success = 0
                for index in position:
                    if hung[index] == man:
                        error = 1
                    else:
                        success = 1
                        hung[index] = man

                if success:
                    print(hung)
                    if not any('_' == x for x in hung):
                        print 'Success HUNGMAN!'
                        break
                elif error:
                    print('already typed before')
