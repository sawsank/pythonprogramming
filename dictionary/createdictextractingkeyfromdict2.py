## Using the update() method and loop

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)