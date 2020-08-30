# We have some data that contains a mixture of flowers and shrubs, in a list.
# Our customer would like two separate lists.
# One, called  flowers, will contain only flowers, and the other, not surprisingly called shrubs , must contain only shrubs.
# Write code to populate the two lists with the appropriate plants from data.
# Write your code below the comment, starting on line 35.
# There is no need to print the lists, but you can if you wish.
# Hint: Note that "flower" will not match "Flower" (with a capital F) in Python.

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for plant in data:
    if "Flower" in plant:
        flowers.append(plant)
    elif "Shrub" in plant:
        shrubs.append(plant)
print(flowers)
print("-" * 5)
print(shrubs)