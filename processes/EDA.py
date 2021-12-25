from functools import lru_cache
import matplotlib
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import take
import itertools

@lru_cache(maxsize=1024)
def one_word_frequency(document: str) -> dict:
    """
    This function returns a sorted dict that contatins the frequency of words in document
    """
    words = document.split()
    dict = {}
    update = dict.update
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            update({word : 1})
    return {k : v for k, v in sorted(dict.items(), reverse=True, key=lambda item: item[1])}

def plot_histogram(d: dict, size: int):
    """
    Plotting Histogram in size of size or max
    """
    hebrew_font = {'fontname': 'Adobe Hebrew'}
    if size > len(d):
        pass
    else:
        d = dict(itertools.islice(d.items(), size)) 

    plt.figure(figsize=(14,7)) # Make it 14x7 
    plt.style.use('seaborn-whitegrid') # Nice and clean grid

    plt.rcParams["font.family"] = 'Adobe Hebrew'
    plt.title("ליאם", **hebrew_font)
    plt.bar(d.keys(), d.values())
    plt.show()