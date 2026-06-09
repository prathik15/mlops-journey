# ── Day 04: Functions ─────────────────────────────────────────────────────────
# MLOps Learning Roadmap | Week 1, Day 4
# Concepts: defining functions, parameters, return values, default arguments,
#           *args, **kwargs, scope (local vs global)
# ─────────────────────────────────────────────────────────────────────────────
 
 
# ── 1. Scope — local vs global ────────────────────────────────────────────────
# Global: defined at module level, accessible everywhere
# Local:  defined inside a function, only lives inside that function

RETRAINING_THRESHOLD = 0.80
REPORT_WIDTH = 55

def demonstrate_scope():
    local_variable = "I exist only inside this function"
    print(f"local variable --> {local_variable}")
    print(f"Global --> RETRAINING_THRESHOLD = {RETRAINING_THRESHOLD} (I exist outside the function as well)")

print("=== Scope demonstration ===")
demonstrate_scope()

# ── 2. Basic function — parameters + return value ────────────────────────────

def add_accuracy_label(accuracy):
    if accuracy >= 0.95:
        print("excellent")
    elif accuracy >= 0.85:
        print("good")
    elif accuracy >= 0.75:
        print("acceptable")
    else:
        print("needs retraining")
        
print("="*10)
add_accuracy_label(0.98)
add_accuracy_label(0.86)
add_accuracy_label(0.77)

# ── 3. Default arguments ──────────────────────────────────────────────────────
# Default value is used when caller doesn't pass that argument

def format_accuracy(accuracy, decimal_places=2, is_percent=True):
    if is_percent:
        return f"{accuracy:.{decimal_places}%}"
    else:    
        return f"{accuracy:.{decimal_places}f}"
    
print ("=== print default arguments ===")
print(format_accuracy(0.98))
print(format_accuracy(0.94, decimal_places=0))
print(format_accuracy(0.86, is_percent=True))


# ── 4. *args — variable number of positional arguments ───────────────────────
# Useful when you don't know how many values will be passed in

def most_accurate_model(*accuracies):
    if accuracies:
        return max(accuracies)
    else:
        return none

print("\n=== *args ===")
print(most_accurate_model(0.4,0.7,0.8,0.9))


# ── 5. **kwargs — variable number of keyword arguments ───────────────────────
# Useful for flexible config / optional metadata
def create_model(name,accuracy, **kwargs):

    """
    Create a model dict. Required: name + accuracy.
    Any extra keyword arguments are stored as metadata.
    """
    model = {
        "name": name,
        "accuracy": accuracy,
        "status" : kwargs.get("status","staging"),
    }
    
    for key,value in kwargs.items():
        if key != "status":
            model[key] = value 
    return model

print("\n === **kwargs ===")
print(create_model("Bert",8.25, status= "deployed", framework= "pytorch", created_at = 2026)) 

# ── 6. Core build — refactored model tracker ─────────────────────────────────
# The same logic from Day 3, now split into clean, reusable functions
 
def get_models():
    """
    Return the full list of ML model records.
    In a real system this would query a database or model registry API.
    """
    return [
        {"name": "LogisticRegression", "algorithm": "Linear",   "accuracy": 0.78, "status": "retired"},
        {"name": "RandomForest",       "algorithm": "Ensemble", "accuracy": 0.91, "status": "deployed"},
        {"name": "XGBoost",            "algorithm": "Boosting", "accuracy": 0.94, "status": "deployed"},
        {"name": "SVM",                "algorithm": "Kernel",   "accuracy": 0.83, "status": "staging"},
        {"name": "NeuralNetwork",      "algorithm": "Deep",     "accuracy": 0.96, "status": "deployed"},
        {"name": "KNN",                "algorithm": "Instance", "accuracy": 0.74, "status": "retired"},
        {"name": "NaiveBayes",         "algorithm": "Prob",     "accuracy": 0.79, "status": "staging"},
    ]
    
def filter_by_accuracy(models, threshold=0.85):
        """
    Return only models with accuracy above the threshold.
    Default threshold is 0.85 — override when calling if needed.
    """
    return [m for m in models["accuracy"] >= threshold]

def flag_for_retraining(models, threshold=None):
    """
    Mark models below the threshold as 'needs_retraining'.
    Mutates status in place. Returns list of flagged model names.
    Uses global RETRAINING_THRESHOLD if no threshold is passed.
    """
    
    cutoff = threshold if threshold is not none else RETRAINING_THRESHOLD
    flagged = []
    
    for model in models:
        if model["accuracy"] < cutoff:
            model["status"] = "needs retraining"
            flagged.append(model["name"])
    return flagged

def print_report(models, title = "ML model status report"):
        """
    Print a formatted status report for a list of models.
    Title is a default argument — override to customise the header.
    """
    
    print("\n" + "="*REPORT_WIDTH)
    print(f"{title}")
    print("\n" + "="*REPORT_WIDTH)
    
    for model in models:
        label = add_accuracy_label(model["accuracy"])
        print(f"model: {model["name"]}")
        print(f"algorithm: {model["algorithm"]}")
        print(f"accuracy: {format_accuracy(model["accuracy"],decimal_places=1)}")
        print(f"status: {model["status"]}")
        print(f"flag: {label}")
        
    avg = sum(m["accuracy"] for m in models)/ len(models)
    best = max(models, key:lambda m:m["accuracy"])
        

    
