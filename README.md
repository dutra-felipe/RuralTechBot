# RuralTech Bot 🤖

Bot de atendimento para a RuralTech, especialista em soluções tecnológicas para agricultura.

## 📋 Descrição

O RuralTech Bot é um assistente virtual desenvolvido em Python utilizando a API do Telegram. Ele oferece um menu interativo com botões para facilitar a navegação e o acesso a informações sobre produtos, serviços, horários de atendimento e contato com a empresa.

## 🌟 Funcionalidades

- Menu interativo com botões
- Catálogo de produtos com descrições e preços
- Informações sobre a empresa
- Horários de atendimento
- Localização da empresa
- Formulário para contato
- Sistema de finalização e reinício de atendimento

## 🔧 Tecnologias Utilizadas

- Python 3.12
- python-telegram-bot
- PostgreSQL para armazenamento de dados
- Docker para containerização

## 📁 Estrutura do Projeto

```
botRural/
├── database/
│   ├── db_manager.py    # Gerenciamento do banco de dados
│   └── models.py        # Modelos de dados
├── handlers/
│   ├── command.py       # Handlers para comandos
│   ├── contact.py       # Formulário de contato
│   ├── feedback.py      # Sistema de feedback
│   ├── finish.py        # Finalização de atendimento
│   ├── menu.py          # Menu interativo
│   └── message.py       # Processamento de mensagens
├── utils/
│   └── constants.py     # Constantes e configurações
├── venv/                # Ambiente virtual (não versionado)
├── .env                 # Variáveis de ambiente (não versionado)
├── .gitignore           # Arquivos ignorados pelo Git
├── config.py            # Configurações gerais
├── docker-compose.yml   # Configuração do Docker
├── Dockerfile           # Instruções para construção da imagem
├── main.py              # Ponto de entrada da aplicação
└── requirements.txt     # Dependências do projeto
```

## ⚙️ Instalação e Configuração

### Requisitos

- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)
- Token de bot do Telegram (obtido através do [BotFather](https://t.me/botfather))

### Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/botRural.git
   cd botRural
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   BOT_TOKEN=seu_token_aqui
   ```

### Execução com Docker

```bash
docker-compose up -d
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

