import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()
db_filename = os.getenv('DB_NAME', 'f1_telemetry.db')

conexion = sqlite3.connect(db_filename)

query_colapinto = "SELECT * FROM Colapinto_Fastest_Lap"
df_colapinto = pd.read_sql_query(query_colapinto, conexion)

query_gasly = "SELECT * FROM Gasly_Fastest_Lap"
df_gasly = pd.read_sql_query(query_gasly, conexion)

conexion.close()

print(f"Datos listos. Franco: {len(df_colapinto)} filas | Gasly: {len(df_gasly)} filas")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

ax1.plot(df_colapinto['X'], df_colapinto['Y'], color='black', linewidth=2)

ax1.set_aspect('equal') 
ax1.axis('off')         
ax1.set_title("Silverstone: Traza GPS de la Vuelta", fontsize=14, fontweight='bold')


ax2.plot(df_colapinto['Distance'], df_colapinto['Speed'], label='Colapinto', color='blue', linewidth=2)
ax2.plot(df_gasly['Distance'], df_gasly['Speed'], label='Gasly', color='hotpink', linewidth=1.5, alpha=0.8)

ax2.set_title("Comparativa de Velocidad: Franco vs Gasly", fontsize=14, fontweight='bold')
ax2.set_xlabel("Distancia recorrida en pista (metros)", fontsize=11)
ax2.set_ylabel("Velocidad (km/h)", fontsize=11)
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()