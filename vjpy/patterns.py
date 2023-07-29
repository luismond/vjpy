"""vjpy midi pattern examples."""

from vjpy import Pattern, Bar


# Pattern example
pattern = Pattern(pattern='k.h.')

# Pattern example
bar_ = Bar(num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh'])

# Bars example
bars = [
    Bar(num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(num=2, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(num=3, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(num=4, patterns=['k.h.', 'chhh', 'kkvv', 'cccc']),
    Bar(num=5, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(num=6, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(num=7, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(num=8, patterns=['k.h.', 'chhh', 'kkkk', 'cccc'])
]
