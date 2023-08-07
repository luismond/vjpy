import pandas as pd
from vjpy.data_classes import Pattern

# create a data structure that is efficient and visually convenient

h = Pattern(pattern="".join([".", ".", ".", ".", ".", ".", ".", "."]))
c = Pattern(pattern="".join([".", ".", ".", ".", ".", ".", ".", "."]))
k = Pattern(pattern="".join([".", ".", ".", ".", ".", ".", ".", "."]))

df = pd.DataFrame(zip(h.pattern, c.pattern, k.pattern)).T
cols = ["1", "2", "3", "4", "5", "6", "7", "8"]
df.columns = cols
df.index = ["h", "c", "k"]


#%%

df = pd.DataFrame(d)
df.index = sounds
