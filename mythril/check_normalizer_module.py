#!/usr/bin/env python3
import json
import sys
from evmaudit import run_mythril, normalize_mythril_output, ToolNotFoundError, AnalysisError

def test_normalizer_integration():
    # Contrato de ejemplo para la prueba
    nombre_contrato = "calls.sol"
    
    contrato_ejemplo = "contracts/mythril_solidity_examples/"+nombre_contrato
    ruta_json_raw = "jsons/runner/mythril/"+nombre_contrato.replace(".sol", "_mythril.json")
    ruta_json_normalizado = "jsons/normalizer/"+nombre_contrato.replace(".sol", "_hallazgos_normalizados.json")
    
    
    try:
        # 1. Obtener la salida cruda estructurada del módulo runner

        print(f"[*] Fase 1: Invocando el Runner sobre: {contrato_ejemplo}")
        print("[*] Ejecutando Mythril y capturando JSON crudo...")
        cargando_json = run_mythril(contrato_ejemplo, timeout=30, depth=10)
        print("[+] Fase 1 completada con éxito.")

        # print(f"[*] Fase 1: Cargando JSON crudo desde: {ruta_json_raw}")
        # with open(ruta_json_raw, "r", encoding="utf-8") as f:
        #     cargando_json = json.load(f)
        # print("[+] Fase 1 completada con éxito.")

        
        # 2. Invocar el módulo normalizador pasándole el diccionario obtenido
        print("\n[*] Fase 2: Invocando el Normalizer...")
        hallazgos_normalizados = normalize_mythril_output(cargando_json)
        print("[+] Fase 2 completada con éxito.")
        
        # 3. Mostrar y validar los resultados transformados a objetos Finding
        print(f"\n[+] Se han encontrado y transformado {len(hallazgos_normalizados)} hallazgo(s):")
        print("=" * 80)

        findings = hallazgos_normalizados["findings"] if isinstance(hallazgos_normalizados, dict) else []
        
        for idx, finding in enumerate(findings, 1):
            print(f"Hallazgo {idx}:")
            print(f"  Título: {finding['title']}")
            print(f"  Descripción: {finding['description'][:100]}...")  # Mostrar solo los primeros 100 caracteres
            print(f"  Severidad: {finding['severity']}")
            print(f"  Categoría: {finding['category']}")
            print(f"  Ubicación: {finding['location']['file']}:{finding['location']['line']}")
            print(f"  SWC ID: {finding['swc_id']}")
            print("-" * 80)

        # 4. Guardar el JSON normalizado en la carpeta de destino
        print("\n[*] Fase 3: Guardando resultados normalizados en JSON...")
        with open(f"{ruta_json_normalizado}", "w", encoding="utf-8") as f:
            json.dump(hallazgos_normalizados, f, indent=4, ensure_ascii=False)
        print("[+] Fase 3 completada con éxito. Resultados guardados en 'hallazgos_normalizados.json'.")


    except ToolNotFoundError as e:
        print(f"\n[X] Error de entorno: {e}")
        sys.exit(1)
        
    except AnalysisError as e:
        print(f"\n[X] Error en el análisis del contrato: {e}")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n[X] Error inesperado no controlado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_normalizer_integration()