KB = 1024
MB = 1048576
GB = 1073741824

num_entries = float(input("Please enter the number of entries per second: "))
entry_size = float(input("Please enter the average number of bytes per entry: "))

bytes_per_second = num_entries * entry_size

kb_size = (bytes_per_second * 60) / KB
mb_size = (bytes_per_second * 3600) / MB
gb_size = (bytes_per_second * 86400) / GB

print("\nStorage Estimates:")
print(f"Per minute: {kb_size}KB")
print(f"Per hour: {mb_size}MB")
print(f"Per day: {gb_size}GB")