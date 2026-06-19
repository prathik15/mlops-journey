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
        f.write("BERT,pytorch,0.82\n")
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
    print(f"{m["name"]:<22} --->  {m["accuracy"]:.0%}")
    
 # ── 3. The model data ─────────────────────────────────────────────────────────
 
def get_models():
    return [
        {"name": "LogisticRegression", "algorithm": "Linear",   "accuracy": 0.78, "status": "retired"},
        {"name": "RandomForest",       "algorithm": "Ensemble", "accuracy": 0.91, "status": "deployed"},
        {"name": "XGBoost",            "algorithm": "Boosting", "accuracy": 0.94, "status": "deployed"},
        {"name": "SVM",                "algorithm": "Kernel",   "accuracy": 0.83, "status": "staging"},
        {"name": "NeuralNetwork",      "algorithm": "Deep",     "accuracy": 0.96, "status": "deployed"},
    ]
# ── 4. Save models to JSON ────────────────────────────────────────────────────

def save_models(models, filepath=MODELS_FILE):
    """Write the models list to a json file
    Raises ValueError if models list is empty - no point in storing a list that is empty"""
    
    if not models:
        raise ValueError("The models list is empty")
    
    with open(filepath, "w") as f:
        json.dump(models,f,indent=4)
        
    print("\n===== wrting to json file =====")    
    print(f" saved {len(models)} to {filepath}")
        
# ── 5. Load models from JSON — with full exception handling ───────────────────

def load_models(filepath=MODELS_FILE):
    """
    Load models from a JSON file.
 
    Handles three failure cases:
      - File doesn't exist yet     → create it with defaults, return defaults
      - File exists but is corrupt → warn and return defaults
      - File exists but is empty   → treat same as corrupt
    """
    try:
        with open(filepath, "r") as f:
            content = f.read().strip()
            
        if not content:
            raise ValueError("The file is empty")
        
        models = json.loads(content)
        print(f"loaded {len(models)} from '{filepath}'")
        return models
    
    except FileNotFoundError:
        # File doesn't exist at all — first run scenario

        print(f"{filepath} not found, creating a file with default models...")
        defaults = get_models()
        save_models(defaults, filepath)
        return defaults
    
    except (json.JSONDecodeError, ValueError) as e:
        # File exists but content is broken or empty
        print(f"could not read '{filepath}' : {e}")
        print(f"falling back to default model")
        return get_models()
    
    finally:
        # finally ALWAYS runs — whether it succeeded, failed, or raised
        print(f"load attempt complete for {filepath}")
        
# ── 6. Demonstrate raise ──────────────────────────────────────────────────────
# 'raise' lets you deliberately trigger an exception with a clear message


def validate_model(model):
    """
    Check a model dict has required fields and valid values.
    Raises descriptive exceptions instead of silently passing bad data.
    """
    if "name" not in model:
        raise KeyError("Model is missing required field: 'name'")
    
    if "accuracy" not in model:
        raise KeyError("Model is missing required field: 'accuracy'")
    
    if not isinstance(model["accuracy"], (int,float)):
        raise TypeError(f"accuracy must be a number, got {type(model["accuracy"]).__name__}")
    
    if not [0.0 <= model["accuracy"] <= 1.0]:
        raise ValueError(f"accuracy must be a 0 and 1, got {model["accuracy"]}")
    
    return True    # all checks passed


print("\n ==== validate model with raise ===")

# Test 1: valid model — should pass
try:
    validate_model({"name":"XGBoost", "accuracy":0.94})
    print("valid model passed validation")
    
except(KeyError, ValueError, TypeError) as e:
    print(f"X {e}")
    
# Test 2: missing name — should raise KeyError

try:
    validate_model({"accuracy":0.94})
    print("passed")
except KeyError as e:
    print(f"keyerror caught: {e}")
    
# Test 3: accuracy out of range — should raise ValueError
try:
    validate_model({"name":"badmodel", "accuracy": 1.82})
    print("passed")
except ValueError as e:
    print(f"valueError caught: {e}")
    
    
# ── 7. Simulate corrupted file ────────────────────────────────────────────────

def simmulate_corrupted_file(filepath="corrupted.json"):
    with open(filepath,"w") as e:
        e.write("this is a corrupted file!")
    return filepath    
  # ── 8. Run the full pipeline ──────────────────────────────────────────────────
 
print("\n" + "=" * 50)
print("  PIPELINE: save → corrupt → reload → fallback")
print("=" * 50)

# Step 1: save good data
print("\n step1 ---> Save")
save_models(get_models())

# Step 2: load normally
print("\n-- Step 2: load (should succeed) --")
models = load_models()

# Step 3: corrupt the file and try loading
print("\n-- Step 3: load corrupted file --")
bad_file = simmulate_corrupted_file()
models = load_models(bad_file)

# Step 4: load from non-existent file
print("\n-- Step 4: load missing file --")

if os.path.exists("temp.json"):
    os.remove("temp.json")
models = load_models("temp.json")

print("\n" + "=" * 50)
print(f"  Pipeline complete. {len(models)} models ready.")
print("=" * 50)

