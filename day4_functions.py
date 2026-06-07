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
def create_model(name,):

    """
    Create a model dict. Required: name + accuracy.
    Any extra keyword arguments are stored as metadata.
    """



    
