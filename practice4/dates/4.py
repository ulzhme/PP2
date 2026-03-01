# 4 Calculate difference between two dates in seconds
from datetime import datetime

date1 = datetime(2026, 2, 27, 12, 0, 0)  # Example date
date2 = datetime(2026, 2, 28, 12, 0, 0)  # Example date

difference = (date2 - date1).total_seconds()
print("Difference in seconds:", difference)