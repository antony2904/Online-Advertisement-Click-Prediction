# AdClick Analytics — Separate Files

## Folder structure
```text
AdClick_Analytics_Separate_Files/
├── app.py
├── styles.py
├── requirements.txt
├── README.md
├── utils/
│   ├── __init__.py
│   ├── data_utils.py
│   └── model_utils.py
└── views/
    ├── __init__.py
    └── pages.py
```

## Run on Windows PowerShell
```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\\venv\\Scripts\\Activate.ps1
```

Put `advertising.csv` beside `app.py`, or upload it using the sidebar.

## Required CSV columns
- Daily Time Spent on Site
- Age
- Area Income
- Daily Internet Usage
- Male
- Clicked on Ad

`Clicked on Ad` must contain 0 or 1.

## File responsibilities
- `app.py`: Main application, navigation, data upload and routing.
- `styles.py`: Dark black-and-red theme.
- `utils/data_utils.py`: Dataset validation and cleaning.
- `utils/model_utils.py`: Preprocessing, Logistic Regression and evaluation.
- `views/pages.py`: Dashboard, dataset explorer, visualizations, model performance, prediction and about pages.
