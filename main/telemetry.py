import fastf1
import pandas as pd
import os
import sqlite3
import logging
from dotenv import load_dotenv

load_dotenv()
db_filename = os.getenv('DB_NAME', 'f1_telemetry.db')

logging.basicConfig(
    filename='f1_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Initializing telemetry extraction process...")

def extract_data (df, name, conexion):
    logging.info("Extracting fastest lap telemetry...")
    fast_lap = df.pick_fastest()
    crude_telemetry = fast_lap.get_telemetry()
    
    telemetry_data = ['Distance', 'Speed', 'nGear', 'Throttle', 'Brake', 'RPM', 'X', 'Y']
    clean_telemetry = crude_telemetry[telemetry_data]

    clean_telemetry.to_sql(name+'_Fastest_Lap', conexion, if_exists='replace', index=False)
    logging.info("Fastest lap telemetry saved successfully!")

    starter = len(df)
    df = df.dropna(subset=['LapTime']).copy() 
    df['LapTime_sec'] = df['LapTime'].dt.total_seconds()
    
    ending = len(df)
    logging.info(f"Clean data: {starter - ending} invalid laps were discarded.")
    
    sql_columns = ['Driver', 'LapNumber', 'LapTime_sec', 'Sector1Time', 'Sector2Time', 'Sector3Time', 'Compound']
    df[sql_columns].astype(str).to_sql(name + '_Session_Telemetry', conexion, if_exists='replace', index=False)


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
    
    GP = fastf1.get_session(year, event_name, 'FP1')
    GP.load(telemetry=True) 
    
    colapinto = GP.laps.pick_drivers('COL')
    conexion = sqlite3.connect(db_filename)
    extract_data(colapinto, "Colapinto", conexion)

    gasly = GP.laps.pick_drivers('GAS')
    extract_data(gasly, "Gasly", conexion)

    conexion.close()
    
    logging.info("Data saved successfully in the Data Base.")

except Exception as e:
    logging.error(f"Pipeline critical failure: {e}")