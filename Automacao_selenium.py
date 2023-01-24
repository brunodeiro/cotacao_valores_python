"""
- Você precisa atualizar a cotação dos valores do dólar,euro e ouro para uma tabela do excel
- Gerar novo arquivo com os dados atualizados

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()

navegador.get("https://www.google.com")

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação do dolar")

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#print(cotacao_dolar)



navegador.find_element('xpath','//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys(Keys.CONTROL + "a")

navegador.find_element('xpath','//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys("Cotação do euro")

navegador.find_element('xpath','//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#print(cotacao_euro)



navegador.get('https://www.melhorcambio.com/ouro-hoje')

cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")

#print(cotacao_ouro)

navegador.quit()





tabela = pd.read_excel("Produtos.xlsx")
#print(tabela)

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]

tabela["Preço de Venda"] = tabela["Cotação"] * tabela["Margem"]


tabela.to_excel("Produtos Novo.xlsx", index=False)