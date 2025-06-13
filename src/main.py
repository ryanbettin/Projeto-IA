import argparse
from datetime import datetime
from utils import detectar_cores_e_formas

def salvar_log(imagem_path, sinais_detectados):
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Analisando imagem: {imagem_path}\n")
        if sinais_detectados:
            for cor, forma in sinais_detectados:
                log_file.write(f"- {cor}: {forma}\n")
        else:
            log_file.write("Nenhuma cor de semáforo detectada.\n")

def main():
    parser = argparse.ArgumentParser(description="Detector de Sinal com Formas para Daltônicos")
    parser.add_argument('--input', required=True, help="Caminho da imagem de entrada")
    args = parser.parse_args()

    sinais = detectar_cores_e_formas(args.input)

    if sinais:
        print("Sinais e cores detectados na imagem:")
        for cor, forma in sinais:
            print(f"- {cor}: {forma}")
    else:
        print("Nenhuma cor de semáforo detectada.")

    salvar_log(args.input, sinais)
