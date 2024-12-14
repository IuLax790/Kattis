def calculate_alcohol_content(ingredients):
    """
    Calculates the total alcohol content of a shot.

    Args:
      ingredients: A list of tuples, where each tuple represents an ingredient 
                    and contains the volume (in centiliters) and alcohol content (in percent).

    Returns:
      The total alcohol content of the shot in centiliters.
    """
    total_alcohol = 0
    for volume, alcohol_content in ingredients:
        total_alcohol += (volume / 100) * alcohol_content
    return total_alcohol

if __name__ == "__main__":
    a, b = map(int, input().split())
    shot1_ingredients = []
    for _ in range(a):
        volume, alcohol_content = map(int, input().split())
        shot1_ingredients.append((volume, alcohol_content))

    shot2_ingredients = []
    for _ in range(b):
        volume, alcohol_content = map(int, input().split())
        shot2_ingredients.append((volume, alcohol_content))

    alcohol_content_shot1 = calculate_alcohol_content(shot1_ingredients)
    alcohol_content_shot2 = calculate_alcohol_content(shot2_ingredients)

    if abs(alcohol_content_shot1 - alcohol_content_shot2) < 1e-6:
        print("same")
    else:
        print("different")
