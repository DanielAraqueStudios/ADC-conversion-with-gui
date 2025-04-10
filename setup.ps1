# Crear entorno virtual si no existe
if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

# Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
python -m pip install -r requirements.txt
