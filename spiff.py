
#this is jank
#start it, you got 5s to click onto the input field in youtube chat, then every 2 s it will load a line from the csv and keep going
#fuckit to cancel it break since i don't include something to do that
#i coded this in like, 2 minutes

import pandas as pd
import pyautogui as pa
import time as t

inp = 'c:\GitHub\spiff-spam\input.csv'
df = pd.read_csv(inp, sep = '#', header = None)

df = df.rename(columns={0:'qval'})

print (df)

i = len(df)
v = 0
q = ''

t.sleep(5)

while i > v:

    q = df['qval'].iloc[v]
    pa.write(q, interval = 0.0001)
    pa.press('enter')
    v = v + 1
    t.sleep(2)