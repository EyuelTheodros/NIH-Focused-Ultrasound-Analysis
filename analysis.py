import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("DatanCleaning.xlsx",sheet_name=0)

top_institutions = (
    df.groupby("Organization Name")["Total Cost"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


print("Top 10 Institutions by Total Funding")
print(top_institutions)

plt.figure(figsize=(10,6))
top_institutions.plot(kind="barh", color="steelblue")
plt.xlabel("Total Funding ($)")
plt.title("Top 10 Institutions by NIH Focused Ultrasound Funding")
plt.tight_layout()
plt.savefig("top_institutions.png")
plt.show()