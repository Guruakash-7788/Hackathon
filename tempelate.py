import streamlit as st

# Create a dictionary with image names and paths
image_paths = {
    'Business Model Canvas':'WhatsApp Image 2024-04-07 at 1.25.16 AM.jpeg',
    'SWOT Analysis':'bdd1ccb7-bd7c-4531-be4a-c5ba72ebc2c1.jpeg',
    'Balance Sheet Template':'b6663760-b7c5-490f-9cc7-9f96ffb420d8.jpeg',
    'Income Statement':'96a109d4-88ba-4b62-9a2c-5c16d8a6ef39.jpeg',
    'Cash Flow Statement':'67d3439b-3ecc-4faa-ad72-5ed3db99918d.jpeg',
    'Sales Forecasting':'59b7d66d-7fbe-4541-a232-231f15d7892c.jpeg',
    'Project Proposal':'3ef794ec-da4a-4568-a072-94994bc3a85c.jpeg',
    'Meeting Agenda Tempelate':'cbe53a06-9c9c-4953-bf83-498ccb98a017.jpeg',
    'Training Plan':'209d2061-5743-4d16-95d3-17dfeae7eb1c.jpeg',
    'NDA':'332e6d5d-3adf-46f1-a690-41deeaa58bda.jpeg'
   
}

# Create a sidebar column
with st.sidebar:
    st.write("### Sidebar")
    st.write("Choose Your Template from the Dropdown below.")
    # Display the names of the images
    selected_image = st.selectbox("Select an image:", list(image_paths.keys()))

# Main content area
st.write("## TEMPLATES FOR BUSINESS")
st.write("Choose Your Template from the sidebar on the left.")

# Display the selected image in the main content area
if selected_image:
    st.write(f"### {selected_image}")
    st.image(image_paths[selected_image], use_column_width=True)





