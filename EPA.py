# Imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class EPAnalysis:
    """
    In this class functions to perform EPA are stored.

    """

    def __init__(self, df, numerical_columns, player_list):
        self.df = df
        self.numerical_columns = numerical_columns
        self.player_list = player_list

    def first_insights(self):
        """

        :return: First five rows and information of each column.
        """
        print(f"First five rows:\n{self.df.head()}")
        print(f"Information of each column:\n{self.df.info()}")

    def most_players(self):
        """

        :return: Pandas DataFrame with number occurrences for each player.
        """
        most_df = pd.DataFrame(self.df['Name'].value_counts())
        print(f"Players sorted according to their number of occurrences:\n{most_df}")

    def histogram(self):
        """

        :return: Histogram of each numerical column.
        """
        self.df[self.numerical_columns].hist(bins=15, figsize=(15, 4))

    def rates_year(self):
        """

        :return: Line plots with the development of each player rating.
        """
        for player in self.player_list:
            df_player = self.df.loc[self.df['Name'] == player]
            sns.lineplot(data=df_player, x="year", y="rates")
        plt.show()

    def scatter_plot(self):
        """

        :return: Scatter-plot for each player and each numerical column.
        """
        for player in self.player_list:
            df_player = self.df.loc[self.df['Name'] == player]
            for column in self.numerical_columns:
                sns.scatterplot(data=df_player, x=column, y="rates")
                plt.title(f"Rates per {column} for player {player}")
                plt.show()
        plt.show()

    def heatmap(self):
        """

        :return: Heatmap with correlation values is returned.
        """
        sns.heatmap(self.df[self.numerical_columns].corr(), annot=True)

    def heatmap_rating(self):
        """

        :return: Correlation values only for rates as dependent variable in form of a heatmap.
        """
        sns.heatmap(self.df[self.numerical_columns].corr()[['rates']].sort_values(by="rates", ascending=False),
                    annot=True)
