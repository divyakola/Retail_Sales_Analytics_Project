import os

from src.analysis import (
    load_data,
    clean_data,
    sales_analysis,
    product_analysis,
    category_analysis,
    city_analysis,
    monthly_analysis
)

from src.visualizations import (
    monthly_sales_chart,
    product_sales_chart,
    category_sales_chart,
    profit_chart
)


# Create output directory
os.makedirs("outputs", exist_ok=True)


# Step 1: Load Dataset
df = load_data()


# Step 2: Clean Dataset
df = clean_data(df)


# Step 3: Sales Analysis
sales_analysis(df)


# Step 4: Product Analysis
product_analysis(df)


# Step 5: Category Analysis
category_analysis(df)


# Step 6: City Analysis
city_analysis(df)


# Step 7: Monthly Analysis
monthly_analysis(df)


# Step 8: Generate Visualizations
monthly_sales_chart(df)

product_sales_chart(df)

category_sales_chart(df)

profit_chart(df)


# Step 9: Save Cleaned Dataset
df.to_csv(
    "outputs/cleaned_sales_data.csv",
    index=False
)


print("\nRetail Sales Analytics Completed!")
