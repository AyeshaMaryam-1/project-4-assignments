import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")
    st.title("⚖️ BMI Calculator")
    st.subheader("Calculate your Body Mass Index (BMI)")

    st.caption("👤 Enter your details below (height in **meters**, weight in **kilograms**)")

    # Input fields
    name = st.text_input("Enter your name:")
    height = st.number_input("Enter your height (in meters):", min_value=0.0, format="%.2f")
    weight = st.number_input("Enter your weight (in kilograms):", min_value=0.0, format="%.2f")

    # BMI Calculation
    if st.button("Calculate BMI"):
        if height > 0 and weight > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"{name}, your BMI is **{bmi}**")

            # Interpretation
            if bmi < 18.5:
                st.info("📉 You're underweight.")
            elif 18.5 <= bmi < 24.9:
                st.success("✅ You're in the normal range.")
            elif 25 <= bmi < 29.9:
                st.warning("⚠️ You're overweight.")
            else:
                st.error("🚨 You're obese.")
        else:
            st.error("Please enter valid height and weight greater than 0.")

    # BMI Reference Table
    st.markdown("---")
    st.markdown("### 💡 BMI Categories")
    st.markdown("""
    - **Underweight**: BMI < 18.5  
    - **Normal weight**: BMI between 18.5 and 24.9  
    - **Overweight**: BMI between 25 and 29.9  
    - **Obese**: BMI ≥ 30
    """)

if __name__ == "__main__":
    main()
