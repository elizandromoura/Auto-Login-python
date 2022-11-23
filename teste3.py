import sys
import pyautogui
from random import sample
import time
import pyperclip as pc

lista24 = ['cave', 'box', 'priority', 'shadow', 'farm', 'orchard', 'stool', 'hazard', 'quote', 'noise', 'solar','mixed', 'minimum', 'slot', 'total', 'story', 'large', 'else', 'mean', 'search', 'impulse', 'harvest', 'insect', 'transfer']

lista9 = ['stove', 'bean', 'nuclear', 'young', 'cancel', 'win', 'bachelor', 'urban', 'canoe', 'era', 'crouch', 'away']


lista01 = ['orchard', 'stool', 'hazard', 'quote', 'noise', 'solar','mixed', 'minimum', 'slot', 'total', 'story', 'large']

listList = []





def embaralha(lista): # retorna uma cópia da lista, só que embaralhada
    return sample(lista, k=len(lista))

# lista2 = embaralha(lista0)
# x, y = pyautogui.locateCenterOnScreen('teste.png')
# 
a = True
# cor = True
while(a):
    def listar():
        lista2 = embaralha(lista01)
        # pyautogui.click(x, y)

        convert = " ".join(lista2)
        # print(convert)
        # print(x,y)
        pc.copy(convert)
        # pc.paste()
        # for palavra in lista2:
        pyautogui.click(x=1981, y=409)
        pyautogui.click(clicks=2, interval=0.15) 
        time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.click(x=2017, y=657)
        time.sleep(0.5)
        # cor = pyautogui.pixelMatchesColor(2267, 498, (251, 236, 237))
        cor = pyautogui.pixelMatchesColor(2017, 657, (226, 226, 226))
# time.sleep(0.5)
        if(cor):
        
            print("Cor True")
        else:
            a = False
            
            print(convert)
            listList.append(convert)
            exit()
            
        # pyautogui.press('tab')
        # pyautogui.press('tab')
            
            
        
    listar()

                
        # time.sleep(1)
        # x, y = pyautogui.locateCenterOnScreen('teste2.png')
        # pyautogui.write('Chave encontrada')
    
    

