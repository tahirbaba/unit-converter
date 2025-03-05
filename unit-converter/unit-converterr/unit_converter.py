import streamlit as st  

def convert_units(value, unit_from, unit_to):
    # Conversion dictionary
    conversions = {
        # Length conversions
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "centimeters_meters": 0.01,
        "meters_centimeters": 100,
        "inches_centimeters": 2.54,
        "centimeters_inches": 0.393701,
        "feet_meters": 0.3048,
        "meters_feet": 3.28084,
        "miles_kilometers": 1.60934,
        "kilometers_miles": 0.621371,

        # Weight conversions
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "pounds_kilograms": 0.453592,
        "kilograms_pounds": 2.20462,
        "ounces_grams": 28.3495,
        "grams_ounces": 0.035274,

        # Volume conversions
        "liters_milliliters": 1000,
        "milliliters_liters": 0.001,
        "gallons_liters": 3.78541,
        "liters_gallons": 0.264172,
    }

    # Generating conversion key
    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion_factor = conversions[key]  # Corrected variable name
        return value * conversion_factor
    else:
        return "Invalid unit conversion"

# Streamlit UI
st.title("Unit Converter")

# User input
value = st.number_input("Enter the value to convert:", min_value=0.0, format="%.2f")

# Available units
units = [
    "meters", "kilometers", "centimeters", "inches", "feet", "miles",
    "grams", "kilograms", "pounds", "ounces",
    "liters", "milliliters", "gallons"
]

unit_from = st.selectbox("Convert from:", units)
unit_to = st.selectbox("Convert to:", units)

# Conversion button
if st.button("Convert"):
    if unit_from == unit_to:
        st.write("Please select different units for conversion.")
    else:
        result = convert_units(value, unit_from, unit_to)
        st.write(f"Converted value: {result}")
