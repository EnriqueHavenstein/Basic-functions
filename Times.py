# Calculate cycle time and cycles per minute
# Inputs: total time and number of cycles

total_time = float(input("Total time in seconds: "))
cycles = float(input("Number of cycles: "))

cycle_time = total_time / cycles
cycles_per_minute = cycles / total_time * 60

print(f"Cycle time: {cycle_time} seconds")
print(f"Cycles per minute: {cycles_per_minute}")

# Calculate pace and speed

distance = int(input('Distance (m): '))
time = int(input('Time (s): '))

speed = (distance / 1000) / (time / 3600)

pace = (time / 60) / (distance / 1000)  # develop a way to see the format 4'25"

print('Speed = {} km/h.'.format(speed))
print('Pace = {} min/km.'.format(pace))