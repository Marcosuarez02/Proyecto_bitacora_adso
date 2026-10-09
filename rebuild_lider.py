import os
import subprocess

repo_dir = r"C:\proyecto-bitacora\lider"
file_path = os.path.join(repo_dir, "2026", "SEPTIEMBRE", "SEMANA3", "bitacora-03.txt")

entries = [
    {
        "id": 11,
        "text": """id: 11
fecha: 17/09/2026
hora: 4:02pm - 4:08pm
autor: Marco Antonio Suarez Gonzalez
actividad: Redacta y crea un nuevo archivo denominado config.json con el texto descriptivo de la estructura develop.
impedimentos: Sin impedimentos operativos
plan: Construye el archivo de configuración dentro de la rama develop.
""",
        "commit": "feat(septiembre-semana3): [ID 11] redacta y crea archivo config.json en develop"
    },
    {
        "id": 12,
        "text": """id: 12
fecha: 17/09/2026
hora: 4:08pm - 4:14pm
autor: Marco Antonio Suarez Gonzalez
actividad: Envía al área de preparación el archivo de configuración config.json.
impedimentos: Sin impedimentos operativos
plan: Agrega el archivo de configuración al área de preparación de la rama.
""",
        "commit": "feat(septiembre-semana3): [ID 12] envia config.json al area de preparacion"
    },
    {
        "id": 13,
        "text": """id: 13
fecha: 17/09/2026
hora: 4:14pm - 4:20pm
autor: Marco Antonio Suarez Gonzalez
actividad: Registra los cambios de configuración en el historial mediante un commit en la rama develop.
impedimentos: Sin impedimentos operativos
plan: Consolida el commit correspondiente a la rama develop.
""",
        "commit": "feat(septiembre-semana3): [ID 13] registra commit de configuracion en develop"
    },
    {
        "id": 14,
        "text": """id: 14
fecha: 17/09/2026
hora: 4:20pm - 4:26pm
autor: Marco Antonio Suarez Gonzalez
actividad: Crea la rama feature/reportes e ingresa directamente a ella para iniciar el nuevo módulo.
impedimentos: Sin impedimentos operativos
plan: Crea la rama de características feature/reportes.
""",
        "commit": "feat(septiembre-semana3): [ID 14] crea y salta a la rama feature/reportes"
    },
    {
        "id": 15,
        "text": """id: 15
fecha: 17/09/2026
hora: 4:26pm - 4:32pm
autor: Marco Antonio Suarez Gonzalez
actividad: Desarrolla el archivo funcional reporte.js incorporando su respectivo contenido de código.
impedimentos: Sin impedimentos operativos
plan: Diseña y escribe el archivo base de reportes.
""",
        "commit": "feat(septiembre-semana3): [ID 15] desarrolla codigo base de reporte.js"
    },
    {
        "id": 16,
        "text": """id: 16
fecha: 17/09/2026
hora: 4:32pm - 4:38pm
autor: Marco Antonio Suarez Gonzalez
actividad: Traslada el archivo reporte.js hacia el área de preparación.
impedimentos: Sin impedimentos operativos
plan: Prepara el archivo de reporte en el Staging Area.
""",
        "commit": "feat(septiembre-semana3): [ID 16] traslada reporte.js al staging area"
    },
    {
        "id": 17,
        "text": """id: 17
fecha: 17/09/2026
hora: 4:38pm - 4:44pm
autor: Marco Antonio Suarez Gonzalez
actividad: Asegura y sella el archivo de reportes en el historial del repositorio con un commit.
impedimentos: Sin impedimentos operativos
plan: Registra los cambios iniciales de reportes en la historia del proyecto.
""",
        "commit": "feat(septiembre-semana3): [ID 17] sella primer commit del modulo de reportes"
    },
    {
        "id": 18,
        "text": """id: 18
fecha: 17/09/2026
hora: 4:44pm - 4:50pm
autor: Marco Antonio Suarez Gonzalez
actividad: Añade una segunda modificación dentro del archivo reporte.js utilizando el editor de texto.
impedimentos: Sin impedimentos operativos
plan: Agrega modificaciones secundarias al código fuente.
""",
        "commit": "feat(septiembre-semana3): [ID 18] añade modificaciones secundarias en reporte.js"
    },
    {
        "id": 19,
        "text": """id: 19
fecha: 17/09/2026
hora: 4:50pm - 4:56pm
autor: Marco Antonio Suarez Gonzalez
actividad: Prepara el archivo reporte.js incorporando las nuevas modificaciones realizadas.
impedimentos: Sin impedimentos operativos
plan: Mueve las nuevas modificaciones al Staging Area.
""",
        "commit": "feat(septiembre-semana3): [ID 19] prepara cambios secundarios en el staging area"
    },
    {
        "id": 20,
        "text": """id: 20
fecha: 17/09/2026
hora: 4:56pm - 5:02pm
autor: Marco Antonio Suarez Gonzalez
actividad: Confirma y genera un commit para identificar la actualización del reporte funcional.
impedimentos: Sin impedimentos operativos
plan: Consolida el commit correspondiente a la actualización de reportes.
""",
        "commit": "feat(septiembre-semana3): [ID 20] confirma commit de actualizacion de reportes"
    },
    {
        "id": 21,
        "text": """id: 21
fecha: 17/09/2026
hora: 5:02pm - 5:08pm
autor: Marco Antonio Suarez Gonzalez
actividad: Regresa a la rama principal de integración develop.
impedimentos: Sin impedimentos operativos
plan: Conmuta nuevamente a la rama develop.
""",
        "commit": "feat(septiembre-semana3): [ID 21] regresa a rama de integracion develop"
    },
    {
        "id": 22,
        "text": """id: 22
fecha: 17/09/2026
hora: 5:08pm - 5:15pm
autor: Marco Antonio Suarez Gonzalez
actividad: Fusiona en develop todos los avances completados en la rama feature/reportes.
impedimentos: Sin impedimentos operativos
plan: Integra los avances de la rama feature/reportes en develop.
""",
        "commit": "feat(septiembre-semana3): [ID 22] fusiona rama feature/reportes en develop"
    }
]

# Ensure git is on feature/septiembre-semana3
subprocess.run(["git", "checkout", "feature/septiembre-semana3"], cwd=repo_dir, check=True)

for item in entries:
    sep = "________________________________________\n" if os.path.exists(file_path) and os.path.getsize(file_path) > 0 else ""
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(sep + item["text"])
    
    subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)
    res = subprocess.run(["git", "commit", "-m", item["commit"]], cwd=repo_dir, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"Error on ID {item['id']}: {res.stderr}")
    else:
        print(f"ID {item['id']} committed successfully.")

print("All IDs 11 to 22 created with adjusted schedule.")
