import matplotlib.pyplot as plt


def monthly_sales_chart(df):

    monthly_sales = df.groupby(
        "month"
    )["revenue"].sum()

    plt.figure(figsize=(10, 5))

    plt.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o"
    )

    plt.title("Monthly Sales Analysis")

    plt.xlabel("Month")

    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("outputs/monthly_sales.png")

    plt.show()


def product_sales_chart(df):

    product_sales = df.groupby(
        "product"
    )["revenue"].sum()

    plt.figure(figsize=(10, 5))

    plt.bar(
        product_sales.index,
        product_sales.values
    )

    plt.title("Product Wise Sales")

    plt.xlabel("Product")

    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("outputs/product_sales.png")

    plt.show()


def category_sales_chart(df):

    category_sales = df.groupby(
        "category"
    )["revenue"].sum()

    plt.figure(figsize=(7, 7))

    plt.pie(
        category_sales.values,
        labels=category_sales.index,
        autopct="%1.1f%%"
    )

    plt.title("Category Wise Sales")

    plt.savefig("outputs/category_sales.png")

    plt.show()


def profit_chart(df):

    plt.figure(figsize=(10, 5))

    plt.scatter(
        df["quantity"],
        df["profit"]
    )

    plt.title("Quantity vs Profit")

    plt.xlabel("Quantity")

    plt.ylabel("Profit")

    plt.savefig("outputs/profit_analysis.png")

    plt.show()
