
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
from datetime import datetime

# Set Streamlit to use full-width layout
st.set_page_config(layout="wide")

# Streamlit Display
st.title("Retirement Cash Flow Analysis")
st.subheader("Monte Carlo Simulation")

# # Put the tabs inside a container with fixed height
# with st.container(height=360, border=None):
#     # Create tabs for different sections
#     tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Personal Details", "Investment and Savings", "Income and Expense", "Social Security", "Healthcare Costs", "Market Returns", "Downsize"])

#     # Tab 1: Personal Details
#     with tab1:
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             current_age = st.number_input("Current Age", value=50)
#             partner_current_age = st.number_input("Partner's Current Age", value=46)
#             life_expectancy = st.number_input("Life Expectancy", value=92)
#         with col2:
#             retirement_age = st.number_input("Retirement Age", value=60)
#             partner_retirement_age = st.number_input("Partner's Retirement Age", value=60)

#     # Tab 2: Investment and Savings
#     with tab2:
#         col1, col2 = st.columns(2)
#         with col1:
#             initial_savings = st.number_input("Current Savings", value=2000000, step=100000)
#         with col2:
#             st.write(" \n")  # Placeholder for any additional inputs if needed in the future
#             st.write(" \n")  # Placeholder for any additional inputs if needed in the future
#             st.write(" \n")  # Placeholder for any additional inputs if needed in the future
#             st.write(" \n")  # Placeholder for any additional inputs if needed in the future

#     # Tab 3: Income and Expense
#     with tab3:
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             earnings = st.number_input("Annual Earnings", value=200000, step=25000)
#             annual_expense = st.number_input("Annual Expense", value=8000 * 12, step=1000)
#             mortgage_payment = st.number_input("Yearly Mortgage", value=36000, step=1000)
#         with col2:
#             partner_earnings = st.number_input("Partner's Annual Earnings", value=50000, step=5000)
#             annual_expense_decrease = st.number_input("Annual Expense Decrease Rate (%)", value=1.0) / 100  # Convert to decimal
#             mortgage_years_remaining = st.number_input("Mortgage Years Remaining", value=15)
#         with col3:
#             inflation_mean = st.number_input("Inflation Mean (%)", value=2.5) / 100  # Convert to decimal
#             inflation_std = st.number_input("Inflation Std Dev (%)", value=1.0) / 100  # Convert to decimal
#             tax_rate = st.number_input("Tax Rate (%)", value=15.0, step=1.0) / 100  # Convert to decimal

#     # Tab 4: Social Security 
#     with tab4:
#         col1, col2 = st.columns(2)
#         with col1:
#             annual_social_security = st.number_input("Social Security", value=3000 * 12, step=1000)
#             withdrawal_start_age = st.number_input("Withdrawal Start Age (Self)", value=67)
#             cola_rate = st.number_input("COLA Rate (%)", value=1.50) / 100  # Convert to decimal
#         with col2:
#             partner_social_security = st.number_input("Partner's Social Security", value=1500 * 12, step=1000)
#             partner_withdrawal_start_age = st.number_input("Partner's Withdrawal Start Age", value=65)

#     # Tab 5: Healthcare Costs
#     with tab5:
#         col1, col2 = st.columns(2)
#         with col1:
#             self_healthcare_cost = st.number_input("Self Healthcare Cost (Annual)", value=6000, step=1000)
#             self_healthcare_start_age = st.number_input("Self Healthcare Start Age", value=retirement_age)
#         with col2:
#             partner_healthcare_cost = st.number_input("Partner Healthcare Cost (Annual)", value=6000, step=1000)
#             partner_healthcare_start_age = st.number_input("Partner Healthcare Start Age", value=partner_retirement_age)

#     # Tab 6: Market Returns
#     with tab6:
#         col1, col2 = st.columns(2)
#         with col1:
#             investment_mean = st.number_input("Investment Return Mean (%)", value=5.0, step=0.25) / 100  # Convert to decimal
#             simulations = st.number_input("Number of Simulations", value=1000, step=1000)
#         with col2:
#             investment_std = st.number_input("Investment Return Std Dev (%)", value=12.0, step=0.25) / 100  # Convert to decimal

#     # Tab 7: Downsize
#     with tab7:
#         col1, col2 = st.columns(2)
#         with col1:
#             years_until_downsize = st.number_input("After how many years", value=0)
#         with col2:
#             residual_amount = st.number_input("Residual Amount", value=0, step=100000)



# Put the tabs inside a container with fixed height
with st.container(height=360, border=None):
    # Create tabs for different sections
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Personal Details", "Investment and Savings", "Income and Expense", "Social Security", "Healthcare Costs", "Market Returns", "Downsize"])

    # Tab 1: Personal Details
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            current_age = st.number_input("Current Age", value=50)
            partner_current_age = st.number_input("Partner's Current Age", value=46)
            life_expectancy = st.number_input("Life Expectancy", value=92)
        with col2:
            retirement_age = st.number_input("Retirement Age", value=60)
            partner_retirement_age = st.number_input("Partner's Retirement Age", value=60)

    # Tab 2: Investment and Savings
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            initial_savings = st.number_input("Current Savings", value=2000000, step=100000)
            stock_percentage = st.slider("Percentage of Stock Investment (%)", min_value=0, max_value=100, value=60)
            bond_percentage = 100 - stock_percentage  # Calculate bond percentage
        with col2:
            st.write(" \n")  # Placeholder for any additional inputs if needed in the future
            st.write(" \n")  # Placeholder for any additional inputs if needed in the future
            st.write(" \n")  # Placeholder for any additional inputs if needed in the future
            st.write(" \n")  # Placeholder for any additional inputs if needed in the future

    # Tab 3: Income and Expense
    with tab3:
        col1, col2, col3 = st.columns(3)
        with col1:
            earnings = st.number_input("Annual Earnings", value=200000, step=25000)
            annual_expense = st.number_input("Annual Expense", value=8000 * 12, step=1000)
            mortgage_payment = st.number_input("Yearly Mortgage", value=36000, step=1000)
        with col2:
            partner_earnings = st.number_input("Partner's Annual Earnings", value=50000, step=5000)
            annual_expense_decrease = st.number_input("Annual Expense Decrease Rate (%)", value=1.0) / 100  # Convert to decimal
            mortgage_years_remaining = st.number_input("Mortgage Years Remaining", value=15)
        with col3:
            inflation_mean = st.number_input("Inflation Mean (%)", value=2.5) / 100  # Convert to decimal
            inflation_std = st.number_input("Inflation Std Dev (%)", value=1.0) / 100  # Convert to decimal
            tax_rate = st.number_input("Tax Rate (%)", value=15.0, step=1.0) / 100  # Convert to decimal

    # Tab 4: Social Security 
    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            annual_social_security = st.number_input("Social Security", value=3000 * 12, step=1000)
            withdrawal_start_age = st.number_input("Withdrawal Start Age (Self)", value=67)
            cola_rate = st.number_input("COLA Rate (%)", value=1.50) / 100  # Convert to decimal
        with col2:
            partner_social_security = st.number_input("Partner's Social Security", value=1500 * 12, step=1000)
            partner_withdrawal_start_age = st.number_input("Partner's Withdrawal Start Age", value=65)

    # Tab 5: Healthcare Costs
    with tab5:
        col1, col2 = st.columns(2)
        with col1:
            self_healthcare_cost = st.number_input("Self Healthcare Cost (Annual)", value=6000, step=1000)
            self_healthcare_start_age = st.number_input("Self Healthcare Start Age", value=retirement_age)
        with col2:
            partner_healthcare_cost = st.number_input("Partner Healthcare Cost (Annual)", value=6000, step=1000)
            partner_healthcare_start_age = st.number_input("Partner Healthcare Start Age", value=partner_retirement_age)

    # Tab 6: Market Returns
    with tab6:
        col1, col2 = st.columns(2)
        with col1:
            stock_return_mean = st.number_input("Stock Return Mean (%)", value=7.0, step=0.25) / 100  # Convert to decimal
            stock_return_std = st.number_input("Stock Return Std Dev (%)", value=15.0, step=0.25) / 100  # Convert to decimal
            simulations = st.number_input("Number of Simulations", value=1000, step=1000)
        with col2:
            bond_return_mean = st.number_input("Bond Return Mean (%)", value=3.0, step=0.25) / 100  # Convert to decimal
            bond_return_std = st.number_input("Bond Return Std Dev (%)", value=5.0, step=0.25) / 100  # Convert to decimal

    # Tab 7: Downsize
    with tab7:
        col1, col2 = st.columns(2)
        with col1:
            years_until_downsize = st.number_input("After how many years", value=0)
        with col2:
            residual_amount = st.number_input("Residual Amount", value=0, step=100000)


# Calculate earning years
earning_years = retirement_age - current_age
partner_earning_years = partner_retirement_age - partner_current_age

# Get the current year
current_year = datetime.now().year

# Monte Carlo Simulation
def monte_carlo_simulation():
    years_in_simulation = life_expectancy - current_age
    success_count = 0
    failure_count = 0
    earliest_depletion_year = years_in_simulation  # Initialize to the maximum possible year

    aggregated_data = {year: {'Starting Savings': [], 'Annual Expense': [], 'Self Income': [], 'Partner Income': [],
                              'Investment Return': [], 'Tax': [], 'Self Social Security': [],
                              'Partner Social Security': [], 'Mortgage Payment': [], 'Ending Savings': [],
                              'Healthcare Costs': [], 'Downsize Proceeds': []}
                       for year in range(years_in_simulation)}

    all_simulations = []  # To store all simulation results
    depletion_years = []  # To track the year of depletion for each simulation

    for sim in range(simulations):
        savings = initial_savings
        annual_exp = annual_expense
        simulation_success = True  # Track if the simulation is successful

        effective_mortgage_years_remaining = mortgage_years_remaining

        # Annual copies of earnings for this simulation
        annual_earnings = earnings
        annual_partner_earnings = partner_earnings

        simulation_results = [0] * years_in_simulation  # Initialize with zeros

        for year in range(years_in_simulation):
            current_age_in_loop = current_age + year
            partner_current_age_in_loop = partner_current_age + year

            if year < effective_mortgage_years_remaining:
                mortgage = mortgage_payment
            else:
                mortgage = 0

            # Calculate healthcare costs
            healthcare_costs = 0
            if current_age_in_loop >= self_healthcare_start_age and current_age_in_loop < 65:
                healthcare_costs += self_healthcare_cost

            if current_age_in_loop >= self_healthcare_start_age and partner_current_age_in_loop < 65:
                healthcare_costs += partner_healthcare_cost

            annual_exp_with_mortgage = annual_exp + mortgage + healthcare_costs

            if current_age_in_loop > partner_retirement_age:
                annual_exp_with_mortgage *= (1 - annual_expense_decrease)

            # Initialize income
            self_income = annual_earnings * (1 - tax_rate) if current_age_in_loop < retirement_age else 0
            partner_income = annual_partner_earnings * (1 - tax_rate) if year < partner_earning_years else 0

            # Apply COLA to Social Security benefits based on withdrawal start ages
            self_ss = 0
            partner_ss = 0
            
            if current_age_in_loop >= withdrawal_start_age:  # Self Social Security start age
                self_ss = annual_social_security * (1 + cola_rate) ** (current_age_in_loop - withdrawal_start_age)  # Adjust for COLA
                self_income += self_ss
            
            if partner_current_age_in_loop >= partner_withdrawal_start_age:  # Partner's Social Security start age
                partner_ss = partner_social_security * (1 + cola_rate) ** (partner_current_age_in_loop - partner_withdrawal_start_age)  # Adjust for COLA
                partner_income += partner_ss

            net_cash_flow = self_income + partner_income - annual_exp_with_mortgage

            inflation_rate = np.random.normal(inflation_mean, inflation_std)
            annual_exp *= (1 + inflation_rate)

            # Adjust annual earnings for inflation
            annual_earnings *= (1 + inflation_rate)
            annual_partner_earnings *= (1 + inflation_rate)

            # # Investment growth (allowing for negative returns)
            # investment_return_rate = np.random.normal(investment_mean, investment_std)
            # investment_return = savings * investment_return_rate  # Can be negative

            # Calculate investment returns for stocks and bonds
            stock_investment = savings * (stock_percentage / 100)
            bond_investment = savings * (bond_percentage / 100)

            # Calculate returns for stocks and bonds
            stock_return_rate = np.random.normal(stock_return_mean, stock_return_std)
            bond_return_rate = np.random.normal(bond_return_mean, bond_return_std)

            stock_investment_return = stock_investment * stock_return_rate
            bond_investment_return = bond_investment * bond_return_rate

            # Total investment return
            investment_return = stock_investment_return + bond_investment_return

            if net_cash_flow <= 0:
                withdrawal = annual_exp_with_mortgage
                tax = withdrawal * tax_rate
            else:
                taxable_income = max(0, net_cash_flow)
                tax = taxable_income * tax_rate

            # Add residual amount to savings after specified years, if years_until_downsize > 0
            if years_until_downsize > 0 and year == years_until_downsize:
                savings += residual_amount
                aggregated_data[year]['Downsize Proceeds'].append(residual_amount)  # Store the residual amount
            elif years_until_downsize == 0:
                aggregated_data[year]['Downsize Proceeds'].append(0)  # No proceeds if downsizing is ignored

            #savings_end_of_year = (savings + net_cash_flow) * (1 + investment_return_rate)

            savings_end_of_year = savings + net_cash_flow + investment_return

            # Store values for each year
            aggregated_data[year]['Starting Savings'].append(savings)
            aggregated_data[year]['Annual Expense'].append(annual_exp_with_mortgage)
            aggregated_data[year]['Self Income'].append(self_income)
            aggregated_data[year]['Partner Income'].append(partner_income)
            aggregated_data[year]['Investment Return'].append(investment_return)
            aggregated_data[year]['Tax'].append(tax)
            aggregated_data[year]['Self Social Security'].append(self_ss)
            aggregated_data[year]['Partner Social Security'].append(partner_ss)
            aggregated_data[year]['Mortgage Payment'].append(mortgage)
            aggregated_data[year]['Healthcare Costs'].append(healthcare_costs)
            aggregated_data[year]['Ending Savings'].append(savings_end_of_year)

            savings = savings_end_of_year
            simulation_results[year] = savings_end_of_year  # Store the ending savings for this year

            # If savings drop below zero, fill in the remaining years with zeros
            if savings <= 0:
                simulation_success = False  # Mark this simulation as a failure
                earliest_depletion_year = min(earliest_depletion_year, year)  # Update earliest depletion year
                break  # Exit the loop if savings go below zero

        # Fill in remaining years with zeros if the simulation failed
        if not simulation_success:
            failure_count += 1
            for remaining_year in range(year + 1, years_in_simulation):
                simulation_results[remaining_year] = 0  # Fill with zero for remaining years

        all_simulations.append(simulation_results)  # Store the results of this simulation

        if simulation_success:
            success_count += 1  # Increment success count only if the simulation was successful

    success_rate = (success_count / simulations) * 100
    failure_rate = (failure_count / simulations) * 100

    avg_data = []
    for year, data in aggregated_data.items():
        downsize_proceeds = np.median(data['Downsize Proceeds']) if data['Downsize Proceeds'] else 0  # Check for empty data
        max_ending_savings = np.max(data['Ending Savings'])

        # Initialize min_depletion_simulation to handle cases where there are no successful simulations
        min_depletion_simulation = [0] * years_in_simulation  # Default to zeros

        # Find the specific simulation for the earliest depletion year
        depletion_years = []
        for sim in all_simulations:
            depletion_year = next((year for year, value in enumerate(sim) if value <= 0), years_in_simulation)
            depletion_years.append(depletion_year)

        if success_count > 0:  # Only proceed if there are successful simulations
            min_depletion_year_index = np.argmin(depletion_years)
            min_depletion_simulation = all_simulations[min_depletion_year_index]

        # Use the values from min_depletion_simulation for the Min Ending Savings
        if len(min_depletion_simulation) > year:
            min_ending_savings_value = min_depletion_simulation[year]  # Get the value from min_depletion_simulation
        else:
            min_ending_savings_value = 0  # Default to 0 if the year exceeds the simulation length

        avg_data.append({
            'Year': current_year + year,
            'Age': current_age + year,
            'Partner Age': partner_current_age + year,
            'Starting Savings ($)': "{:,}".format(int(np.median(data['Starting Savings']))),
            'Annual Expense ($)': "{:,}".format(int(np.median(data['Annual Expense']))),
            'Self Income ($)': "{:,}".format(int(np.median(data['Self Income']))),
            'Partner Income ($)': "{:,}".format(int(np.median(data['Partner Income']))),
            'Self Social Security ($)': "{:,}".format(int(np.median(data['Self Social Security']))),
            'Partner Social Security ($)': "{:,}".format(int(np.median(data['Partner Social Security']))),
            'Mortgage Payment ($)': "{:,}".format(int(np.median(data['Mortgage Payment']))),
            'Healthcare Costs ($)': "{:,}".format(int(np.median(data['Healthcare Costs']))),
            'Investment Return ($)': "{:,}".format(int(np.median(data['Investment Return']))),
            'Tax ($)': "{:,}".format(int(np.median(data['Tax']))),
            'Ending Savings ($)': "{:,}".format(int(np.median(data['Ending Savings']))),
            'Downsize Proceeds ($)': "{:,}".format(int(downsize_proceeds)),  # Added Downsize Proceeds
            'Min Ending Savings ($)': "{:,}".format(int(min_ending_savings_value)),  # Use min_depletion_simulation values
            'Max Ending Savings ($)': "{:,}".format(int(max_ending_savings)),  # Maximum Ending Savings
        })

    df_avg_cashflow = pd.DataFrame(avg_data)

    return df_avg_cashflow, success_rate, failure_rate, all_simulations, min_depletion_simulation, earliest_depletion_year

# Run the simulation
df_avg_cashflow, success_rate, failure_rate, all_simulations, min_depletion_simulation, earliest_depletion_year = monte_carlo_simulation()

# Calculate the age at earliest depletion
age_at_earliest_depletion = current_age + earliest_depletion_year


# Display success and failure rates
st.write("# Simulation Results")

# Create a single row for both metrics with CSS margin for spacing
st.markdown(f"<p style='font-size: 36px; color: green; display: inline; margin-right: 50px;'>Success Rate: {success_rate:.0f}%</p>"
            f"<p style='font-size: 36px; color: red; display: inline;margin-right: 50px;'>Failure Rate: {failure_rate:.0f}%</p>"
            f"<p style='font-size: 36px; color: black; display: inline;'>Year of Depletion: {current_year + earliest_depletion_year} (Age: {age_at_earliest_depletion})</p><br><br>", unsafe_allow_html=True)

# Display the DataFrame
st.write("### Yearly Cash Flow Summary")
st.markdown(df_avg_cashflow.to_html(index=False, escape=False), unsafe_allow_html=True)

# Plotting the results
years = df_avg_cashflow['Year']
median_ending_savings = df_avg_cashflow['Ending Savings ($)'].str.replace(',', '').astype(float)
min_ending_savings = df_avg_cashflow['Min Ending Savings ($)'].str.replace(',', '').astype(float)
max_ending_savings = df_avg_cashflow['Max Ending Savings ($)'].str.replace(',', '').astype(float)

plt.figure(figsize=(12, 6))
plt.plot(years, median_ending_savings, label='Median Ending Savings', color='blue', linewidth=2)
plt.fill_between(years, min_ending_savings, max_ending_savings, color='lightblue', alpha=0.5, label='Savings Range')
plt.grid(False)
plt.title('Retirement Ending Savings Over Time')
plt.xlabel('Year')
plt.ylabel('Ending Savings ($)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot in Streamlit
st.pyplot(plt)

# Plotting individual simulations
plt.figure(figsize=(12, 6))
for sim in all_simulations:
    plt.plot(years, sim, color='gray', alpha=0.1)  # Plot each simulation with light color

plt.title('Individual Simulation Results')
plt.xlabel('Year')
plt.ylabel('Ending Savings ($)')
plt.grid(False)
plt.tight_layout()

# Show the individual simulations plot in Streamlit
st.pyplot(plt)


# Prepare data for Altair visualization
years = df_avg_cashflow['Year']
median_ending_savings = df_avg_cashflow['Ending Savings ($)'].str.replace(',', '').astype(float)
min_ending_savings = df_avg_cashflow['Min Ending Savings ($)'].str.replace(',', '').astype(float)
max_ending_savings = df_avg_cashflow['Max Ending Savings ($)'].str.replace(',', '').astype(float)

# Create Altair chart for median ending savings
median_chart = alt.Chart(df_avg_cashflow).mark_line(color='blue').encode(
    x='Year:O',
    y='Ending Savings ($):Q',
    tooltip=['Year', 'Ending Savings ($)']
).properties(
    title='Median Ending Savings Over Time'
)

# Create Altair chart for savings range
range_chart = alt.Chart(df_avg_cashflow).mark_area(opacity=0.5, color='lightblue').encode(
    x='Year:O',
    y='Min Ending Savings ($):Q',
    y2='Max Ending Savings ($):Q'
).properties(
    title='Savings Range Over Time'
)

# Combine the charts
combined_chart = (range_chart + median_chart).properties(width=600, height=400)

# Show the combined chart in Streamlit
st.altair_chart(combined_chart, use_container_width=True)

# Plotting individual simulations using Altair
simulation_data = pd.DataFrame(all_simulations).T
simulation_data.columns = [f'Simulation {i+1}' for i in range(simulations)]
simulation_data['Year'] = years

# Melt the DataFrame for Altair
melted_simulation_data = simulation_data.melt(id_vars='Year', var_name='Simulation', value_name='Ending Savings ($)')

# Create Altair chart for individual simulations
individual_simulation_chart = alt.Chart(melted_simulation_data).mark_line(color='gray', opacity=0.1).encode(
    x='Year:O',
    y='Ending Savings ($):Q',
    tooltip=['Year', 'Simulation', 'Ending Savings ($)']
).properties(
    title='Individual Simulation Results'
)

# Show the individual simulations plot in Streamlit
st.altair_chart(individual_simulation_chart, use_container_width=True)