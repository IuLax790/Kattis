from collections import defaultdict

def find_most_popular_tiktoker(tiktoks):
  """
  Finds the Tok Tikker with the most total views.

  Args:
    tiktoks: A list of tuples (tok_tikker, views) representing each Tok Tik.

  Returns:
    The name of the most popular Tok Tikker.
  """
  tiktoker_views = defaultdict(int)
  for tok_tikker, views in tiktoks:
    tiktoker_views[tok_tikker] += views

  most_popular_tiktoker = max(tiktoker_views, key=tiktoker_views.get)
  return most_popular_tiktoker

if __name__ == "__main__":
  n = int(input())
  tiktoks = []
  for _ in range(n):
    tok_tikker, views = input().split()
    views = int(views)
    tiktoks.append((tok_tikker, views))
  most_popular = find_most_popular_tiktoker(tiktoks)
  print(most_popular)
