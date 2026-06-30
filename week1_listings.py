import pandas as pd
from pathlib import Path

folder = Path(".")

# find all Listing CSV
listing_files = sorted(folder.glob("CRMLSListing20*.csv"))

# combined
listing = pd.concat(
    [pd.read_csv(file) for file in listing_files],
    ignore_index=True
)

# before filter 
print("Listing rows before filter:", len(listing))

# Residential filter
listing = listing[listing["PropertyType"] == "Residential"]

# after filter 
print("Listing rows after filter:", len(listing))

listing.to_csv(
    "combined_listing_202401_202604_residential.csv",
    index=False
)
