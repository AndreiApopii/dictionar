dict1={'disciplina':'Limba Romana','note':[9,9,10,10],'teza':10}
dict2={'disciplina':'Limba Engleza','note':[9,9,9,9],'teza':10}
dict3={'disciplina':'Matematica','note':[10,7,5,9],'teza':9}


x=dict1['teza']
if x<5:
    print('restanta')
y=dict2['teza']
if y<5:
    print('restanta')
z=dict3['teza']
if z<5:
    print('restanta')

x=round((((sum(dict1['note'])/4)+dict1['teza'])/2),2)
print(x)
y=round((((sum(dict2['note'])/4)+dict2['teza'])/2),2)
print(y)
z=round(((sum(dict3['note'])/4)+dict3['teza'])/2,2)
print(z)
media=(x+y+z)/3

if media>=9:
    print('eminent')

if ((media>8) and (media<9)):
    print('proeminent')

if media<8:
    print('codas')
"""
if ((x>9) and (y>9) and (z>9)):
    print('eminent')

if (((x>8) and (x<9)) and ((y>8) and (y<9))and ((z>8) and (z<9))):
    print('proeminent')

if ((x<8) and (y<8) and (z<8)):
    print('codas')

if (y>9):
    print('eminent')
if (y>8) and (y<9):
    print('proeminent')
if (y<8):
    print('codas')

if (z>9):
    print('eminent')
if (z>8) and (z<9):
    print('proeminent')
if (z<8):
    print('codas')"""
