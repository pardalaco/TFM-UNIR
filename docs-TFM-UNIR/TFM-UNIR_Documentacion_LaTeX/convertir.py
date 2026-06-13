from pathlib import Path
import subprocess

origen = Path("capitulos_md")
destino = Path("capitulos")

generados = []

# Convertir todos los .md
for md_file in origen.rglob("*.md"):

    relativa = md_file.relative_to(origen)
    tex_file = (destino / relativa).with_suffix(".tex")

    tex_file.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        ["pandoc", str(md_file), "-o", str(tex_file)],
        check=True
    )

    generados.append(tex_file)

# Mostrar resultado
print("\nArchivos generados:")
print("capitulos/")

for archivo in sorted(generados):
    relativa = archivo.relative_to(destino)
    print(f"└── {relativa}")