# F1 Telemetry Pipeline & Analysis

Un pipeline de ingeniería de datos y visualización desarrollado en **Python** para extraer, procesar y analizar telemetría oficial de la **Fórmula 1** utilizando la librería `FastF1`. Los datos procesados se almacenan de forma local en una base de datos SQLite para su posterior análisis gráfico.

## 🚀 Características principales
- **Extracción automatizada:** Conexión con la API de FastF1 para descargar datos de sesiones de práctica (FP1), filtrando vueltas válidas y descartando registros con datos nulos.
- **Persistencia en Base de Datos:** Almacenamiento estructurado en SQLite (`f1_telemetry.db`) separando la telemetría detallada de la vuelta rápida y los tiempos generales de sesión por piloto.
- **Registro de Eventos (Logging):** Sistema de logs (`f1_pipeline.log`) para la trazabilidad y control de errores en el proceso de extracción.
- **Visualización de Datos:** Generación de gráficos comparativos de velocidad por distancia y mapas de traza GPS en circuito utilizando `matplotlib`.

## 📂 Estructura del Proyecto

```text
├── .env.example            # Plantilla de variables de entorno
├── .gitignore              # Archivos ignorados por Git (caché, bases de datos, logs)
├── LICENSE                 # Licencia de código abierto (MIT)
├── README.md               # Documentación del proyecto
├── pipeline.py             # Script de extracción, limpieza y almacenamiento en SQLite
└── plot_telemetry.py       # Script de ploteo y comparación de telemetría y trazas GPS

⚙️ Requisitos e Instalación
Asegúrate de tener Python instalado y ejecuta los siguientes comandos para instalar las dependencias necesarias:

pip install pandas matplotlib fastf1 python-dotenv

💻 Uso
Configurar el entorno: Crea un archivo .env basado en .env.example si deseas personalizar el nombre de la base de datos (por defecto se usará f1_telemetry.db).

Ejecutar el pipeline de extracción:
  python pipeline.py

Generar las visualizaciones:
  python plot_telemetry.py

🛠️ Tecnologías utilizadas
Python 3.x

FastF1 (Telemetry API)

Pandas (Manipulación de datos)

SQLite3 (Base de datos relacional)

Matplotlib (Visualización de gráficos)
