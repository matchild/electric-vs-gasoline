import streamlit as st


def main():
    st.title('Trip cost calculator')

#     # Input boxes for user to enter numbers
#     num1 = st.number_input('Enter first number:', value=0.0, step=1.0)
#     num2 = st.number_input('Enter second number:', value=0.0, step=1.0)

#     # Calculate the sum
#     result = num1 + num2

#     # Display the result
#     st.write('Sum:', result)


    
# Gather inputs
    

    col_width_ratio = [0.4, 0.6]

    row1 = st.columns(col_width_ratio)
    row2 = st.columns(col_width_ratio)
    row3 = st.columns(col_width_ratio)
    row4 = st.columns(col_width_ratio)
  
    gas_price_cont = row1[0].container(height=110)
    elec_price_cont = row2[0].container(height=110)
    gas_efficiency_cont = row3[0].container(height=110)
    elec_efficiency_cont = row4[0].container(height=110)

    with gas_price_cont:
        gas_price = st.number_input('Gas price (€/L):', value=1.83, step=0.01)
    with elec_price_cont:
        elec_price = st.number_input('Electricity price (€/kWh):', value=0.39, step=0.01)
    with gas_efficiency_cont:
        gas_efficiency = st.number_input('Gas efficiency (L/100km):', value=7.0, step=0.5)
    with elec_efficiency_cont:
        elc_efficiency = st.number_input('Electric efficiency (kWh/100km):', value=10.0, step=0.5)


    distance_cont = row1[1].container(height=110)
    with distance_cont:
        distance = st.number_input('Distance (km):', value=100.0, step=1.0)

############################


if __name__ == '__main__':
    main()
