import random

from colorama import Fore, Style
possible_answers = [
    'japan', 'rainy', 'night', 'daily', 'about', 'reset', 'slate', 'stalk', 'crane', 'frame',
    'niger', 'state', 'modes', 'moody', 'arson', 'crank', 'diner', 'place', 'timed', 'lanes',
    'print', 'later', 'crate', 'fonts', 'pills', 'pines', 'wines', 'fairy', 'fable', 'rhine',
    'raise', 'whine', 'stops', 'norms', 'fifth', 'sixth', 'seven', 'siren', 'exits', 'prime',
    'aztec', 'mayan', 'unite', 'union', 'shade', 'slick', 'nanny', 'vague', 'giant', 'flick',
    'press', 'phone', 'lakes', 'woods', 'fines', 'dives', 'lines', 'enter', 'laser', 'parse',
    'roman', 'greek', 'races', 'cared', 'limes', 'lemon', 'camel', 'pasta', 'llama', 'debug',
    'whose', 'which', 'racer', 'water', 'salty', 'proof', 'prove', 'where', 'hours', 'known',
    'three', 'first', 'eight', 'sassy', 'faker', 'duped', 'dupes', 'dukes', 'duchy', 'seals',
    'penny', 'cones', 'legit', 'favor', 'prick', 'riser', 'riffs', 'mines', 'fails', 'fiery',
    'bones', 'jelly', 'dimes', 'nutty', 'eagle', 'cries', 'cream', 'waves', 'flaws', 'error',
    'train', 'manic', 'sauce', 'study', 'earth', 'micro', 'taser', 'tease', 'yummy', 'pizza'
]
answers = random.choices(possible_answers, k=(g := min([int(input(f'Amount of words to guess (max. {len(possible_answers)}): ')), len(possible_answers)])))


def make_unequal(lst: list, clst):
    for i, v in enumerate(lst):
        lst_copy = lst.copy()
        lst_copy.pop(i)
        while lst[i] in lst_copy:
            lst[i] = random.choice(clst)

    return lst


def colorize_guess(guess, actual):
    code = ''
    for i, v in enumerate(guess):
        if v in actual:
            if v == actual[i]:
                code += 'R'
                actual = actual.replace(v, ' ', 1)
            else:
                code += 'W'
                actual = actual.replace(v, ' ', 1)
        else:
            code += ' '
    l_guess = list(guess)
    Dl_guess = l_guess.copy()
    for i, v in enumerate(Dl_guess):
        l_guess.insert(2 * i, Fore.GREEN if (char := code[i]) == 'R' else (Fore.YELLOW if char == 'W' else Fore.RESET))
    return ''.join(l_guess) + Style.RESET_ALL


def beautify_list(lst):
    result = ''
    for i, v in enumerate(lst):
        if i < len(lst) - 1:
            result += v + ', '
        else:
            result += v
    return result


answers = make_unequal(answers, possible_answers)

guess = ''

l_guess = [''] * g

won = [False] * g
won_all = False

modes = {'practice': 'infinite', 'easiest': 20 * g, 'very easy': 12 * g, 'easy': 8 * g, 'normal': 6 * g, 'hard': 4 * g, 'extra hard': 3 * g, 'one-at-a-time': g}
print('Modes:')
for k, v in modes.items():
    print(f'\t{k}: {v} {"guess" if v == 1 else "guesses"}')

guess_amt = modes[input(f'Enter mode: ').lower()]

guesses = 1

if guess_amt != 'infinite':
    for i in range(guess_amt):
        print(f'Guesses left: {guess_amt - (guesses - 1)}')
        guess = input('Guess a word: ')
        while guess.__len__() != 5:
            guess = input('   Try again: ')

        if not won_all:
            print(' ' * 14, end='')

            for j, w in enumerate(won):
                if w:
                    print(' ' * 6, end='')
                else:
                    print(colorize_guess(guess, answers[j]) + ' ', end='')
                    l_guess[j] = guess

            print()

        for j, w in enumerate(answers):
            if guess == w:
                won[j] = True

        for j in won:
            if not j:
                break
        else:
            won_all = True

        if won_all:
            break

        guesses += 1
else:
    while True:
        guess = input('Guess a word: ')
        while guess.__len__() != 5:
            guess = input('   Try again: ')

        if not won_all:
            print(' ' * 14, end='')

            for j, w in enumerate(won):
                if w:
                    print(' ' * 6, end='')
                else:
                    print(colorize_guess(guess, answers[j]) + ' ', end='')
                    l_guess[j] = guess

            print()

        for j, w in enumerate(answers):
            if guess == w:
                won[j] = True

        for i in won:
            if not i:
                break
        else:
            won_all = True

        if won_all:
            break

        guesses += 1

mws = f'all {g}'

if won_all:
    print(f'Hooray! You solved {mws if g > 1 else "the word"} in {guesses} {"guess" if guesses == 1 else "guesses"}!')

else:
    print(f'You lost, but you tried your best. {"Answer" if len(l_guess) == 1 else "Answers"}: {beautify_list(answers)}')

input()
