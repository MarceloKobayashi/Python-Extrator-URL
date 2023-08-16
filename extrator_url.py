import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia.")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_ecomercial = self.get_url_parametros().find("&", indice_valor)
        if indice_ecomercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_ecomercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "URL base: " + self.get_url_base() + "\n" + "Parâmetros: " + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url


linkurl = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(linkurl)
print("O tamanho da URL é: ", len(extrator_url))
print(extrator_url)

extrator_url_2 = ExtratorURL(linkurl)
print(extrator_url == extrator_url_2)

# DESAFIO

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_final = int(quantidade) / VALOR_DOLAR
    print("o valor de {} reais equivale a {} dolares.".format(quantidade, valor_final))
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_final = int(quantidade) * VALOR_DOLAR
    print("o valor de {} dolares equivale a {} reais.".format(quantidade, valor_final))
else:
    print("o câmbio de {} para {} não está disponível.".format(moeda_origem, moeda_destino))
