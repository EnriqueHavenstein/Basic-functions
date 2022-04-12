# Calculate cycle time and cycles per minute
# Inputs: total time and number of cycles

total_time = float(input("Total time in seconds: "))
cycles = float(input("Number of cycles: "))

cycle_time = total_time / cycles
cycles_per_minute = cycles / total_time * 60

print(f"Cycle time: {cycle_time} seconds.")
print(f"Cycles per minute: {cycles_per_minute}")

