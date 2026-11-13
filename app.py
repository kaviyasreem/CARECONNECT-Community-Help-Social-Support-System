
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="CARECONNECT",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ CARECONNECT")
st.subheader("Connecting People Through Kindness")

st.write(
    "A community support platform that connects "
    "people in need with volunteers and donors."
)

if "requests" not in st.session_state:
    st.session_state.requests = []

if "volunteers" not in st.session_state:
    st.session_state.volunteers = []

menu = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Request Help", "Become a Volunteer",
     "Community Requests", "Blood Donor", "About"]
)

if menu == "Home":

    st.header("Community Support Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Help Requests",
        len(st.session_state.requests)
    )

    col2.metric(
        "Registered Volunteers",
        len(st.session_state.volunteers)
    )

    col3.metric(
        "Platform Status",
        "Active"
    )

    st.success("Together, we can make a difference!")

    st.info(
        "CARECONNECT encourages people to support "
        "their communities through volunteering."
    )

elif menu == "Request Help":

    st.header("Submit a Help Request")

    name = st.text_input("Your Name")
    contact = st.text_input("Contact Number")

    category = st.selectbox(
        "Type of Help Needed",
        ["Food", "Education", "Medical Support",
         "Clothing", "Blood Donation", "Other"]
    )

    location = st.text_input("Your Location")

    description = st.text_area(
        "Describe Your Problem"
    )

    if st.button("Submit Request"):

        if name and contact and location and description:

            request = {
                "Name": name,
                "Contact": contact,
                "Category": category,
                "Location": location,
                "Description": description,
                "Date": datetime.now().strftime("%d-%m-%Y")
            }

            st.session_state.requests.append(request)

            st.success("Help request submitted successfully!")

        else:
            st.warning("Please fill all the fields.")

elif menu == "Become a Volunteer":

    st.header("Volunteer Registration")

    name = st.text_input("Volunteer Name")
    age = st.number_input("Age", min_value=18, max_value=100)
    phone = st.text_input("Mobile Number")

    skills = st.selectbox(
        "Area of Interest",
        ["Education", "Medical Support",
         "Food Distribution", "Community Service",
         "Blood Donation"]
    )

    location = st.text_input("City / Location")

    if st.button("Register as Volunteer"):

        if name and phone and location:

            volunteer = {
                "Name": name,
                "Age": age,
                "Phone": phone,
                "Interest": skills,
                "Location": location
            }

            st.session_state.volunteers.append(volunteer)

            st.success("Volunteer registered successfully!")

        else:
            st.warning("Please complete all details.")

elif menu == "Community Requests":

    st.header("Available Community Requests")

    if st.session_state.requests:

        df = pd.DataFrame(st.session_state.requests)

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Requests",
            csv,
            "community_requests.csv",
            "text/csv"
        )

    else:
        st.info("No community requests submitted yet.")

elif menu == "Blood Donor":

    st.header("Blood Donation Support")

    st.write(
        "Connect with potential blood donors "
        "through community support."
    )

    donor_name = st.text_input("Donor Name")
    blood_group = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    donor_location = st.text_input("Location")
    donor_contact = st.text_input("Contact Number")

    st.warning(
        "This is a demonstration system. "
        "Blood requests and donor details must be "
        "verified by authorized medical organizations."
    )

    if st.button("Register Donor"):

        if donor_name and donor_location and donor_contact:

            st.success("Donor details submitted successfully!")

        else:
            st.warning("Please fill all the details.")

elif menu == "About":

    st.header("About CARECONNECT")

    st.write("""
    CARECONNECT is a social impact mini project.

    Objectives:
    - Connect people who need help.
    - Encourage community volunteering.
    - Support blood donation awareness.
    - Improve access to community assistance.

    Technologies Used:
    - Python
    - Streamlit
    - Pandas

    Project Domain: Social Welfare and Community Support
    """)

st.divider()

st.caption(
    "CARECONNECT © 2026 | Building a Better Community"
)
