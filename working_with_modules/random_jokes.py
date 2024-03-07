# The random module is imported
import random

# A list of random jokes are defined
list_jokes = ["Don't worry about tests, Chuck Norris's test cases cover your code too.",
                "Chuck Norris can install iTunes without installing Quicktime', 'Why do sin and tan work? Just cos.",
                "Waiter: He's choking! Is anyone a doctor? Programmer: I'm a Vim user.",
                'Chuck Norris types with one finger. He points it at the keyboard and the keyboard does the rest.',
                'Code runs faster when Chuck Norris watches it.',
                "There are 10 types of people: those who understand binary,"
                " those who don't, and those who were expecting this joke to be in trinary.",
                'Chick Norris solved the halting problem.',
                "Chuck Norris doesn't sudo, the shell just knows it's him and does what it's told.",
                'Obfuscated Reality Mappers (ORMs) can be useful database tools.',
                "Chuck Norris's beard can type 140 words per minute.",
                'The C language combines all the power of assembly language with all the ease-of-use of assembly '
                'language.',
                'An SEO expert walks into a bar, bars, pub, public house, Irish pub, '
                'tavern, bartender, beer, liquor, wine, alcohol, spirits...',
                "When Chuck Norris breaks the build, you can't fix it, because there is not a single line "
                "of code left.",
                'Real programmers can write assembly code in any language.',
                'Speed dating is useless. 5 minutes is not enough to properly explain the benefits of '
                'the Unix philosophy.']

# The choice function in the random module selects a random joke everytime the program runs
print(random.choice(list_jokes))

# References
# https://pynative.com/python-random-choice/
