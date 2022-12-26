# Imports

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import HuberRegressor


def linearregression(df, X_columns, y_column, name):
    """

    :param df: DataFrame that is to be used for the model.
    :param X_columns: Name of feature columns.
    :param y_column: Name of target model.
    :param name: Name of the model. Is used for printing.
    :return: Evaluation, namely r2, mae and mse are returned.
    """
    X_train, X_test, y_train, y_test = train_test_split(df[X_columns], df[y_column], test_size=0.33, random_state=42)

    pipe = Pipeline([('scaler', StandardScaler()), ('reg', LinearRegression())])
    pipe.fit(X_train, y_train)
    prediction = pipe.predict(X_test)

    # Validation
    r2 = r2_score(y_test, prediction)
    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    print(f"{name}\nr2: {r2}\nmae: {mae}\nmse: {mse}\n---------------")


def randomforest(df, X_columns, y_column, name):
    """

    :param df: DataFrame that is to be used for the model.
    :param X_columns: Name of feature columns.
    :param y_column: Name of target model.
    :param name: Name of the model. Is used for the plots titles.
    :return: Plots for each evaluation parameter to find the right number for max_depth.
    """
    X_train, X_test, y_train, y_test = train_test_split(df[X_columns], df[y_column], test_size=0.33, random_state=42)

    r2_list = []
    mae_list = []
    mse_list = []
    length = []

    for i in range(1, 31):
        length.append(i)

        pipe = Pipeline([('scaler', StandardScaler()), ('clf', RandomForestRegressor(max_depth=i, random_state=0))])
        pipe.fit(X_train, y_train)
        prediction = pipe.predict(X_test)

        # Validation
        r2 = r2_score(y_test, prediction)
        mae = mean_absolute_error(y_test, prediction)
        mse = mean_squared_error(y_test, prediction)

        r2_list.append(r2)
        mae_list.append(mae)
        mse_list.append(mse)

    plt.plot(length, r2_list, label="r2")
    plt.title("r2: " + name)
    plt.show()
    plt.plot(length, mae_list, label="mae")
    plt.title("mae: " + name)
    plt.show()
    plt.plot(length, mse_list, label="mse")
    plt.title("mse: " + name)
    plt.show()


def huber_reg(df, X_columns, y_column, name):
    """

    :param df: DataFrame that is to be used for the model.
    :param X_columns: Name of feature columns.
    :param y_column: Name of target model.
    :param name: Name of the model. Is used for printing.
    :return: Evaluation, namely r2, mae and mse are returned.
    """
    X_train, X_test, y_train, y_test = train_test_split(df[X_columns], df[y_column], test_size=0.33, random_state=42)

    pipe = Pipeline([('scaler', StandardScaler()), ('huber', HuberRegressor())])
    pipe.fit(X_train, y_train)
    prediction = pipe.predict(X_test)

    # Validation
    r2 = r2_score(y_test, prediction)
    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)

    print(f"{name}\nr2: {r2}\nmae: {mae}\nmse: {mse}\n---------------")
