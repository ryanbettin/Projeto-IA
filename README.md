# 🚦 IA-UV-SEMAFARO

Projeto de detecção de sinais de trânsito por **formas e cores**, com foco em acessibilidade para pessoas com daltonismo.

## 🎯 Objetivo

O sistema identifica automaticamente sinais de trânsito em uma imagem, associando cada **forma geométrica** a uma **cor específica** do semáforo:

- 🔴 **Círculo** → **Vermelho**
- 🟡 **Triângulo** → **Amarelo**
- 🟢 **Quadrado** → **Verde**

Isso permite interpretar os sinais **sem depender da cor**, sendo útil para quem tem deficiência de percepção visual.

---

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [uv](https://github.com/astral-sh/uv) – Gerenciador de ambiente Python moderno
- Estrutura modular baseada em `pyproject.toml`

---

## 📁 Estrutura do Projeto

IA-UV-SEMAFARO/
├── imagens/
│ └── imagem1.jpg
├── src/
│ └── ia_uv_semafaro/
│ ├── algoritmos/
│ │ └── mapeamento.py
│ ├── init.py
│ ├── main.py
│ └── utils.py
├── tests/
│ └── init.py
├── .venv/
├── pyproject.toml
├── README.md
└── log.txt


---

## ▶️ Como Executar

1. Instale as dependências com `uv`:
```bash
uv sync

uv run ia-uv-semafaro -- --input imagens/imagem1.jpg

📌Exemplo de Saída
Sinais e cores detectados na imagem:
- VERMELHO: Círculo
- AMARELO: Triângulo
- VERDE: Quadrado

📜 Licença
Projeto acadêmico com finalidade educacional. Uso livre para fins de estudo


## Autores

- **Andrei Lemos Cruz**  
- **Silvio Ryan Bettin**
