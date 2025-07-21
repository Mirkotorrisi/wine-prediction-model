from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import numpy as np
import joblib



# Load the wine dataset and split it into training and testing sets
data = load_wine()

X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

np.savetxt("assets/wine_x_test.csv", X_test, delimiter=",", fmt="%d")
np.savetxt("assets/wine_y_test.csv", y_test, delimiter=",", fmt="%d")

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Export to ONNX
initial_type = [("input", FloatTensorType([None, X.shape[1]]))]
onnx_model = convert_sklearn(model, initial_types=initial_type)

with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

# Save the model to a pkl file, but needs to be loaded with joblib (and sklearn)
# with open("assets/wine_model.pkl", "wb") as model_file:
#     joblib.dump(model, model_file)
