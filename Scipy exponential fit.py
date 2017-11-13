from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np

parameters = expon.fit(df["time"],floc=0)

x = np.linspace(df["time"].min(), df["time"].max(), len(df["time"]))

pdf_fitted = expon.pdf(x, *parameters)

plt.plot(x, pdf_fitted, color='r'),plt.hist(df["time"], normed=True)
