import pandas as pd
from pathlib import Path

base = Path(__file__).resolve().parents[1]
clean = base/'Data'/'clean'
print('Tables:', [p.name for p in clean.glob('*.csv')])
