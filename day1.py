# ── Day 01: Python Data Types & ML Model Details ─────────────────────────────
# MLOps Learning Roadmap | Week 1, Day 1
# Concepts: int, float, str, bool, type(), type conversion, f-strings, print()
# ─────────────────────────────────────────────────────────────────────────────


# ── 1. Core data types ────────────────────────────────────────────────────────

model_name    = "ResNet-50"        # str   — model identifier
version       = 1.0                # float — model version
accuracy      = 92.42               # float — percentage accuracy
num_params    = 25000000         # int   — parameter count (underscores ok!)
is_deployed   = True               # bool  — deployment status


# ── 2. Inspecting types with type() ──────────────────────────────────────────
print ("\n === Inspecting Types ===")
print (type(model_name))
print (type(version))
print (type(accuracy))
print (type(num_params))
print (type(is_deployed))


a = input("enter a number: ")
print ("\n === Inspecting Types ===")
print(type(a))

# ── 3. Type conversion ────────────────────────────────────────────────────────

version_str = str(version)
accuracy_int = int(accuracy)
num_params_fl = float(num_params)
isdeployed_int = int(is_deployed)

print(f'{version} --> {version_str}')
print(f'{accuracy} --> {accuracy_int}')
print(f'{num_params} --> {num_params_fl}')
print(f'{is_deployed} --> {isdeployed_int}')

# ── 4. F-strings & formatted print() ─────────────────────────────────────────

status = 'Live' if is_deployed else 'Offline'

print('\n' + '='*40)
print("             Model Summary")
print('='*40)
print(f'Name: {model_name}')
print(f'Version: v{version}')
print(f'Accuracy: {accuracy:.1f}%')
print(f'Parameters: {num_params:,}')
print(f'status: {status}')
print(f'Type check: accuracy is type {type(accuracy).__name__}, is_deployed is type {type(is_deployed).__name__}')

print('\n' + '='*40)

# ── 5. Multiple models — list of dicts ───────────────────────────────────────

models = [{"model": "restnet-50", "version":"1.0", "is_deployed":True}, 
          {"model":"llama", "version":"2.4", "is_deployed": True},
          {"model":"BERT-base", "version": "3.2", "is_deployed": False},]

print("\n ==== All models ====")

for i, m in enumerate(models,start=1):
    # print(f'{i}.{m}')
    print(f'{i}. {m['model']:<25}  v{m['version']}  {m['is_deployed']}')