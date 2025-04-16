#code snippet only
def find_peak(N):
  current = 0
  while current < N:
    if query(current) < query(current +1):
      current += 1
    else:
      break
  return current 
