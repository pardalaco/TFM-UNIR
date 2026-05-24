#!/usr/bin/env python3
import json
import sys
from evmaudit import run_slither, ToolNotFoundError, AnalysisError


def test_integration():
    contrato_ejemplo = "../contracts/Reentrancy.sol"

    print(f"[*] Iniciando análisis de prueba sobre: {contrato_ejemplo}")
    print("[*] Ejecutando Slither...")

    try:
        resultado = run_slither(contrato_ejemplo, timeout=60)

        print("\n[+] Ejecución exitosa del módulo runner")

        raw_str = json.dumps(resultado, indent=2, ensure_ascii=False)
        print("\n[+] Estructura del JSON recibido:")
        print(raw_str[:500] + "...\n[Salida recortada]")

    except ToolNotFoundError as e:
        print(f"\n[X] Error de entorno: {e}")
        print("[!] Comprueba que `slither --version` funciona.")
        sys.exit(1)

    except AnalysisError as e:
        print(f"\n[X] Error en el análisis: {e}")
        print("[!] Revisa solc/solc-select y la ruta del contrato.")
        sys.exit(1)

    except Exception as e:
        print(f"\n[X] Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    test_integration()