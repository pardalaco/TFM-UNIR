#!/usr/bin/env python3
import json
from pathlib import Path
from evmaudit import run_slither, ToolNotFoundError, AnalysisError


def process_all_contracts(src_dir: str = "../contracts", dest_dir: str = "../jsons/slither"):
    path_src = Path(src_dir)
    path_dest = Path(dest_dir)

    path_dest.mkdir(parents=True, exist_ok=True)

    if not path_src.exists() or not path_src.is_dir():
        print(f"[X] Error: la carpeta de origen '{src_dir}' no existe.")
        return

    contracts = list(path_src.glob("*.sol"))

    if not contracts:
        print(f"[-] No se encontraron archivos .sol en '{src_dir}'.")
        return

    print(f"[*] Se han encontrado {len(contracts)} contrato(s).\n")

    for idx, contract_path in enumerate(contracts, 1):
        print(f"[{idx}/{len(contracts)}] Analizando: {contract_path.name}...")

        output_json_path = path_dest / f"{contract_path.stem}_slither.json"

        try:
            resultado = run_slither(str(contract_path), timeout=60)

            with open(output_json_path, "w", encoding="utf-8") as f:
                json.dump(resultado, f, indent=4, ensure_ascii=False)

            print(f"    [+] Guardado en: {output_json_path}")

        except ToolNotFoundError as e:
            print(f"    [X] Error crítico de entorno: {e}")
            break

        except AnalysisError as e:
            print(f"    [X] Error analizando '{contract_path.name}': {e}")

        except Exception as e:
            print(f"    [X] Error inesperado con '{contract_path.name}': {e}")

    print("\n[+] Procesamiento finalizado.")


if __name__ == "__main__":
    process_all_contracts(
        src_dir="../contracts",
        dest_dir="../jsons/slither",
    )