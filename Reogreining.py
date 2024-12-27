def reconstruct_dna(n, sequences):
  """
  Reconstructs the DNA sequence from sequenced pieces.

  Args:
    n: The length of the DNA sequence.
    sequences: A list of tuples, where each tuple contains the start position 
               and the sequenced DNA fragment.

  Returns:
    The reconstructed DNA sequence, or "Villa" if there are contradictions.
  """
  dna = ['?' for _ in range(n)]  # Initialize DNA sequence with '?'

  for start, fragment in sequences:
    for i, nucleotide in enumerate(fragment):
      if dna[start + i - 1] == '?' or dna[start + i - 1] == nucleotide:
        dna[start + i - 1] = nucleotide
      elif dna[start + i - 1] != nucleotide:
        return "Villa"  # Contradiction

  return "".join(dna)

if __name__ == "__main__":
  n, m = map(int, input().split())
  sequences = []
  for _ in range(m):
    start, fragment = map(str, input().split())
    start = int(start)
    sequences.append((start, fragment))
  dna_sequence = reconstruct_dna(n, sequences)
  print(dna_sequence)
