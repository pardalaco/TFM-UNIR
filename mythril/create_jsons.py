#!/usr/bin/env python3
import os
import json
from pathlib import Path
from evmaudit import run_mythril
from evmaudit import ToolNotFoundError, AnalysisError

def process_all_contracts(src_dir: str = "contracts", dest_dir: str = "jsons"):
    """
    Escanea la carpeta de origen en busca de contratos .sol, ejecuta Mythril
    sobre cada uno de ellos y guarda el resultado crudo en formato JSON.
    """
    path_src = Path(src_dir)
    path_dest = Path(dest_dir)

    # Aseguramos que la carpeta de destino exista
    if not path_dest.exists():
        print(f"[X] La carpeta de destino '{dest_dir}' no existe.")
        return


    # Validamos que la carpeta de origen exista
    if not path_src.exists() or not path_src.is_dir():
        print(f"[X] Error: La carpeta de origen '{src_dir}' no existe.")
        return

    # Buscamos todos los archivos .sol en la carpeta
    contracts = list(path_src.glob("*.sol"))

    if not contracts:
        print(f"[-] No se encontraron archivos .sol en '{src_dir}'.")
        return

    print(f"[*] Se han encontrado {len(contracts)} contrato(s) para analizar.\n")

    for idx, contract_path in enumerate(contracts, 1):
        print(f"[{idx}/{len(contracts)}] Analizando: {contract_path.name}...")
        
        # Definimos el nombre del archivo JSON de salida
        output_json_path = path_dest / f"{contract_path.stem}_mythril.json"

        try:
            # Ejecutamos el runner de tu paquete
            resultado = run_mythril(str(contract_path), timeout=60, depth=10)
            
            # Guardamos el JSON resultante en la carpeta de destino
            with open(output_json_path, "w", encoding="utf-8") as f:
                json.dump(resultado, f, indent=4, ensure_ascii=False)
                
            print(f"    [+] Guardado correctamente en: {output_json_path} (Status: {resultado['success']})")
            
            if not resultado["success"]:
                print(f"    [!] El análisis no fue exitoso. Status: {resultado['success']}")

        except ToolNotFoundError as e:
            print(f"    [X] Error crítico de entorno: {e}")
            print("    [!] Abortando el procesamiento por falta de herramientas.")
            break

        except AnalysisError as e:
            print(f"    [X] Error al analizar '{contract_path.name}': {e}")
            print("    [!] Saltando este contrato y continuando con el siguiente...")
            
        except Exception as e:
            print(f"    [X] Error inesperado con '{contract_path.name}': {e}")
            print("    [!] Saltando...")

    print("\n[+] Procesamiento por lotes finalizado.")

if __name__ == "__main__":
    path_src = "contracts/mythril_solidity_examples"  # Cambia esto si tus contratos están en otra carpeta
    path_dest = "jsons/mythril"     # Cambia esto si quieres guardar los JSON en
    process_all_contracts(path_src, path_dest)