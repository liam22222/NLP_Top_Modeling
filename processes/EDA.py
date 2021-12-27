from functools import lru_cache
from collections import deque
import matplotlib
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import take
import itertools

@lru_cache(maxsize=1024)
def n_words_frequency(document: str, numberOfWords = 1) -> dict:
    """
    This function returns a sorted dict that contatins the frequency of words in document
    """
    words = document.split()
    queue = deque()
    dict = {}
    update_dict = dict.update
    append_right = queue.append
    pop_left = queue.popleft
    for idx, word in enumerate(words):
        # We need to create the queue
        if idx < numberOfWords - 1:
            append_right(word)
        
        # Queue size equals to numOfWords
        else:
            append_right(word)
            expre = ' '.join(queue)
            
            if expre in dict:
                dict[expre] += 1
            
            else:
                update_dict({expre : 1})
            pop_left()
            

            


            

    return {k[::-1] : v for k, v in sorted(dict.items(), reverse=True, key=lambda item: item[1])}

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
    plt.title("מספר החזרות בטקסט"[::-1], **hebrew_font)
    plt.bar(d.keys(), d.values())
    plt.show()