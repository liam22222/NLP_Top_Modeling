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

d = """
. להפחית מלח בהדרגה
מומחים ממליצים להפחית את כמות הנתרן/ המלח בתפריט היומי כדי לשמור על אורח חיים בריא, אך יש לעשות זאת באופן הדרגתי. הפחתה בבת אחת תגרום למזון להפוך להיות תפל, ותגרום לנו להמליח את המזון בחזרה יתר על המידה.

 

3. עלול לגרום ליתר לחץ דם
לנתרן תפקידים רבים וחשובים בגוף האדם, אך צריכה גבוהה שלו עלולה לגרום ליתר לחץ דם המגביר את הסיכון לשבץ מוחי, מחלות לב וכלי דם ואי ספיקת כליות.

 

4. כמה צריך לצרוך?
ההמלצות לצריכת נתרן למבוגר בישראל הן: 1,500 מ"ג נתרן ליום, גבול מירבי של 2,000-2,400 מ"ג ליום, כמות שוות ערך ל-5-6 גרם מלח (כפית לערך). אולם ההמלצות לילדים נמוכות יותר. ילדים בגילאי 1-3, 4-8, 9-13 לא צריכים לעבור כמות של 1.5, 1.9, ו-2.2 גרם ביממה בהתאמה. מסקרי בריאות בעולם עולה כי מרבית האנשים צורכים פי 2 מהמלצות אלה.

 

5. המלח כחומר משמר
המלח מוסף למזון בתעשייה לא רק לשם הטעם (במוצרי מזון מתוקים ישנם כמויות גבוהות של מלח) אלא גם כחומר משמר, לבניית מרקם המזון לויסות תהליכי תסיסה, לפיתוח הצבע ועוד. המלח מופיע בעוד שמות על גב האריזה.

 

6. אוכלים  יותר ג'אנק פוד
בקרב ילדים ונוער צריכת הנתרן גבוהה יותר ממבוגרים וזאת בשל צריכה גבוהה יותר של מזון מתועש וחטיפים.

 

7. עלייה בלחץ דם
ביולי השנה פורסם מחקר בירחון הרפואי Hypertension בו השוו בין סקר בריאות שנעשה בשנים 1988-1994 (3,248 ילדים בגילאי 8-17) לבין סקר שנעשה בשנים 1998-2008 (8,388 ילדים באותם גילאים). שכיחות יתר לחץ הדם עלתה מ-15.8% ל-19.2% בבנים ומ-8.2% ל-12.6% בבנות.

 

8. סיכון לחלות בשבץ מוחי
כל ירידה ב-300 מ"ג נתרן בממוצע באוכלוסיה תגרום לירידה של 1 מ"מ כספית בלחץ הדם. כל ירידה ב-1 מ"מ כספית יפחיתו את הסיכון היחסי של שבץ מוחי בכ-5%.2. חשוב לדעת כי 51% ממקרי השבץ המוחי וכ-45% ממחלות הלב האיסכמיות ניתן ליחסן ללחץ דם גבוה.

 

9. תוכנית לאומית להפחתת צריכת המלח
מטרת התוכנית הלאומית של משרד הבריאות להפחית את צריכת המלח הממוצעת באוכלוסייה הישראלית ב-3 גרם כך שהצריכה הממוצעת תעמוד על 6 גרם מלח ליום בשנת 2020. לצורך הפחתת המלח יוטמעו הרגלי תזונה ויופחת באופן הדרגתי כמות הנתרן במזון המתועש בשיתוף עם חברות תעשיית המזון ובהובלת משרד הבריאות.

 

10.  הפחתת נתרן - ירידה במשקל
הגישה התזונתית הנהוגה נקראת- DASH- Diet Approach to Stop Hypertension הגישה התזונתית למנוע/ לטפל ביתר לחץ דם והיא כוללת הפחתת נתרן, הגברת סידן ואשלגן, ירידה במשקל והגברת פעילות גופנית. גישה זו הוכחה כיעילה בהורדת לחץ דם כמו טיפול בתרופה בודדת ללחץ דם.

 

הכותבת היא מנהלת היחידה לתזונה ודיאטה, בית חולים בילינסון
"""

liam = n_words_frequency(d,2)
#plot_histogram(liam,10)