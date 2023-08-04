# python-slider-allocation-budgeting-tool
Budget Forecast App

This application calculates and forecasts budget based on transaction data for various categories. Offering a better understanding and macro perspective of which months certain categories are higher/lower to better prepare/budget. It takes transaction data as input, calculates the monthly totals, and produces an HTML report that includes an overview of the total amounts spent per category, and a detailed monthly breakdown. It differentiation from a pivot table is that it offers an interactive slider bar to allocate money based on the set amount of your actual budget, or a custom amount for each category/month within that category.

<img width="1083" alt="Screenshot 2023-08-01 at 11 12 07 AM" src="https://github.com/Ben-Hatton-1/python-slider-allocation-budgeting-tool/assets/126031725/086f328c-1ba6-46c5-bdaf-f51a8c7f89c5">

Features:
- Monthly totals calculation: The application calculates the monthly totals for each category.
- Next year's budget: The application predicts the next year's budget based on the total amount spent in the previous year.
- Interactive HTML report: The application generates an interactive HTML report with the following features:
- Slider bars: Each category and month has a slider bar that represents the budget allocated to that month. The slider bars can be adjusted to allocate more or less budget to each month.
- Fixed Budget: In this mode, the sum of the budgets for all months cannot exceed the next year's budget for the category. Adjusting the budget for one month will automatically adjust the budgets for the other months to maintain the total budget.
- Custom Budget: In this mode, the budgets for each month can be adjusted independently up to the maximum budget for the category.
- Lock/Unlock: Each month's budget can be locked to prevent it from being adjusted automatically when other budgets are adjusted.

How to Use:
Prepare your transaction data in Excel format. (A. "Date" B. "Desciption" C. "Amount" D. "Category")
Run the Python script. It will read the transaction data, calculate the monthly totals, and generate the HTML report.
Open the generated budget_forecast_report.html file in a web browser to view the report and adjust the budgets as needed.

Dependencies:
This application requires the following Python packages:

pandas
jinja2
These can be installed with pip:

bash
pip install pandas jinja2

Notes
This application is for budgeting purposes only. It does not connect to any bank accounts or automatically track transactions. All transaction data must be manually entered into the Excel file locally.
