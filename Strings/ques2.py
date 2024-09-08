# write a program to fill in a letter template given below with name date 

letter='''Dear<|Name|>,
you are selected
<|Date|>'''

print(letter.replace("<|Name|>","ROHIT").replace("<|Date|>","24th September 2024"))