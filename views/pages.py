import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def dashboard(df, r, target):
    st.markdown('<div class="hero-card"><div class="hero-eyebrow">Machine Learning • Classification</div><div class="hero-title">Advertisement Intelligence</div><p class="hero-subtitle">Understand audience behaviour and predict advertisement clicks with Logistic Regression.</p></div>', unsafe_allow_html=True)
    st.subheader("Performance Overview")
    n, clicked = len(df), int((df[target] == 1).sum())
    a,b,c,d = st.columns(4)
    a.metric("Total Records", f"{n:,}")
    b.metric("Clicked Ads", f"{clicked:,}")
    c.metric("Did Not Click", f"{n-clicked:,}")
    d.metric("Click Rate", f"{clicked/n:.1%}")
    st.markdown("### Model performance")
    a,b,c,d = st.columns(4)
    a.metric("Accuracy", f"{r['accuracy']:.2%}")
    b.metric("Precision", f"{r['precision']:.2%}")
    c.metric("Recall", f"{r['recall']:.2%}")
    d.metric("F1-score", f"{r['f1']:.2%}")
    left,right = st.columns(2)
    with left:
        fig,ax = plt.subplots()
        counts = df[target].value_counts().reindex([0,1], fill_value=0)
        ax.bar(["Not Clicked","Clicked"], counts.values)
        ax.set_ylabel("Users")
        st.pyplot(fig); plt.close(fig)
    with right:
        st.dataframe(df.head(10), use_container_width=True)

def explorer(df):
    st.subheader("Dataset Explorer")
    st.write(f"{df.shape[0]} rows × {df.shape[1]} columns")
    t1,t2,t3 = st.tabs(["Preview","Summary","Missing values"])
    with t1: st.dataframe(df, use_container_width=True)
    with t2: st.dataframe(df.describe(include="all").T, use_container_width=True)
    with t3: st.dataframe(df.isna().sum().rename("Missing Values").to_frame(), use_container_width=True)

def visualizations(df, features, target):
    st.subheader("Exploratory Data Analysis")
    t1,t2,t3,t4 = st.tabs(["Age Distribution","Income vs Age","Internet Usage","Feature Relationships"])
    with t1:
        fig,ax = plt.subplots(); sns.histplot(data=df,x="Age",bins=25,kde=True,ax=ax)
        ax.set_title("Age Distribution"); st.pyplot(fig); plt.close(fig)
    with t2:
        fig,ax = plt.subplots(); sns.scatterplot(data=df,x="Age",y="Area Income",hue=target,palette="Set1",ax=ax)
        ax.set_title("Area Income vs Age"); st.pyplot(fig); plt.close(fig)
    with t3:
        fig,ax = plt.subplots(); sns.scatterplot(data=df,x="Daily Time Spent on Site",y="Daily Internet Usage",hue=target,palette="Set1",ax=ax)
        ax.set_title("Daily Time Spent vs Internet Usage"); st.pyplot(fig); plt.close(fig)
    with t4:
        grid = sns.pairplot(df[features+[target]],hue=target,corner=True,diag_kind="hist")
        st.pyplot(grid.fig); plt.close(grid.fig)

def performance(r):
    st.subheader("Logistic Regression Model Evaluation")
    a,b,c,d = st.columns(4)
    a.metric("Accuracy",f"{r['accuracy']:.3f}")
    b.metric("Precision",f"{r['precision']:.3f}")
    c.metric("Recall",f"{r['recall']:.3f}")
    d.metric("F1-score",f"{r['f1']:.3f}")
    left,right = st.columns(2)
    with left:
        fig,ax = plt.subplots()
        sns.heatmap(r["confusion"],annot=True,fmt="d",cmap="Reds",
                    xticklabels=["Not Clicked","Clicked"],yticklabels=["Not Clicked","Clicked"],ax=ax)
        ax.set_xlabel("Predicted"); ax.set_ylabel("Actual")
        st.pyplot(fig); plt.close(fig)
    with right:
        if r["roc"] is not None:
            fpr,tpr,_ = r["roc"]
            fig,ax = plt.subplots(); ax.plot(fpr,tpr,label=f"AUC = {r['auc']:.3f}")
            ax.plot([0,1],[0,1],"--"); ax.set_xlabel("False Positive Rate"); ax.set_ylabel("True Positive Rate")
            ax.legend(); st.pyplot(fig); plt.close(fig)
            st.metric("ROC-AUC",f"{r['auc']:.3f}")
        else: st.warning("ROC curve requires both classes in the test set.")
    st.markdown("#### Classification Report")
    st.code(r["report"])
    table = pd.DataFrame({"Actual":r["y_test"].values,"Predicted":r["predictions"],"Probability of Click":r["probabilities"]})
    st.dataframe(table.head(30),use_container_width=True)
    st.download_button("Download test predictions as CSV",table.to_csv(index=False).encode("utf-8"),
                       "ad_click_test_predictions.csv","text/csv")

def prediction(r, features):
    st.subheader("Predict Advertisement Click")
    with st.form("prediction_form"):
        c1,c2 = st.columns(2)
        with c1:
            time_spent = st.number_input("Daily Time Spent on Site",min_value=0.0,value=60.0)
            age = st.number_input("Age",min_value=1,max_value=120,value=35)
            income = st.number_input("Area Income",min_value=0.0,value=50000.0)
        with c2:
            usage = st.number_input("Daily Internet Usage",min_value=0.0,value=180.0)
            male = st.selectbox("Male",[0,1],format_func=lambda x:"No (0)" if x==0 else "Yes (1)")
        submitted = st.form_submit_button("Predict Click")
    if submitted:
        person = pd.DataFrame([{"Daily Time Spent on Site":time_spent,"Age":age,"Area Income":income,
                                "Daily Internet Usage":usage,"Male":male}],columns=features)
        predicted = int(r["model"].predict(person)[0])
        probability = float(r["model"].predict_proba(person)[0][1])
        if predicted == 1: st.success("The user is likely to click the advertisement.")
        else: st.info("The user is unlikely to click the advertisement.")
        st.metric("Estimated probability of clicking",f"{probability:.1%}")
        st.progress(probability)

def about(features, target):
    st.subheader("About the Project")
    st.markdown("""
    **Project:** Online Advertisement Click Prediction using Logistic Regression

    **Problem:** Predict whether a user clicks an online advertisement using selected demographic and internet-usage information.

    **Algorithm:** Logistic Regression, a supervised binary-classification algorithm.

    **Evaluation:** Accuracy, precision, recall, F1-score, confusion matrix and ROC curve.

    The dashboard calculates evaluation scores from the uploaded CSV; it does not hard-code results.
    """)
    st.markdown("#### Selected input features")
    st.write(", ".join(features))
    st.markdown("#### Required CSV columns")
    st.code("\\n".join(features+[target]))
