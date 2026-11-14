# Online Advertisement Click Prediction

A Streamlit dashboard for exploring advertisement engagement data and predicting whether a user will click an ad. The app trains a Logistic Regression classifier from the supplied dataset and presents model evaluation metrics, visualizations, and individual predictions.

## Features

- Dashboard with dataset and model performance summaries
- Dataset preview, descriptive statistics, and missing-value counts
- Exploratory visualizations for user demographics and internet usage
- Logistic Regression evaluation with accuracy, precision, recall, F1-score, confusion matrix, and ROC-AUC when available
- Interactive prediction form and downloadable test-set predictions

## Requirements

- Python and pip
- A CSV dataset with the required columns listed below

## Run the app

From the project directory, create and activate a virtual environment, install dependencies, and start Streamlit:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

If PowerShell prevents environment activation, allow it for the current terminal session and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Upload your CSV using the app's sidebar. Alternatively, place it in the project directory as `advertising.csv`; the app will load that file automatically when no dataset has been uploaded.

## Dataset format

The CSV must include these columns with exact names:

| Column | Description |
| --- | --- |
| `Daily Time Spent on Site` | Daily time spent on the site |
| `Age` | User age |
| `Area Income` | User's area income |
| `Daily Internet Usage` | Daily internet usage |
| `Male` | Binary indicator encoded as `0` or `1` |
| `Clicked on Ad` | Target label: `0` for not clicked, `1` for clicked |

Values are converted to numeric. Rows with an invalid or missing target, or a target other than `0` or `1`, are excluded. Feature values that cannot be converted are treated as missing and imputed using the median during model training. The `Male` feature is expected to use `0` or `1`. The target needs both classes, with at least two rows per class, to train the model.

## Model and evaluation

The app splits the data into training and test sets using a stratified 67/33 split. Numeric features are median-imputed and standardized before fitting Logistic Regression. The displayed scores and plots are calculated from the test set; results depend on the dataset provided. ROC-AUC is shown when the test set contains both target classes.

## Project files

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit entry point, dataset loading, navigation, and model setup |
| `data.py` | Required-column validation and target cleanup |
| `model.py` | Preprocessing pipeline, classifier training, and evaluation |
| `pages.py` | Dashboard, data exploration, visualizations, evaluation, and prediction pages |
| `styles.py` | Application theme |
| `requirements.txt` | Python package dependencies |
