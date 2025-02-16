 
import streamlit as st
import pandas as pd

def business_setup_calculator():
    st.title("Business Setup Cost Calculator")

    cost_components = {
        "Trade Name Reservation": {"Estimated Time": "1-2 working days", "Fee (SAR)": 0},
        "MISA Investment License": {"Estimated Time": "3-5 working days", "Fee (SAR)": 2000},
        "MISA First-Year Service Fee": {"Estimated Time": "Same day", "Fee (SAR)": 10000},
        "MISA Renewal Fee": {"Estimated Time": "Annually", "Fee (SAR)": 60000},
        "Commercial Registration (CR)": {"Estimated Time": "2-3 working days", "Fee (SAR)": 1200},
        "Chamber of Commerce Registration": {"Estimated Time": "Immediate", "Fee (SAR)": 3000},
        "Iqama & Work Permit Fees": {"Estimated Time": "1-2 weeks", "Fee (SAR)": 9000},
        "Municipality License": {"Estimated Time": "Varies", "Fee (SAR)": 5000},
        "Corporate Bank Account Opening": {"Estimated Time": "1-2 weeks", "Fee (SAR)": 0},
    }

    cost_df = pd.DataFrame(cost_components).T
    cost_df.reset_index(inplace=True)
    cost_df.rename(columns={"index": "Service"}, inplace=True)

    st.write("### Available Business Setup Services and Costs")
    st.dataframe(cost_df)

    selected_services = st.multiselect(
        "Select the services required for business setup:", cost_df["Service"].tolist()
    )

    if selected_services:
        selected_df = cost_df[cost_df["Service"].isin(selected_services)]
        total_cost = selected_df["Fee (SAR)"].sum()

        st.write("### Selected Services & Costs")
        st.dataframe(selected_df)
        st.write(f"## 💰 Estimated Total Setup Cost: SAR {total_cost}")

if __name__ == "__main__":
    business_setup_calculator()
