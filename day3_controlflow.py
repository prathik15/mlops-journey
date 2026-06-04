# ── Day 03: More Collections + Control Flow ──────────────────────────────────
# MLOps Learning Roadmap | Week 1, Day 3
# Concepts: sets, tuples, if/elif/else, for loops, while loops, break, continue
# ─────────────────────────────────────────────────────────────────────────────
 
 
# ── 1. Tuples — immutable, ordered ───────────────────────────────────────────
# Use when the data should NOT change: thresholds, config, coordinates

ACCURACY_THRESHOLD = (0.80,0.90,0.95)
VALID_STATUSES      = ("deployed", "staging", "retired", "needs_retraining")

print(f"accuracy threshold : {ACCURACY_THRESHOLD}")
print(f"restraining flag : {VALID_STATUSES[0]}")
print(f"type check : {type(VALID_STATUSES[0]).__name__}")

# tuple unpacking
low, good, excellent = ACCURACY_THRESHOLD
print(f"unpacked : low ={low}, medium ={good} and high ={excellent}")

# ── 2. Sets — unordered, unique values only ───────────────────────────────────
# Use when you need deduplication or fast membership checks
 
deployed_teams  = {"team-alpha", "team-beta", "team-alpha", "team-gamma"}
monitering_tags = {"team-alpha", "team-beta", "team-gamma"}

# set operations
print(f"deployed teams : {deployed_teams}")
print(f"monitering tags : {monitering_tags}")

print(f"in both : {deployed_teams & monitering_tags}")
print(f"in either : {deployed_teams | monitering_tags}")
print(f"only one : {deployed_teams - monitering_tags}")

print(f" 'team-beta' monitored? : {'team-beta' in deployed_teams}")

# ── 3. Main build — extended model list ──────────────────────────────────────
 
models = [
    {"name": "LogisticRegression", "algorithm": "Linear",   "accuracy": 0.78, "status": "retired"},
    {"name": "RandomForest",       "algorithm": "Ensemble", "accuracy": 0.91, "status": "deployed"},
    {"name": "XGBoost",            "algorithm": "Boosting", "accuracy": 0.94, "status": "deployed"},
    {"name": "SVM",                "algorithm": "Kernel",   "accuracy": 0.83, "status": "staging"},
    {"name": "NeuralNetwork",      "algorithm": "Deep",     "accuracy": 0.96, "status": "deployed"},
    {"name": "KNN",                "algorithm": "Instance", "accuracy": 0.74, "status": "retired"},
    {"name": "NaiveBayes",         "algorithm": "Prob",     "accuracy": 0.79, "status": "staging"},
]
 
 
# ── 4. if / elif / else — classify each model ────────────────────────────────

def classify_model(accuracy):
    if accuracy >= excellent:
        return("Excellent!")
    elif accuracy >= good:
        return("Good")
    elif accuracy >= low:
        return("Acceptable")
    else:
        return("Needs retraining")
        
# ── 5. for loop — full status report ─────────────────────────────────────────

print("\n" + "="*50)
print("\n           ML model status report")
print("\n" + "="*50)

flagged_models = []

for model in models:
    label = classify_model(model["accuracy"])
    
    print(f"\nname: {model["name"]}")
    print(f"algorithm: {model["algorithm"]}")
    print(f"accuracy: {model["accuracy"]}")
    print(f"label: {label}")
    
    if model["accuracy"] < low:
        model["status"] = "needs_retraining"
        flagged_models.append(model["name"])
        
print(f"\n {flagged_models}")

print("\n" + "=" * 55)

# ── 6. continue — skip retired models in a second pass ───────────────────────

for model in models:
    if model["status"] == "needs_retraining":
        continue
    print(f"\n {model["name"]:<20}    {model["accuracy"]}   {model["status"]}")
    
# ── 7. break — stop as soon as we find the first deployed model ───────────────

print("\n ==== printing the first deployed model ====")

for model in models:
    if model["status"] == "deployed":
        print(f"\n {model["name"]:<20}    {model["accuracy"]}   {model["status"]}")
        break

# ── 8. while loop — simulate a retraining queue ──────────────────────────────
 
print("\n=== retraining queue ===")

retraining_queue = flagged_models.copy()

while retraining_queue:
    current = retraining_queue.pop(0)
    print(f"{current} model retraining ......... done")
    
print("queue cleared!")
   
# ── 9. Summary ────────────────────────────────────────────────────────────────
   
    
print("\n" + "=" * 55)
print("SUMMARY")
print("-" * 55)
print(f" Total models: {len(models)}")
print(f" flagged models: {len(flagged_models)} - {flagged_models}")
print(f" unique models: {len({m["name"] for m in models})}")
print(f" unique algorithm: {len({m["algorithm"] for m in models})}")
print("=" * 55)