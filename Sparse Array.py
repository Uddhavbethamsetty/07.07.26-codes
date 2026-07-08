sparse_array = {2: 10, 5: 45, 102: 99}

def get_val(idx):
    return sparse_array.get(idx, 0)

print(f"Value at index 5: {get_val(5)}")
print(f"Value at index 20: {get_val(20)}")
