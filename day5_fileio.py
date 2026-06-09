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
    