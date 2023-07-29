"""vjpy midi pattern examples."""

from vjpy import Pattern, Bar


# Pattern example
pattern = Pattern(pattern='k.h.')

# Pattern example
bar_ = Bar(num=1, content=['t.h.', 'chhh', 'thhh', 'chhh'])

# Bars example
bars = [
    Bar(num=1, content=['t.h.', 'chhh', 'thhh', 'chhh']),
    Bar(num=2, content=['t.h.', 'chhh', 'thhh', 'cchh']),
    Bar(num=3, content=['t.h.', 'chhh', 'thhh', 'chhh']),
    Bar(num=4, content=['t.h.', 'chhh', 'ttvv', 'cccc']),
    Bar(num=5, content=['t.h.', 'chhh', 'thhh', 'chhh']),
    Bar(num=6, content=['t.h.', 'chhh', 'thhh', 'cchh']),
    Bar(num=7, content=['t.h.', 'chhh', 'thhh', 'chhh']),
    Bar(num=8, content=['t.h.', 'chhh', 'tttt', 'cccc'])
]
