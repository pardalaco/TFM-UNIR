
#!/usr/bin/env python3
import os
import json
from pathlib import Path
from evmaudit import run_mythril, normalize_mythril_output
from evmaudit import ToolNotFoundError, AnalysisError

def process_and_normalize_contracts(src_dir: str = "contracts", dest_dir: str = "jsons/normalizer"):
    """
    Escanea la carpeta de origen en busca de contratos .sol, ejecuta Mythril,
    normaliza los hallazgos y guarda el resultado final estructurado en JSON.
    """
    path_src = Path(src_dir)
    path_dest = Path(dest_dir)

    # Aseguramos que la carpeta de destino exista (la crea si no existe)
    if not path_dest.exists():
        print(f"[*] Creando la carpeta de destino: '{dest_dir}'")
        path_dest.mkdir(parents=True, exist_ok=True)

    # Validamos que la carpeta de origen exista
    if not path_src.exists() or not path_src.is_dir():
        print(f"[X] Error: La carpeta de origen '{src_dir}' no existe o no es un directorio.")
        return

    # Buscamos todos los archivos .sol en la carpeta
    contracts = list(path_src.glob("*.sol"))

    if not contracts:
        print(f"[-] No se encontraron archivos .sol en '{src_dir}'.")
        return

    print(f"[*] Se han encontrado {len(contracts)} contrato(s) para analizar y normalizar.\n")

    for idx, contract_path in enumerate(contracts, 1):
        print(f"[{idx}/{len(contracts)}] Procesando contrato: {contract_path.name}")
        print(f"    [*] Fase 1: Ejecutando Mythril...")
        
        # Definimos el nombre del archivo JSON de salida normalizado
        output_json_path = path_dest / f"{contract_path.stem}_hallazgos_normalizados.json"

        try:
            # 1. Ejecución de Mythril (Runner)
            resultado_raw = run_mythril(str(contract_path), timeout=60, depth=10)
            print(f"    [+] Fase 1 completada (Status: {resultado_raw.get('success', False)})")
            
            # 2. Normalización de la salida (Normalizer)
            print(f"    [*] Fase 2: Normalizando resultados...")
            hallazgos_normalizados = normalize_mythril_output(resultado_raw)
            print(f"    [+] Fase 2 completada.")

            # Mostrar un pequeño resumen por consola de lo que se ha encontrado
            findings = hallazgos_normalizados.get("findings", []) if isinstance(hallazgos_normalizados, dict) else []
            print(f"    [i] Se transformaron {len(findings)} hallazgo(s).")
            
            # 3. Guardar el JSON normalizado
            print(f"    [*] Fase 3: Guardando resultados en JSON...")
            with open(output_json_path, "w", encoding="utf-8") as f:
                json.dump(hallazgos_normalizados, f, indent=4, ensure_ascii=False)
                
            print(f"    [+] Guardado correctamente en: {output_json_path}")
            print("-" * 60)

        except ToolNotFoundError as e:
            print(f"    [X] Error crítico de entorno: {e}")
            print("    [!] Abortando el procesamiento por lotes debido a falta de herramientas.")
            break

        except AnalysisError as e:
            print(f"    [X] Error al analizar '{contract_path.name}': {e}")
            print("    [!] Saltando este contrato y continuando con el siguiente...")
            print("-" * 60)
            
        except Exception as e:
            print(f"    [X] Error inesperado con '{contract_path.name}': {e}")
            print("    [!] Saltando...")
            print("-" * 60)

    print("\n[+] Procesamiento por lotes y normalización finalizados.")

if __name__ == "__main__":
    # Configuración de rutas basada en tus scripts anteriores
    path_src = "contracts/mythril_solidity_examples"
    path_dest = "jsons/normalizer/mythril"
    
    process_and_normalize_contracts(path_src, path_dest)