import pandas as pd
import pylab as pl
data = pd.read_csv("output/dataset.csv.gz")

age_hist = data.age.plot.hist().get_figure()
pl.title("Histogram of participant's age")
pl.xlabel("Age (years)")
pl.ylabel("Individuals")

#age_hist = data.plot(x='age', kind="hist", xlabel="Age (years)")
age_hist.savefig("output/age_hist.png")