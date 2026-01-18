import matplotlib.pyplot as plt
from data_loader import load_data
from deterministic_model import fit_linear_model, predict

prices = load_data()
train = prices[:int(0.7 * len(prices))]
test = prices[int(0.7 * len(prices)):]

coeffs = fit_linear_model(train)
pred = predict(coeffs, len(prices))

plt.figure(figsize=(10, 5))
plt.plot(prices.index, prices, label="True Price")
plt.plot(prices.index, pred, linestyle="--", label="Deterministic Prediction")
plt.axvline(train.index[-1], color="red", linestyle=":", label="Train/Test Split")

plt.legend()
plt.title("Deterministic Model Failure During Market Stress")
plt.tight_layout()
plt.savefig("deterministic_failure.png")
plt.show()
