import streamlit as st


def main():

#######################
# Page configuration
    st.set_page_config(
        page_title="Should I buy an electric car?",
        page_icon="🏂",
        layout="wide")

    st.title("Should I buy an electric car?")
    

# Gather inputs
    

    col_width_ratio = [0.3, 0.3, 0.3]

    row1 = st.columns([1/3, 2/3])
    row2 = st.columns([1/3, 2/9, 2/9, 2/9])
    row3 = st.columns(col_width_ratio)
    row4 = st.columns(col_width_ratio)
  
    gas_price_cont = row1[0].container(height=110)
    elec_price_cont = row2[0].container(height=110)
    gas_efficiency_cont = row3[0].container(height=110)
    elec_efficiency_cont = row4[0].container(height=110)

    with gas_price_cont:
        gas_price = st.number_input('Gas price (€/L):', value=1.83, step=0.01)
    with elec_price_cont:
        elec_price = st.number_input('Electricity price (€/kWh):', value=0.11, step=0.01) / 100
    with gas_efficiency_cont:
        gas_efficiency = st.number_input('Gas efficiency (L/100km):', value=7.0, step=0.5) / 100
    with elec_efficiency_cont:
        elec_efficiency = st.number_input('Electric efficiency (kWh/100km):', value=10.0, step=0.5)


    distance_cont = row1[1].container(height=110)
    with distance_cont:
        distance = st.number_input('Trip length (km):', value=100.0, step=1.0)

############################


    # Calculate costs
    gas_car_cost = gas_price * gas_efficiency * distance
    elec_car_cost = elec_price * elec_efficiency * distance
    delta = (elec_car_cost - gas_car_cost) / gas_car_cost


    gas_cost_cont = row2[1].container(height=110)
    elec_cost_cont = row2[2].container(height=110)
    delta_cont = row2[3].container(height=110)

    with gas_cost_cont:
        st.metric("Gasoline car cost (€)", round(gas_car_cost, 2))
    with elec_cost_cont:
        st.metric("Electric car cost (€)", round(elec_car_cost, 2))
    with delta_cont:
        st.metric("Delta", str(round(delta * 100)) + "%")




if __name__ == '__main__':
    main()
