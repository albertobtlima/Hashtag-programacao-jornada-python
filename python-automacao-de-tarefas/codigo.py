# -------- Passo a Passo do Projeto --------

import time
import pyautogui
import pandas

# -------- Passo 1: Entrar no sistema da empresa --------

pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site
time.sleep(2)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

# -------- Passo 2: Fazer login --------

# email
pyautogui.click(x=1971, y=317)    # x=1970, y=377
pyautogui.write("testepython@gmail.com")

# senha
pyautogui.press("tab")
pyautogui.write("abc123")

# logar
pyautogui.click(x=2003, y=441)    # x=1994, y=530
time.sleep(2)

# -------- Passo 3: Importar a base de dados --------

tabela = pandas.read_csv("produtos.csv")

# -------- Passo 4: Cadastrar 1 produto --------

# para cada linha da minha tabela
for linha in tabela.index:
    # clicar no primeiro campo
    pyautogui.click(x=1961, y=225)     # x=1965, y=259

    # cógigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar a base de dados
