# Archicad × Claude Desktop – Guia de Instalação (Windows 10/11)

## Objetivo

Ligar o Archicad a modelos de linguagem (Claude, ChatGPT, etc.) via Tapir + MCP, utilizando o Model Context Protocol para interação inteligente com projetos BIM.

---

## Índice

1. [Visão geral](#1-Visão-geral)
2. [Pré-requisitos](#2-Pré--requisitos)
3. [Clonar repositório Tapir Archicad MCP](#3-Clonar-repositório-Tapir-Archicad-MCP)
4. [Criar e ativar ambiente Python](#4-Criar-e-ativar-ambiente-Python)
5. [Instalar dependências](#5-Instalar-dependências)
6. [Testar servidor MCP](#6-Testar-servidor-MCP)
7. [Executar server.py no Archicad](#7-Executar-server.py-no-Archicad)
8. [Configurar o Claude Desktop](#8-Configurar-o-Claude-Desktop)
9. [Fluxo de uso](#9-Fluxo-de-uso)
10. [Problemas comuns](#10-Problemas-comuns)
11. [Créditos](#11-Créditos)

---

## 1. Visão geral

O plugin Tapir permite que o Archicad seja usado com o Model Context Protocol (MCP). Isso possibilita que modelos BIM em formato PLN interajam com LLMs como o Claude via scripts Python rodando dentro do Archicad.

---

## 2. Pré-requisitos

| Item     | Versão mínima | Download |
| -------- | ------------- | -------- |
| Archicad | 27+           | [https://graphisoft.com/downloads](https://graphisoft.com/downloads) | 
| Tapir                                                                | –    | [https://github.com/orchitecture/tapir](https://github.com/orchitecture/tapir) |
| Python                                                               | 3.12 | [https://www.python.org/downloads/](https://www.python.org/downloads/)         |
| Claude Desktop                                                       | 0.9+ | [https://claude.ai/download](https://claude.ai/download)                       |

---

## 3. Clonar repositório Tapir Archicad MCP

```bash
mkdir C:\ArchicadIA
cd C:\ArchicadIA
git clone https://github.com/SzamosiMate/tapir-archicad-MCP.git
cd tapir-archicad-MCP
```

---

## 4. Criar e ativar ambiente Python

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 5. Instalar dependências

```bash
pip install --upgrade pip
pip install -e .
pip install mcp[cli] httpx
```

---

## 6. Testar servidor MCP

```bash
python tools.py --help
```

Saída esperada:

```text
usage: tools.py [OPTIONS] COMMAND [ARGS]...
```

Significa que as ferramentas MCP estão instaladas e acessíveis.

---

## 7. Executar server.py no Archicad

1. Abra o Archicad
2. Ative o menu **Tapir** ▸ **Script**
3. Selecione o arquivo `server.py`

```python
import logging
from tapir_archicad_mcp.app import mcp
from tapir_archicad_mcp.tools.registration import register_all_tools

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

register_all_tools()
logging.info("All MCP tools have been registered.")

def main():
    logging.info("Starting Archicad Tapir MCP Server...")
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

4. Clique no botão ▶️ (Executar)
5. O Tapir inicia a comunicação com Claude Desktop via MCP

---

## 8. Configurar o Claude Desktop

Abra **Claude ▸ Settings ▸ Developer ▸ Edit Config**

```json
{
  "mcpServers": {
    "ArchicadTapir": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "C:\\ArchicadIA\\tapir-archicad-MCP",
        "python",
        "-m",
        "tapir_archicad_mcp.server"
      ]
    }
  }
}
```

Salve e reinicie o Claude. O ícone 🛠 deve aparecer mostrando as ferramentas MCP registradas.

---

## 9. Fluxo de uso

1. Inicie o servidor executando `server.py` no Tapir
2. Inicie o Claude Desktop (ou reinicie após configurar)
3. Abra seu projeto PLN no Archicad
4. No Claude, faça perguntas como:

```text
Liste todos os elementos do projeto.
Quantas paredes existem neste modelo?
Qual a hierarquia dos andares?
```

O Claude utilizará as ferramentas registradas pelo Tapir via MCP.

---

## 10. Problemas comuns

| Sintoma                            | Causa + Solução                                                       |
| ---------------------------------- | --------------------------------------------------------------------- |
| Ferramentas não aparecem no Claude | JSON config incorreto ou script server.py não está em execução        |
| "No transport found"               | Parâmetro `mcp.run(transport='stdio')` ausente ou com erro            |
| Claude não detecta Archicad        | Tapir não está ativado ou script não foi executado dentro do Archicad |

---

## 11. Créditos

- Repositório original por [SzamosiMate](https://github.com/SzamosiMate/tapir-archicad-MCP)
- Claude IA + Model Context Protocol por [Anthropic](https://www.anthropic.com/)
- Inspiração: Integração Bonsai BIM + Claude Desktop por @JotaDeRodriguez
- Tutorial por @TiagoMendonca

**Licença MIT** – Este projeto é aberto. Sinta-se à vontade para criar sua versão, enviar melhorias ou abrir PRs!

