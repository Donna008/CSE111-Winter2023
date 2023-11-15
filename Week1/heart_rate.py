"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate betwee"""

age = int(input('What is your age?'))
max_rate = (220-age)
slowst_rate = (max_rate * 0.65)
fastes_rate = (max_rate * 0.85)
print("when you exercise to strengthen your heart, you should maintain" )
print(f"keep your heart rate between {slowst_rate: .0f} and {fastes_rate: .0f}")
print("beats heart rate pre minute")