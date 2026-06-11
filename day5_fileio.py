# ── Day 05: File I/O + Exception Handling ────────────────────────────────────
# MLOps Learning Roadmap | Week 1, Day 5
# Concepts: open(), with statement, reading/writing files, CSV manual read,
#           try/except/finally, raise, FileNotFoundError, ValueError, KeyError
# Time estimate: 60–90 mins
# ─────────────────────────────────────────────────────────────────────────────

import json
import os

MODELS_FILE = "models.json"         #global constant --> filename used throughout

# ── 1. Writing files — open() + with statement ────────────────────────────────
# 'with' automatically closes the file when the block ends, even if it crashes.
# Always prefer 'with' over manually calling file.close()

def write_text_demo():
    
    with open("demo.txt","w") as f:         # "w" - write mode
        f.write("ML model tracker log\n")
        f.write("Line 2: written with Python\n")
        
    with open("demo.txt","r") as f:         # "r" - read mode
        contents = f.read()
        
    print("=== plain text file ===")
    print(contents)
        
        
write_text_demo()

# ── 2. Reading a CSV manually ─────────────────────────────────────────────────
# Before using pandas, understand what's underneath

def write_demo_csv():
    with open("models.csv","w") as f:
        f.write("name,algorithm,accuracy\n")
        f.write("BERT,pytorch,98.43\n")
        f.write("RandomForest,Ensemble,0.91\n")
        
def read_demo_csv_manually(filepath):
    """Read a CSV file without pandas — understand the raw mechanics."""
    models=[]
    
    with open(filepath,"r") as f:
        lines = f.readlines()
        
    headers = lines[0].strip().split(",")
    
    for line in lines[1:]:
        values = line.strip().split(",")
        model = dict(zip(headers,values))
        model["accuracy"] = float(model["accuracy"])  #typeconversion
        models.append(model)
        
    return models

write_demo_csv()
csv_models = read_demo_csv_manually("models.csv")

print("=== priting csv manually ===")
for m in csv_models:
    print(f"{m["name"]} --->  {m["accuracy"]}")
    
    