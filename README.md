Day 7 - Custom Flower Analysis with Pandas

Project Overview
This project marks the transition from basic scripting to Exploratory Data Analysis (EDA). Instead of using built-in datasets, I have designed a custom dataset containing features of various flowers (Rose, Sunflower, Lotus) to practice data manipulation and visualization using Pandas and Matplotlib.

Key Learnings & Implementation
Data Structuring: Created a dictionary-based dataset and converted it into a Pandas DataFrame.

Descriptive Analytics: Used .describe(), .info(), and .shape to understand the data's statistical backbone.

Advanced Filtering: * Filtered data based on specific categories (e.g., "Only Rose").

Applied conditional logic (e.g., "Price > 50").

Feature Engineering: Added a new calculated column price_per_cm by performing vectorized operations on existing columns.

Data Aggregation: Grouped data by 'name' to find the mean price of each flower species using .groupby().

Automated Insights: Used .idxmax() to programmatically identify the most expensive flower in the list.

Visualizations
The code generates a dual-plot figure (day7_results.png) to provide visual insights:

Bar Chart: Displays the Average Price per flower species.

Scatter Plot: Analyzes the relationship between Petal Length and Price for each flower type.

Libraries Used
Pandas: For data manipulation and analysis.

Matplotlib: For creating static, animated, and interactive visualizations.
