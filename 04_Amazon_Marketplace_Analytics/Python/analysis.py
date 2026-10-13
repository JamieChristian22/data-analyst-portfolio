"""Run this project's real SQL/Python pipeline from any working directory."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from portfolio.run import run_project
if __name__=='__main__':
    print(run_project(ROOT,Path(__file__).resolve().parents[1].name))
