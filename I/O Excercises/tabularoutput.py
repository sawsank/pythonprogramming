names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score':<5}")
print("-" * 15)
for name, score in zip(names, scores):
    print(f"{name:<10} {score:<5}")