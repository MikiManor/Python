import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import statsmodels as sm
import sklearn as skl
import sklearn.preprocessing as preprocessing
import sklearn.linear_model as linear_model
import sklearn.cross_validation as cross_validation
import sklearn.metrics as metrics
import sklearn.tree as tree
import seaborn as sns



def plot_Distributor_Of_Each_Column(data):
    fig = plt.figure(figsize=(20,15))
    cols = 5
    rows = math.ceil(float(data.shape[1]) / cols)
    for i, column in enumerate(data.columns):
        ax = fig.add_subplot(rows, cols, i + 1)
        ax.set_title(column)
        if data.dtypes[column] == np.object:
            data[column].value_counts().plot(kind="bar", axes=ax)
        else:
            data[column].hist(axes=ax)
            plt.xticks(rotation="vertical")

    plt.subplots_adjust(hspace=1.2, wspace=0.4)
    plt.show()


def get_Csv_Date(csvFileName):
    original_data = pd.read_csv("ModifiedData.csv", names=["Age", "Workclass", "fnlwgt", "Education-Num",
                                                           "Martial Status", "Occupation", "Relationship", "Race",
                                                           "Sex", "Capital Gain", "Capital Loss", "Hours per week", "Target"],
                                                            sep=r'\s*,\s*', engine='python', na_values="NaN")
    original_data.tail()
    return(original_data)

def encode_Categorical_Features_To_Numerical(dataSet):
    copiedData = dataSet.copy()
    encoders = {}
    for column in copiedData.columns:
        if copiedData.dtypes[column] == np.object:
            encoders[column] = preprocessing.LabelEncoder()
            copiedData[column] = encoders[column].fit_transform(copiedData[column])
    return copiedData, encoders


def split_Data_To_Test_And_Train_Sets(encoded_data):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(encoded_data[encoded_data.columns - ["Target"]],
                                                                         encoded_data["Target"], train_size=0.70)
    scaler = preprocessing.StandardScaler()
    X_train = pd.DataFrame(scaler.fit_transform(X_train.astype("f8")), columns=X_train.columns)
    X_test = scaler.transform(X_test.astype("f8"))
    return X_train, X_test, y_train, y_test


def plot_Heat_Map(encoded_date):
    correlation = encoded_data.corr()
    # Generate a mask for the upper triangle
    mask = np.zeros_like(correlation, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 10))
    sns.heatmap(correlation, mask=mask, cmap=cmap, vmax=.3, center=0, square=True,
                linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()

def logical_Regression(X_train, X_test, y_train, y_test):
    cls = linear_model.LogisticRegression()
    cls.fit(X_train, y_train)
    y_pred = cls.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(12, 9))
    coefs = pd.Series(cls.coef_[0], index=X_train.columns)
    coefs.sort()
    coefs.plot(kind="bar")
    plt.subplots_adjust(bottom = 0.2)
    plt.show()

if __name__ == "__main__":
    csvFileName = "ModifiedData.csv"
    manipulatedFile = get_Csv_Date(csvFileName)
    # Plot Distributor Per Column
    plot_Distributor_Of_Each_Column(manipulatedFile)
    encoded_data, encoders = encode_Categorical_Features_To_Numerical(manipulatedFile)
    plot_Heat_Map(encoded_data)
    plot_Distributor_Of_Each_Column(encoded_data)
    X_train, X_test, y_train, y_test = split_Data_To_Test_And_Train_Sets(encoded_data)
    logical_Regression(X_train, X_test, y_train, y_test)
