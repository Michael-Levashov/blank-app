import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

df = pd.DataFrame(
    [
       {"Reagent": "Hypochlorite", "Quantity per m3 of brine (kg)": 0.4, "Price per kg": 0.4,  "Time (hours)": 0.4, "is used": False},
       {"Reagent": "Polyacrylamide",  "Quantity per m3 of brine (kg)": 0.4, "Price per kg": 0.4, "Time (hours)": 0.5, "is used": False},
       {"Reagent": "Polyphosphate",  "Quantity per m3 of brine (kg)": 0.4, "Price per kg": 0.4, "Time (hours)": 0.3, "is used": False},
   ]
)
with col1:
    st.title("XtraLit calculator")
    st.subheader("0. Brine Treatment Cost Calculator")
    edited_df = st.data_editor(df, hide_index=True, num_rows="dynamic")
with col2:
    st.write("0. Brine Treatment Cost Calculator")
    selected_reagents = edited_df[edited_df["is used"] == True]
    if not selected_reagents.empty:

         total_cost = (selected_reagents["Quantity per m3 of brine (kg)"] * selected_reagents["Price per kg"]).sum()
         total_time = selected_reagents["Time (hours)"].sum()
         st.write(f"**Total Cost:** ${total_cost:.2f}/m3")
         st.write(f"**Total Time:** {total_time:.2f} hours")
    else:
         st.warning("No need pretreatment!")

with col1:
    st.subheader("1. Sorption")
    selection = st.segmented_control( "Method", ["Column", "Batch", "Continuous batch"], selection_mode="single")
    number = st.number_input("Number of stages", value=1, step=1,min_value=1, max_value=3)
    brine= st.selectbox("Brine:",("GSL-N", "GSL-S", "P-19", "Leach"), )
    option = st.selectbox("Sorbent:",("TOE277", "Home TOE274", "TOE15"), )

    flow = st.slider("Flow (BV)", 5, 150, 25)
    capacity = st.slider("Capacity (mg/g)", 5, 20, 10)



with col2:
    st.write("1. Sorption")
    st.markdown(f"Brine: {brine} ")
    st.markdown(f"Your selected: {selection} with  {number} stages")












cap1 = pd.DataFrame(
    [
       {"Capacity 1": 88, "Capacity 2": 0.4,  "Capacity 3": 0.4},

   ]
)
st.dataframe(cap1)
st.write('Sorption time'+"8")
st.subheader("2. Washing")
