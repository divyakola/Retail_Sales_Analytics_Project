import numpy as np
import pandas as pd
import os


def load_data():

    df = pd.read_csv("data/retail_sales.csv")

    print("Original Dataset")
    print(df.head())

    return df


def clean_data(df):

    # Remove duplicate records
    df = df.drop_duplicates(subset=["order_id"])

    # Handle missing values
    df = df.dropna()

    # Convert date
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Calculate profit
    df["profit"] = df["revenue"] - df["cost"]

    # Calculate profit percentage
    df["profit_margin"] = np.where(
        df["revenue"] > 0,
        (df["profit"] / df["revenue"]) * 100,
        0
    )

    # Extract month
    df["month"] = df["order_date"].dt.month_name()

    return df


def sales_analysis(df):

    print("\nTotal Revenue:",
          df["revenue"].sum())

    print("\nTotal Profit:",
          df["profit"].sum())

    print("\nTotal Orders:",
          df["order_id"].nunique())

    print("\nTotal Quantity:",
          df["quantity"].sum())

    print("\nAverage Revenue:",
          df["revenue"].mean())

    print("\nAverage Profit:",
          df["profit"].mean())


def product_analysis(df):

    print("\nProduct Wise Sales")

    product_sales = df.groupby(
        "product"
    )["revenue"].sum()

    print(product_sales)

    print("\nTop Selling Product:")

    print(product_sales.idxmax())


def category_analysis(df):

    print("\nCategory Wise Sales")

    category_sales = df.groupby(
        "category"
    )["revenue"].sum()

    print(category_sales)


def city_analysis(df):

    print("\nCity Wise Sales")

    city_sales = df.groupby(
        "city"
    )["revenue"].sum()

    print(city_sales)


def monthly_analysis(df):

    print("\nMonthly Sales")

    monthly_sales = df.groupby(
        "month"
    )["revenue"].sum()

    print(monthly_sales)

    return monthly_sales
