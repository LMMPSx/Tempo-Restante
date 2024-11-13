import pyautogui
import time
import pyperclip
import cv2
import pytesseract
import keyboard


# Caminho do tesseract
caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

pyautogui.PAUSE = 0.1

# Variaveis
dias = ''
tempo_restante = 0
cpf = ''
tamanho = 0

# Clica e seleciona a primeira celula
pyautogui.click(1116,1058, duration=0.5)
pyautogui.click(177,297, duration=0.5)

while(dias != '-'):
    # Copia a quantidade de dias restantes e salva numa variavel
    pyautogui.hotkey('ctrl', 'c')
    dias = pyperclip.paste()

    # Copia o CPF do estagiário salva numa variável
    pyautogui.hotkey('left')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    cpf = str(pyperclip.paste())
    print(cpf)
    tamanho = len(cpf)     
    time.sleep(0.1)
    pyautogui.hotkey('right')

    # Verifica se o CPF tem 11 caracteres se não tiver adiciona o zero na frente e faz a pesquisa no sigest
    if tamanho < 11:
        pyautogui.click(1160,1053, duration=0.5)
        pyautogui.click(86,254, duration=0.5)
        pyautogui.click(539,308, duration=0.5)
        pyautogui.click(896,368, duration=0.5)
        keyboard.write(f'0{cpf}')
        pyautogui.click(1114,370, duration=0.5)
    else:
        pyautogui.click(1160,1053, duration=0.5)
        pyautogui.click(86,254, duration=0.5)
        pyautogui.click(539,308, duration=0.5)
        pyautogui.click(896,368, duration=0.5)
        keyboard.write(f'{cpf}')
        pyautogui.click(1114,370, duration=0.5)

    time.sleep(10)

    # Vê o tempo restante e salva em forma de imagem
    pyautogui.click(435,789, duration=2)
    time.sleep(10)
    pyautogui.screenshot("dias_Restantes.png", region=((1136, 222, 42, 22)))

    time.sleep(3)

    # Le a imagem e salva o texto numa variável
    img = cv2.imread("dias_Restantes.png")
    texto = pytesseract.image_to_string(img, lang="eng", config=r'--psm 7 -c tessedit_char_whitelist=0123456789')
    # --psm 7 'para texto em linha unica', 'a whitelist serve para o programa reconhecer apenas os caracteres listados nesse caso apenas numeros'
    tempo_restante = int(texto)

    
    pyautogui.click(682,486, duration=0.5)
    pyautogui.click(489,508, duration=0.5)

    pyautogui.click(587,789, duration=0.5)

    time.sleep(0.1)
    pyautogui.click(1116,1058, duration=0.5)
    time.sleep(0.1)
    pyautogui.hotkey('right')
    time.sleep(0.1)

    # compara se o tempo restante no sigest é o mesmo da planiha se for pinta de verde senão vermelho
    tempo_texto = str(tempo_restante)
    if len(tempo_texto > 3):
        tempo_restante = tempo_texto[:3]
    keyboard.write(str(tempo_restante))
    if(int(tempo_restante) != int(dias)):
        pyautogui.click(778,194, duration=0.5)
        pyautogui.click(803,279, duration=0.5)
    else:
        pyautogui.click(778,194, duration=0.5)
        pyautogui.click(859,279, duration=0.5)
    pyautogui.hotkey('left')  
    time.sleep(0.1)
    pyautogui.hotkey('down')
    time.sleep(0.1)