# 🚀 Automatización del TFM (Compilación Automática a PDF)

Para mantener el documento final del TFM siempre actualizado y evitar inconsistencias, este repositorio incluye un **hook de Git (`pre-commit`)**. 

Este script se ejecuta de forma automática en tu entorno local cada vez que intentas hacer un commit, asegurando que todos los fragmentos Markdown se unifiquen, se inserten los saltos de página correctos y se compile el PDF final antes de subir los cambios a GitHub.

---

## 🛠️ ¿Qué hace exactamente este automatismo?

El script actúa como un filtro inteligente y realiza las siguientes tareas **solo si el mensaje de tu commit empieza por el prefijo `docs:`** (por ejemplo: `git commit -m "docs: corregida la introducción"`):

1. **Filtro por prefijo:** Verifica si estás editando documentación. Si tu commit no empieza por `docs:`, el script se salta para no quitarte tiempo si solo estás subiendo código o scripts auxiliares.
2. **Control de dependencias:** Comprueba si tienes `pandoc` instalado en tu sistema. Si no lo encuentra, detiene el commit y te avisa para evitar generar archivos corruptos.
3. **Consolidación de la Sección 4:** Limpia el archivo de la sección 4 y concatena en orden todos los subapartados que se encuentren dentro de `docs-TFM-UNIR/Entrega/4. Desarrollo específico de la contribución/*`, añadiendo un salto de página (`\newpage`) al final de cada uno.
4. **Generación del `documento_final.md`:** Une todos los capítulos `.md` de la carpeta `Entrega/` en un único documento maestro, insertando saltos de página limpios entre capítulos para respetar el formato académico.
5. **Compilación a PDF:** Invoca a `pandoc` de forma automática para renderizar `documento_final.md` en el PDF definitivo (`documento_final.pdf`).
6. **Auto-stage:** Añade (`git add`) automáticamente los archivos generados (`.md` y `.pdf`) al commit en curso, garantizando que lo que subes a GitHub coincida exactamente con tu última versión.

---

## ⚙️ Cómo activarlo en tu ordenador (Solo una vez)

Dado que la carpeta `.git/` es estrictamente local y no se sincroniza entre miembros del equipo, debes indicarle a tu Git local que ejecute los hooks compartidos que están en la carpeta `.githooks/`.

Sigue estos pasos en tu terminal (en la raíz del proyecto):

### 1. Vincular la carpeta de hooks compartida
Ejecuta el siguiente comando para mapear los hooks del repositorio:
```bash
git config core.hooksPath .githooks

```

### 2. Asegurar permisos de ejecución (Solo si estás en Linux/macOS)

Para asegurarte de que tu sistema operativo permite que Git ejecute el script, dale permisos con:

```bash
chmod +x .githooks/pre-commit

```

¡Listo! Ya tienes el entorno configurado.

---

## 💡 Flujo de trabajo diario

A partir de ahora, cuando trabajes en la documentación:

* **Para compilar el PDF automáticamente:** Asegúrate de nombrar tu commit con el prefijo `docs:`.
```bash
git add .
git commit -m "docs: añadida la conclusión del proyecto"

```


*Verás cómo la terminal te muestra el progreso de la concatenación y la compilación de Pandoc antes de dar el commit por bueno.*
* **Para commits normales (sin compilar el PDF):** Haz el commit como de costumbre sin el prefijo.
```bash
git commit -m "feat: actualizado script de limpieza de datos"

```


* **En caso de emergencia (Si no tienes Pandoc instalado):** Si estás trabajando desde un ordenador secundario sin `pandoc` y necesitas subir un cambio en los Markdown urgentemente, puedes saltarte el script añadiendo el flag `--no-verify`:
```bash
git commit -m "docs: corrección rápida de typo" --no-verify

```


