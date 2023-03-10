import random

def main():

    d = {
        'Texas': 'Austin',
        'California': 'San Diego'
    }

    play = True
    win, loss = 0, 0

    while play:
        x = random.randint(0, len(d)-1)
        states = list(d.keys())
        user = input(f"Enter capital of {states[x]}: ")

        if user == d[states[x]]:
            print('Correct ans')
            win += 1
        else:
            print('Oops! Correct answer is: ', d[states[x]])
            loss += 1

        p = input('Hit 0 to quit')
        if p == 0:
            play = False

    print('You played:')
    print('Total: ', win + loss)
    print('Win: ', win)
    print('Loss: ', loss)


if __name__ == '__main__':
    main()
