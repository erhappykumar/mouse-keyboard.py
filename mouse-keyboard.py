import pyautogui
import keyboard
import sys
import time
from time import sleep
pyautogui.size()
print((pyautogui.size().height))
print(pyautogui.position())
print(pyautogui.position().x)
#while pyautogui.size():
#x=input("please enter x,y......:   ")
#y=str(x)[0]+str(x)[1]
#y=int(y)
#pyautogui.moveTo(y,58)
#x=input()
#print(x)
#try:
def fun(r,m):
    
  keyboard.read_key()
#keyboard.is_pressed()
  print(pyautogui.position())
  
#print(keyboard.is_pressed())
  if True:#px!=pyautogui.position().x or py!=pyautogui.position().y:
    c=9
    if keyboard.is_pressed('down'):
     if pyautogui.position().y+m+r<pyautogui.size().height:
      pyautogui.moveTo((pyautogui.position().x),pyautogui.position().y+m+r,.5)
      print("exit")
    if keyboard.is_pressed('up'):
     if pyautogui.position().y-m-r>0:
      pyautogui.moveTo((pyautogui.position().x),pyautogui.position().y-m-r)
      print("exit2")
    if keyboard.is_pressed('right'):
     if (pyautogui.position().x+r)+2*m<pyautogui.size().width:
      pyautogui.moveTo((pyautogui.position().x+r)+2*m,pyautogui.position().y)
      print("exit3") 
    if keyboard.is_pressed('left'):
     if (pyautogui.position().x-r)-2*m>0:
      pyautogui.moveTo((pyautogui.position().x-r)-2*m,pyautogui.position().y)
      print("exit3") 
  #else :
    #pyautogui.moveTo(pyautogui.position().x+10,pyautogui.position().y-10)
    #fun(50,50)
    #print(str(m)+'else')
 
while True: 
  #print(m+'else')
  px=pyautogui.position().x
  py=pyautogui.position().y
  fun(50,150)
  if px==pyautogui.position().x and py==pyautogui.position().y :
   fun(40,10)
  px=pyautogui.position().x
  py=pyautogui.position().y
  fun(30,150)
  if px==pyautogui.position().x and py==pyautogui.position().y :
   fun(20,10)
  px=pyautogui.position().x
  py=pyautogui.position().y
  fun(10,150)  
  px=pyautogui.position().x
  py=pyautogui.position().y
  if px==pyautogui.position().x and py==pyautogui.position().y :
   fun(10,10)
  