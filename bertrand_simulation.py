import random
import sys

"""
Short script by Michael Zeevi to simulate the result of the Bertrand's box paradox:

    There are three boxes:
      1. a box containing two gold coins,
      2. a box containing two silver coins,
      3. a box containing one gold coin and a silver coin.
    The 'paradox' is in the probability, after choosing a box at random and withdrawing
    one coin at random, if that happens to be a gold coin, of the next coin also being
    a gold coin.

Description from https://en.wikipedia.org/wiki/Bertrand's_box_paradox
17/1/2017
"""

def simulation(cases = 10000):
    counts = {
               'cases': cases,
               'first': {
                         'gold': 0,
                         'silver': 0
                        },
               'second': {
                         'gold': 0,
                         'silver': 0
                        }
              }

    print('\nRunning simulations...')

    for trial in range(cases):
        boxes = [
                 ['gold', 'gold'],
                 ['gold', 'silver'],
                 ['silver', 'silver']
                ]

        box = random.choice(boxes)
        first = random.choice(box)
        counts['first'][first] += 1

        if first == 'gold':
            box.remove('gold')
            second = random.choice(box)
            counts['second'][second] += 1

    return counts

def main():
    print('\n\tWelcome to Bertrand\'s box simulation by Michael Zeevi.')
    print('\tFor more information see source code at github (https://github.com/maze88/bertrand_simulation).')  # insert link!
    print('\tAmount of test cases can be adjusted by adding optional argument after bertrand_simulation.py.')
    print('\tDefault number of test cases is 10000. Recommended value: 10^4 < cases < 10^6')

    try:
        cases = abs(int(sys.argv[1]))
        results = simulation(cases)
    except:
        results = simulation()

    # analysis
    results['first']['gold_percent'] = 100 * results['first']['gold'] / results['cases']
    results['second']['gold_percent'] = 100 * results['second']['gold'] / results['first']['gold']
    results['second']['silver_percent'] = 100 * results['second']['silver'] / results['first']['gold']

    print('Complete!\n')
    print('\tOut of {r[cases]} test cases, in {r[first][gold]} cases (~{r[first][gold_percent]}%) where the first coin was gold:'.format(r = results))
    print('\tThe second coin was gold in {r[second][gold]} cases (~{r[second][gold_percent]}%).'.format(r = results))
    print('\tThe second coin was silver in {r[second][silver]} cases (~{r[second][silver_percent]}%).'.format(r = results))
    print('\nQuitting...\n')


if __name__ == '__main__':
    main()
