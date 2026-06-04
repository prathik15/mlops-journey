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