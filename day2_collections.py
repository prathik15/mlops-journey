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



