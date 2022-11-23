import sys
import pyautogui
from random import sample
import time
import pyperclip as pc

lista24 = ['cave', 'box', 'priority', 'shadow', 'farm', 'orchard', 'stool', 'hazard', 'quote', 'noise', 'solar','mixed', 'minimum', 'slot', 'total', 'story', 'large', 'else', 'mean', 'search', 'impulse', 'harvest', 'insect', 'transfer']

lista9 = ['cave', 'box', 'priority', 'shadow', 'farm', 'orchard', 'stool', 'hazard', 'quote', 'noise', 'solar', 'transfer']
lista0 = ['mixed', 'minimum', 'slot', 'total', 'story', 'large', 'else', 'mean', 'search', 'impulse', 'harvest', 'insect']

lista01 = ['orchard', 'stool', 'hazard', 'quote', 'noise', 'solar','mixed', 'minimum', 'slot', 'total', 'story', 'large']

listList = []





def embaralha(lista): # retorna uma cópia da lista, só que embaralhada
    return sample(lista, k=len(lista))

# lista2 = embaralha(lista0)
x, y = pyautogui.locateCenterOnScreen('teste.png')
# 
a = True
# cor = True
while(a):
    def listar():
        lista2 = embaralha(lista24)
        pyautogui.click(x, y)

        convert = str(lista2).strip('[]')
        print(x,y)
        pc.copy(convert)
        # pc.paste()
        # for palavra in lista2:

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        # cor = pyautogui.pixelMatchesColor(2267, 498, (251, 236, 237))
        cor = pyautogui.pixelMatchesColor(2214, 666, (251, 236, 237))
# time.sleep(0.5)
        if(cor):
        
            print("Cor True")
        else:
            a = False
            
            print(convert)
            listList.append(convert)
            print(listList)
            exit()
            
        # pyautogui.press('tab')
        # pyautogui.press('tab')
            
            
        
    listar()

                
        # time.sleep(1)
        # x, y = pyautogui.locateCenterOnScreen('teste2.png')
        # pyautogui.write('Chave encontrada')
    
    

