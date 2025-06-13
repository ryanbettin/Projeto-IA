# IA-UV-SEMAFARO

Projeto de detecção de sinais de trânsito por **formas e cores** voltado para acessibilidade de pessoas daltônicas.

## 🎯 Objetivo

O sistema identifica automaticamente sinais de trânsito presentes em uma imagem, relacionando:

- **Círculo** → **Vermelho**
- **Triângulo** → **Amarelo**
- **Quadrado** → **Verde**

Isso permite interpretar o semáforo por **forma geométrica**, auxiliando pessoas com deficiência de percepção de cor.

---

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- OpenCV
- NumPy
- uv (gerenciador de ambiente Python moderno)
- Estrutura baseada em módulos e `pyproject.toml`

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
| |__ tests/
│  └── init.py
├── .venv/ 
├── pyproject.toml
└── index.md

# Execute o script:

uv run ia-uv-semafaro -- --input imagens/imagem1.jpg


# Ao rodar o programa, você verá uma saída como:
Sinais detectados na imagem:
- VERMELHO: Círculo
- AMARELO: Triângulo
- VERDE: Quadrado

