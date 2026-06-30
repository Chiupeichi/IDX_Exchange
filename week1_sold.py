import pandas as pd
from pathlib import Path

folder = Path(".")

# find all Sold CSV（excluded _filled）
sold_files = sorted(
    file
    for file in folder.glob("CRMLSSold20*.csv")
    if "_filled" not in file.name
)

# combined
sold = pd.concat(
    [pd.read_csv(file) for file in sold_files],
    ignore_index=True
)

# before filter 
print("Sold rows before filter:", len(sold))

# Residential filter
sold = sold[sold["PropertyType"] == "Residential"]

# after filter 
print("Sold rows after filter:", len(sold))

sold.to_csv(
    "combined_sold_202401_202604_residential.csv",
    index=False
)
