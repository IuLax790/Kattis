def calculate_total_chugging_time(initial_time, deterioration_rate, num_bottles):
  """
  Calculates the total time taken to chug a given number of bottles.

  Args:
    initial_time: Time taken to chug the first bottle.
    deterioration_rate: Increase in chugging time per bottle.
    num_bottles: Number of bottles to chug.

  Returns:
    Total time taken to chug all bottles.
  """
  total_time = 0
  for i in range(num_bottles):
    total_time += initial_time + (i * deterioration_rate)
  return total_time

if __name__ == "__main__":
  N = int(input())
  tA, dA = map(int, input().split())
  tB, dB = map(int, input().split())

  alice_time = calculate_total_chugging_time(tA, dA, N)
  bob_time = calculate_total_chugging_time(tB, dB, N)

  if alice_time < bob_time:
    print("Alice")
  elif alice_time > bob_time:
    print("Bob")
  else:
    print("=")
