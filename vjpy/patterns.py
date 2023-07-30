"""vjpy midi pattern examples."""

from vjpy.data_classes import Pattern, Bar


# Pattern example
pattern_example = Pattern(pattern='k.h.')  # kick-silence-hat-silence

# Pattern example
bar_example = Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh'])

# Bars example
bars_example = [
    Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=2, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(bar_num=3, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=4, patterns=['k.h.', 'chhh', 'kkvv', 'cccc'])
]
