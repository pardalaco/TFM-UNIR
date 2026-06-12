#!/usr/bin/env python3
import json
import sys
from evmaudit import run_mythril, ToolNotFoundError, AnalysisError

def test_integration():
    # Asegúrate de tener un contrato en esta ruta para la prueba
    contrato_ejemplo = "contracts/mythril_solidity_examples/origin.sol"
    
    print(f"[*] Iniciando análisis de prueba sobre: {contrato_ejemplo}")
    print("[*] Ejecutando Mythril (esto puede tardar unos segundos)...")
    
    try:
        # Invocamos el paquete tal y como lo haría un usuario externo
        resultado = run_mythril(contrato_ejemplo, timeout=30, depth=10)
        
        print("\n[+] ¡Ejecución exitosa del módulo runner!")
        
        # Imprimir una muestra de la salida cruda para verificar que llegó el JSON
        print("\n[+] Estructura del JSON recibido (primeros 200 caracteres de 'raw'):")
        raw_str = json.dumps(resultado, indent=2)
        print(raw_str[:200] + "...\n[Salida recortada]")
        
    except ToolNotFoundError as e:
        print(f"\n[X] Error de entorno: {e}")
        print("[!] Asegúrate de que 'myth' está instalado y que `myth --version` funciona en tu terminal.")
        sys.exit(1)
        
    except AnalysisError as e:
        print(f"\n[X] Error en el análisis del contrato: {e}")
        print("[!] Revisa si el compilador de Solidity (solc) está configurado correctamente para ese contrato.")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n[X] Error inesperado no controlado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_integration()