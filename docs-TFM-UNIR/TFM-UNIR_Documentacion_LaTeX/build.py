from pathlib import Path
import subprocess

ORIGEN = Path("capitulos_md")
DESTINO = Path("capitulos")
PLANTILLA = "plantilla"


def convertir_markdown():
    generados = []

    for md_file in ORIGEN.rglob("*.md"):
        relativa = md_file.relative_to(ORIGEN)
        tex_file = (DESTINO / relativa).with_suffix(".tex")

        tex_file.parent.mkdir(parents=True, exist_ok=True)

        subprocess.run(
            ["pandoc", str(md_file), "-o", str(tex_file)],
            check=True
        )

        generados.append(tex_file)

    print("\n=== Archivos .tex generados ===")
    print("capitulos/")
    for archivo in sorted(generados):
        print(f"└── {archivo.relative_to(DESTINO)}")


def compilar_pdf():
    print("\n=== Compilando PDF ===")

    subprocess.run(
        ["latexmk", "-pdf", "-interaction=nonstopmode", f"{PLANTILLA}.tex"],
        check=True
    )

    print(f"\nPDF generado correctamente: {PLANTILLA}.pdf")

if __name__ == "__main__":
    convertir_markdown()
    compilar_pdf()