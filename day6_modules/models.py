"""
models.py — Data and logic layer for the ML Model Tracker.
 
Responsibilities:
    - Define the model data
    - Load and save models to JSON
    - Filter, flag, and validate models
 
Used by: main.py
"""

import json
import os
from datetime import datetime
from pathlib import Path

# ── Constants ─────────────────────────────────────────────────────────────────

MODELS_FILE: str = "models.json"
RETRAINING_THRESHOLD: float = 0.80
REPORT_WIDTH: int = 55

# ── Data ──────────────────────────────────────────────────────────────────────

def get_models() -> list[dict]:
    """Return the default list of ml model records.
        Returns:
        list[dict]: Each dict contains name, algorithm, accuracy, and status.
    """
    return [
        {"name":"LogisticRegression", "algorithm":"Linear", "accuracy":0.78, "status": "retired"},
        {"name": "RandomForest",       "algorithm": "Ensemble", "accuracy": 0.91, "status": "deployed"},
        {"name": "XGBoost",            "algorithm": "Boosting", "accuracy": 0.94, "status": "deployed"},
        {"name": "SVM",                "algorithm": "Kernel",   "accuracy": 0.83, "status": "staging"},
        {"name": "NeuralNetwork",      "algorithm": "Deep",     "accuracy": 0.96, "status": "deployed"},
        {"name": "KNN",                "algorithm": "Instance", "accuracy": 0.74, "status": "retired"},
        {"name": "NaiveBayes",         "algorithm": "Prob",     "accuracy": 0.79, "status": "staging"},
    ]
    
# ── Validation ────────────────────────────────────────────────────────────────

def validate_models(model: dict) -> bool:
    """
    Validate that a model dict has required fields and sensible values.
 
    Args:
        model (dict): The model record to validate.
 
    Returns:
        bool: True if valid.
 
    Raises:
        KeyError: If a required field is missing.
        TypeError: If accuracy is not a number.
        ValueError: If accuracy is outside 0.0–1.0.
    """
    
    for field in ("name", "alrorithm" ,"accuracy", "status"):
        if field not in model:
            raise KeyError(f"Model is missing , the required field is '{field}'")
        
    if not isinstance(model["accuracy"], (int,float)):
        raise TypeError(f"accuracy must be a number, got {type(model["accuracy"].__name__)}")
    
    return True


# ── File I/O ──────────────────────────────────────────────────────────────────

def save_models(models: list[dict], filepath = MODELS_FILE) -> None:
    """
    Serialise the model list to a JSON file.
 
    Args:
        models (list[dict]): The list of model records to save.
        filepath (str): Destination file path. Defaults to MODELS_FILE.
 
    Raises:
        ValueError: If the models list is empty.
    """
    
    if not models:
       raise ValueError("cannot save - models list is empty")
   
    path = path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)          #create folders if needed

    with open(path, "w") as f:
        json.dumps(models, f , indent=4)

    print(f" saved {len(models)} to {filepath}")