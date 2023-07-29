"""vjpy midi pattern examples."""

from vjpy import Pattern, Bar


# Pattern example
pattern = Pattern(pattern='k.h.')

# Pattern example
bar_ = Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh'])

# Bars example
bars = [
    Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=2, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(bar_num=3, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=4, patterns=['k.h.', 'chhh', 'kkvv', 'cccc']),
    Bar(bar_num=5, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=6, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(bar_num=7, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=8, patterns=['k.h.', 'chhh', 'kkkk', 'cccc'])
]
