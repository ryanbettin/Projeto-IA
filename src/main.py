import argparse
from utils import detectar_cores_e_formas

def main():
    parser = argparse.ArgumentParser(description="Detector de Sinal com Formas para Daltônicos")
    parser.add_argument('--input', required=True, help="Caminho da imagem de entrada")
    args = parser.parse_args()

    sinais = detectar_cores_e_formas(args.input)

    if sinais:
        print("Sinais detectados na imagem:")
        for cor, forma in sinais:
            print(f"- {cor}: {forma}")
    else:
        print("Nenhuma cor de semáforo detectada.")

if __name__ == "__main__":
    main()
