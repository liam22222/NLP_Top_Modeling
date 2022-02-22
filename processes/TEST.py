import pandas as pd

dict = {"מדינה": ["ברזיל", "רוסיה", "הודו", "סין", "דרום אפריקה"],
       "עיר בירה": ["בריסל", "מוסקווה", "ניו דלהי", "בייג'ינג", "פרטוריה"],
       "אזור": [8.516, 17.10, 3.286, 9.597, 1.221],
       "אוכלוסייה": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
brics.to_excel("brics.xlsx", encoding="UTF-8")