"""vjpy midi pattern examples."""

from vjpy.data_classes import Pattern, Bar


# Pattern examples (define a pattern generator)

pattern_example_0 = Pattern(
    pattern='k.h.sshhh.s.s.k.k.h.s.h.h.k.s.h.k.h.s.hhhhk.s.h.h.h.s.k.k.s.s.h')
pattern_example_1 = Pattern(
    pattern='k.h.s.h.h.s.s.k.k.h.s.h.h.k.s.h.k.h.s.h.h.k.s.h.h.h.s.k.k.s.s.h')
pattern_example_2 = Pattern(
    pattern='k.h.s.k.k.h.s.k.k.h.s.h.h.k.s.h.k.h.s.k.k.h.s.h.k.h.s.h.h.k.s.h')
pattern_example_3 = Pattern(
    pattern='k.h.s.k.h.s.k.h.k.h.s.k.h.s.k.h.k.h.s.k.h.k.s.h.s.h.s.h.s.h.s.k')
pattern_example_4 = Pattern(
    pattern='k.h.s.k.h.k.s.k.h.k.s.h.k.h.s.k.h.h.s.k.h.k.s.h.k.h.s.k.h.k.s.s')
pattern_example_5 = Pattern(
    pattern='k.h.s.k.h.k.s.k.h.k.s.h.k.h.s.k.h.h.s.k.h.k.s.h.k.s.h.k.s.h.k.k')

pattern_examples = [pattern_example_0, pattern_example_1, pattern_example_2,
                    pattern_example_3, pattern_example_4, pattern_example_5]

# Bar example
bar_example = Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh'])

# Bars example
bars_example = [
    Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=2, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(bar_num=3, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=4, patterns=['k.h.', 'chhh', 'kkvv', 'cccc'])
]
