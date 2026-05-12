from slither.slither import Slither

def analizar_contrato(archivo_sol):
    try:
        # Inicializamos Slither con el archivo del contrato
        slither = Slither(archivo_sol)

        for contrato in slither.contracts:
            print(f"--- Analizando contrato: {contrato.name} ---")
            
            for funcion in contrato.functions:
                # Obtenemos la visibilidad de la función
                visibilidad = funcion.visibility
                
                print(f"Función: {funcion.name}")
                print(f"  - Visibilidad: {visibilidad}")
                
                # Ejemplo de detección simple
                if visibilidad == 'public':
                    print("  [!] Nota: Esta función es pública y puede ser llamada por cualquiera.")
                
                print("-" * 30)

    except Exception as e:
        print(f"Error al analizar el contrato: {e}")

if __name__ == "__main__":
    # Asegúrate de tener ejemplo.sol en la misma carpeta o cambia la ruta
    analizar_contrato('not-so-smart-contracts/denial_of_service/auction.sol')