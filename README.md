# SCRAPER CITAÇÕES
Um web scraper desenvolvido em Python que navega por um site de citações, extrai informações estruturadas e as salva em um arquivo CSV.

Este projeto faz a coleta de dados na web, incluindo a realização de requisições HTTP e a navegação automática por múltiplas páginas (paginação). É uma demonstração prática de como construir ferramentas de automação para a extração de dados da internet.

✨ Funcionalidades
1. Extração de Dados: Coleta o texto da citação, o nome do autor e as tags associadas.
2. Paginação Automática: Navega de forma autônoma por todas as páginas do site, seguindo o link "Next" até a última página.
3. Armazenamento Estruturado: Salva todos os dados coletados em um arquivo .csv limpo e bem formatado, pronto para ser usado em planilhas ou análises de dados.

🎯 Alvo do Scraper: O script foi desenvolvido para extrair dados do site http://quotes.toscrape.com. Este site é um "sandbox" (ambiente de testes) mantido especificamente para fins educacionais, permitindo a prática de web scraping de forma legal e ética, sem violar termos de serviço ou sobrecarregar servidores de produção.

🛠️ Tecnologias Utilizadas
1. Python 3: Linguagem principal do projeto.
2. requests: Biblioteca para realizar as requisições HTTP e fazer o download do conteúdo HTML das páginas.
3. Beautiful Soup 4: A principal biblioteca de parsing utilizada para navegar na estrutura do documento HTML e extrair os dados de interesse de forma eficiente.

⚙️ Como Usar
1. Instalação e Execução

Faça o clone este repositório: https://github.com/danilogep/Scraper_Citacoes.git

Acesse o cd [NOME-DO-SEU-REPOSITORIO]

Instale as bibliotecas requests e beautifulsoup4. Instale-as com o seguinte comando: pip install requests beautifulsoup4

Execute o script: python scraper_citacoes.py
Ao final, o arquivo citacoes.csv será criado na mesma pasta.

