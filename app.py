import subprocess

with open("req.txt") as f:
    pacotes = [linha.strip() for linha in f if linha.strip()]

for pacote in pacotes:
    print(f"Desinstalando {pacote}...")
    subprocess.run(["pip", "uninstall", "-y", pacote])
