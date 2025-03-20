import streamlit as st


def calculate_damage(base_damage, amplifiers, misc_percentage=0):
    """Calculate total damage after applying amplification sources."""
    # Start with base damage
    total_damage = base_damage

    # Apply each amplifier sequentially
    for name, percentage in amplifiers.items():
        if st.session_state.get(name, False):
            total_damage += total_damage * (percentage / 100)

    # Apply miscellaneous percentage increase if provided
    if misc_percentage > 0:
        total_damage += total_damage * (misc_percentage / 100)

    return total_damage


# App title and description
st.title("Amplificationator")

# Input for base damage
base_damage = st.number_input(
    "Enter base damage:",
    min_value=0,
    value=300,
    step=10
)

# Checkboxes for amplification sources
st.subheader("Damage Amplification Sources")
col1, col2 = st.columns(2)

with col1:
    st.checkbox("Axiom Arcanist (12%)", key="Axiom Arcanist")
    st.checkbox("Liandry's Torment (6%)", key="Liandry's Torment")

with col2:
    st.checkbox("Riftmaker (8%)", key="Riftmaker")
    st.checkbox("Spear of Shojin (12%)", key="Spear of Shojin")

# Optional miscellaneous percentage increase
misc_percentage = st.number_input(
    "Miscellaneous damage increase (%):",
    min_value=0,
    value=0,
    step=1
)

# Amplifier definitions
amplifiers = {
    "Axiom Arcanist": 12,
    "Liandry's Torment": 6,
    "Riftmaker": 8,
    "Spear of Shojin": 12
}

# Calculate final damage
total_damage = calculate_damage(base_damage, amplifiers, misc_percentage)

# Display results
st.markdown("---")
st.subheader("Damage Calculation Results")

# Create two columns for the results
res_col1, res_col2 = st.columns([1, 1])

with res_col1:
    st.metric(
        "Base Damage",
        f"{base_damage:.1f}"
    )

with res_col2:
    st.metric(
        "Final Damage",
        f"{total_damage:.1f}",
        delta=f"{total_damage - base_damage:.1f}"
    )