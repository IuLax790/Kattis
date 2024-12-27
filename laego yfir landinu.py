def has_low_pressure_system(forecast):
  """
  Checks if the forecast contains a low pressure system.

  Args:
    forecast: A list of lists representing the forecast grid.

  Returns:
    "Jebb" if a low pressure system is found, otherwise "Neibb".
  """
  n_rows, n_cols = len(forecast), len(forecast[0])

  for i in range(1, n_rows - 1):
    for j in range(1, n_cols - 1):
      center_pressure = forecast[i][j]
      # Check all four neighbors
      if (center_pressure < forecast[i-1][j] and
          center_pressure < forecast[i+1][j] and
          center_pressure < forecast[i][j-1] and
          center_pressure < forecast[i][j+1]):
        return "Jebb"

  return "Neibb"

if __name__ == "__main__":
  n, m = map(int, input().split())
  forecast =
  for _ in range(n):
    forecast.append(list(map(int, input().split())))
  result = has_low_pressure_system(forecast)
  print(result)
