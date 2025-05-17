from sklearn.metrics import classification_report, roc_auc_score

def evaluate_classifier(X_train, y_train, X_test, y_test, model, target_names=['Not Churn', 'Churn']):
    """
    Trains and evaluates a classifier, printing the classification report and AUC-ROC.
    The target names are set to 'Not Churn' and 'Churn' by default.

    Args:
        X_train: Training data (features).
        y_train: Training labels.
        X_test: Test data (features).
        y_test: Test labels.
        model: Classifier (required).
        target_names: List of target names (optional). Defaults to ['Not Churn', 'Churn'].
    """

    model.fit(X_train, y_train)

    # Evaluation on the training set
    y_train_pred = model.predict(X_train)
    y_train_proba = model.predict_proba(X_train)[:, 1]
    auc_roc_train = roc_auc_score(y_train, y_train_proba)

    print("----- Training Set -----")
    print(classification_report(y_train, y_train_pred, target_names=target_names))
    print(f"AUC-ROC (Train): {auc_roc_train}")

    # Evaluation on the test set
    y_test_pred = model.predict(X_test)
    y_test_proba = model.predict_proba(X_test)[:, 1]
    auc_roc_test = roc_auc_score(y_test, y_test_proba)

    print("\n\n----- Test Set -----")
    print(classification_report(y_test, y_test_pred, target_names=target_names))
    print(f"AUC-ROC (Test): {auc_roc_test}")