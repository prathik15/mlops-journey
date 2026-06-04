# _____ Day 02: Collections — Lists & Dictionaries _______________________________
# MLOps Learning Roadmap | Week 1, Day 2
# Concepts: lists (indexing, slicing, append, remove, sort, len)
#           dicts (key/value, .get(), .items(), .keys(), nested dicts)
# ______________________________________________________________________________

# ========= 1. List basics — before we add models ================

frameworks = ['Pytorch', 'Tensorflow', 'scikit-learn', 'XGBoost', 'Keras']

print ("==== list basics ====")

print(f"All frameworks: {frameworks}")
print(f"First item: {frameworks[0]}")
print(f"last item: {frameworks[-1]}")
print (f"first three: {frameworks[:3]}")       #slicing (start:stop)
print (f"first three: {frameworks[:-2]}")      #slicing from back
print(f"middle three: {frameworks[1:4]}")
print(f"total count: {len(frameworks)}")

frameworks.append("LightGBM")
print(f"After append: {frameworks}")

frameworks.remove("XGBoost")
print(f"After remove: {frameworks}")

frameworks.sort()
print(f"After sort: {frameworks}")

# ── 2. Dictionary basics ──────────────────────────────────────────────────────
 
print("\n=== dict basics ===")
 
sample_model = {
    "name"      : "RandomForest",
    "algorithm" : "Ensemble",
    "accuracy"  : 0.91,
    "status"    : "deployed",
}

print(f"keys: {list(sample_model.keys())}")
print(f"name: {sample_model["name"]}")
print(f"accuracy: {sample_model.get("accuracy")}")
print(f"missing-key: {sample_model.get("size", "Not Available")}\n")

print( sample_model.items())
print("\n==Print all Key value pairs==")

for key, value in sample_model.items():
    print(f"{key:<10} : {value}")
print("\n")  

#combining enumerate and items() with dictionaries 
for index, (key,value) in enumerate(sample_model.items(),start=1):
 
    print(f" Field {index} --> {key} : {value}")

# ── 3. Nested dict — model with metadata inside ───────────────────────────────

print("\n==== Nested dict ====")

nested_model = {
    "Name" : "RandomFrest",
    "Accuracy" : 0.91,
    "Status" : "deployed",
    "metadata" : {
        "framework" : "pytorch",
        "epochs" : 10,
    }
}

print(f"model : {nested_model["Name"]}")
print(f"framework : {nested_model["metadata"]["framework"]}")
print(f"epochs : {nested_model["metadata"]["epochs"]}")

# ── 4. Main build — 5 ML models in a list of dicts ───────────────────────────
 
models = [
    {"name": "LogisticRegression", "algorithm": "Linear",    "accuracy": 0.78, "status": "retired"},
    {"name": "RandomForest",       "algorithm": "Ensemble",  "accuracy": 0.91, "status": "deployed"},
    {"name": "XGBoost",            "algorithm": "Boosting",  "accuracy": 0.94, "status": "deployed"},
    {"name": "SVM",                "algorithm": "Kernel",    "accuracy": 0.83, "status": "staging"},
    {"name": "NeuralNetwork",      "algorithm": "Deep",      "accuracy": 0.96, "status": "deployed"},
]
 
 
# ── 5. Filter — only models with accuracy > 0.85 ─────────────────────────────

print("\n==== Filter models problem ====\n")

high_accuracy_models = [m for m in models if m["accuracy"] > 0.85]

for model in high_accuracy_models:
    print(f"name : {model["name"]}")
    print(f"accuracy : {model["accuracy"]}\n")
    
# ── 6. Bonus — sort models by accuracy (best first) ──────────────────────────
 
print("\n=== all models ranked by accuracy ===")

sorted_models = sorted(models, key=lambda x:x["accuracy"], reverse=True)

for model in sorted_models:
    print (f"name: {model["name"]}")
    print (f"accuracy: {model["accuracy"]}")



