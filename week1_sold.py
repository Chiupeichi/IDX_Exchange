import pandas as pd
from pathlib import Path

folder = Path(".")

# 找所有 Sold CSV（排除 _filled）
sold_files = sorted(
    file
    for file in folder.glob("CRMLSSold20*.csv")
    if "_filled" not in file.name
)

# 合併
sold = pd.concat(
    [pd.read_csv(file) for file in sold_files],
    ignore_index=True
)

# 印出 filter 前筆數
print("Sold rows before filter:", len(sold))

# Residential filter
sold = sold[sold["PropertyType"] == "Residential"]

# 印出 filter 後筆數
print("Sold rows after filter:", len(sold))

# 輸出 CSV
sold.to_csv(
    "combined_sold_202401_202604_residential.csv",
    index=False
)
