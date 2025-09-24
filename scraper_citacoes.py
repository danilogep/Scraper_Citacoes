import requests
from bs4 import BeautifulSoup
import csv

# URL base do site a ser raspado
URL_BASE = "http://quotes.toscrape.com"

def raspar_citacoes():
    """
    Função principal para raspar as citações de todas as páginas do site
    e salvar em um arquivo CSV.
    """
    url_pagina_atual = "/"
    citacoes_completas = []
    
    # Loop para navegar através de todas as páginas ("paginação")
    while url_pagina_atual:
        # Monta a URL completa da página a ser raspada
        url_completa = URL_BASE + url_pagina_atual
        print(f"Raspando a página: {url_completa}...")
        
        try:
            # Faz a requisição HTTP para obter o conteúdo da página
            response = requests.get(url_completa)
            response.raise_for_status() # Lança erro para status HTTP ruins (4xx/5xx)
            
            # Cria um objeto BeautifulSoup para "parsear" (analisar) o HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontra todos os contêineres de citação na página
            # Cada citação está dentro de uma <div class="quote">
            citacoes_na_pagina = soup.find_all('div', class_='quote')
            
            if not citacoes_na_pagina:
                print("Nenhuma citação encontrada nesta página. Encerrando.")
                break
            
            # Itera sobre cada contêiner de citação encontrado
            for citacao in citacoes_na_pagina:
                # Extrai o texto, autor e as tags
                texto = citacao.find('span', class_='text').get_text(strip=True)
                autor = citacao.find('small', class_='author').get_text(strip=True)
                
                # As tags estão dentro de <a> dentro de uma <div class="tags">
                tags_elementos = citacao.find_all('a', class_='tag')
                tags = [tag.get_text(strip=True) for tag in tags_elementos]
                
                # Adiciona os dados extraídos à nossa lista principal
                citacoes_completas.append({
                    'texto': texto,
                    'autor': autor,
                    'tags': ', '.join(tags) # Junta as tags em uma única string
                })
            
            # Lógica para encontrar o link da próxima página
            # O link está em um elemento <li> com a classe "next"
            proxima_pagina_li = soup.find('li', class_='next')
            if proxima_pagina_li and proxima_pagina_li.find('a'):
                url_pagina_atual = proxima_pagina_li.find('a')['href']
            else:
                # Se não encontrar o botão "Next", encerra o loop
                print("Fim da paginação. Todas as páginas foram raspadas.")
                url_pagina_atual = None

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a página {url_completa}: {e}")
            break # Encerra em caso de erro de conexão
    
    return citacoes_completas

def salvar_em_csv(citacoes, nome_arquivo='citacoes.csv'):
    """Salva a lista de citações em um arquivo CSV."""
    if not citacoes:
        print("Nenhuma citação para salvar.")
        return
        
    print(f"\nSalvando {len(citacoes)} citações no arquivo '{nome_arquivo}'...")
    
    # Define os nomes das colunas (cabeçalho)
    cabecalho = ['texto', 'autor', 'tags']
    
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            # Cria um escritor de dicionários para o CSV
            escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
            
            # Escreve o cabeçalho
            escritor.writeheader()
            
            # Escreve todas as citações da lista
            escritor.writerows(citacoes)
            
        print("Arquivo CSV salvo com sucesso!")
    except IOError as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

# Bloco principal de execução
if __name__ == "__main__":
    lista_de_citacoes = raspar_citacoes()
    salvar_em_csv(lista_de_citacoes)