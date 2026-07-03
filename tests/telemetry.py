import fastf1
import pandas as pd
import os
import sqlite3
import logging

logging.basicConfig(
    filename='f1_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Initializating telemetry extraction process...")

try:
    if not os.path.exists('cache'):
        os.makedirs('cache')
    fastf1.Cache.enable_cache('cache')
    
    year = pd.Timestamp.now().year
    schedule = fastf1.get_event_schedule(year)
    now_utc = pd.Timestamp.now(tz='UTC').tz_localize(None)
    past_races = schedule[schedule['Session1DateUtc'] < now_utc]
    
    last_gp = past_races.iloc[-1]['RoundNumber']
    event_name = past_races.iloc[-1]['EventName']
    
    logging.info(f"Last race detected: {event_name} (Round {last_gp})")
    
    GP = fastf1.get_session(year, event_name, 'SQ')
    GP.load(telemetry=True) 
    
    colapinto = GP.laps.pick_drivers('COL')

    filas_iniciales = len(colapinto)
    
    colapinto = colapinto.dropna(subset=['LapTime'])

    colapinto['LapTime_sec'] = colapinto['LapTime'].dt.total_seconds()
    
    filas_finales = len(colapinto)
    logging.info(f"Clean data: {filas_iniciales - filas_finales} invalid laps were discarded.")
    
    conexion = sqlite3.connect('f1_telemetry.db')

    columnas_sql = ['Driver', 'LapNumber', 'LapTime_sec', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Compound']
    colapinto[columnas_sql].astype(str).to_sql('franco_laps', conexion, if_exists='replace', index=False)
    conexion.close()
    
    logging.info("Data saved succesfully on the Data Base.")

except Exception as e:
    logging.error(f"Pipeline critical failure: {e}")