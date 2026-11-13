from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def train_model(data, features, target):
    X, y = data[features], data[target].astype(int)
    if y.nunique() < 2 or y.value_counts().min() < 2:
        raise ValueError("The target needs both classes (0 and 1), with at least two rows per class.")
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)
    numeric = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
    prep = ColumnTransformer([("numeric", numeric, features)], remainder="drop")
    model = Pipeline([("preprocessing", prep), ("classifier", LogisticRegression(max_iter=1000, random_state=42))])
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    prob = model.predict_proba(x_test)[:, 1]
    result = {
        "model": model, "y_test": y_test, "predictions": pred, "probabilities": prob,
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "confusion": confusion_matrix(y_test, pred, labels=[0, 1]),
        "report": classification_report(y_test, pred, labels=[0, 1],
            target_names=["Not Clicked (0)", "Clicked (1)"], zero_division=0)
    }
    if y_test.nunique() == 2:
        result["auc"] = roc_auc_score(y_test, prob)
        result["roc"] = roc_curve(y_test, prob)
    else:
        result["auc"], result["roc"] = None, None
    return result
