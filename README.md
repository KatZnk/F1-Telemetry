```markdown
# F1 Telemetry Pipeline & Analysis

A data engineering and visualization pipeline developed in **Python** to extract, process, and analyze official **Formula 1** telemetry using the `FastF1` library. The processed data is stored locally in an SQLite database for subsequent graphical analysis.

## 🚀 Key Features
- **Automated Extraction:** Connection with the FastF1 API to download free practice session data (FP1), filtering out invalid laps and discarding records with null data.
- **Database Persistence:** Structured storage in SQLite (`f1_telemetry.db`), separating detailed fastest-lap telemetry from general session lap times per driver.
- **Event Logging:** A logging system (`f1_pipeline.log`) for traceability and error control during the extraction process.
- **Data Visualization:** Generation of comparative speed-by-distance charts and circuit GPS trace maps using `matplotlib`.

## 📂 Project Structure

```text
├── .env.example            # Environment variables template
├── .gitignore              # Files ignored by Git (cache, databases, logs)
├── LICENSE                 # Open-source license (MIT)
├── README.md               # Project documentation
├── pipeline.py             # Extraction, cleaning, and SQLite storage script
└── plot_telemetry.py       # Telemetry plotting and GPS comparison script

```

## ⚙️ Requirements & Installation

Make sure you have Python installed, then run the following commands to install the required dependencies:

```bash
pip install pandas matplotlib fastf1 python-dotenv

```

## 💻 Usage

1. **Configure Environment:** Create a `.env` file based on `.env.example` if you want to customize the database name (by default, `f1_telemetry.db` will be used).
2. **Run the Extraction Pipeline:**
```bash
python pipeline.py

```


3. **Generate Visualizations:**
```bash
python plot_telemetry.py

```



## 🛠️ Technologies Used

* **Python 3.x**
* **FastF1** (Telemetry API)
* **Pandas** (Data manipulation)
* **SQLite3** (Relational database)
* **Matplotlib** (Data visualization)

```

```
