import pandas as pd
import re

#EX_01
df = pd.read_csv("Tweets.csv")
with open("column2.txt", "w") as f:
    for i in range(len(df)):
        f.write(str(df['text'][i]))
        f.write("\n")

#EX_02
with open("column2.txt", "r") as f:
    text = f.read()

URL_PATTERN = r'https?://\S+'
new = re.sub(URL_PATTERN, '*', text)

with open("hidden_url.txt", "w") as f:
    f.write(new)

#EX_03
atsign = re.findall(r'^@.*', text)
print(atsign)

#EX_04
filtered_chars = re.sub(r"[\n+\t+' ']", '_', text)
print(filtered_chars)

#EX_05
tmp = re.findall(r"[^#.*]*[.*#$]*", text)
print(tmp)