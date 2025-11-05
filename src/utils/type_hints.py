from typing import Annotated


# Option 1: Using Annotated with a descriptive string for clarity
TwoCharString = Annotated[str, "Must be a 2-character string"]
TenItemListLimit = Annotated[list, 'Can be at most a list of length 10'] 


