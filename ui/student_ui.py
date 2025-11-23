# student_ui.py

import streamlit as st
import requests
from typing import Optional

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Student Auth Demo", page_icon="🎓")


# Session state helpers

if "access_token" not in st.session_state:
    st.session_state.access_token = None

if "current_student" not in st.session_state:
    st.session_state.current_student = None

if "last_resources" not in st.session_state:
    st.session_state.last_resources = None


def set_token(token: Optional[str]):
    st.session_state.access_token = token


def get_headers():
    if st.session_state.access_token:
        return {"Authorization": f"Bearer {st.session_state.access_token}"}
    return {}



# UI layout

st.title("🎓 Student Profile System")

page = st.sidebar.radio("Navigate", ["Register", "Login", "My Profile"])

st.sidebar.markdown("---")
if st.session_state.access_token:
    st.sidebar.success("Logged in")
    if st.sidebar.button("Logout"):
        set_token(None)
        st.session_state.current_student = None
        st.session_state.last_resources = None
        st.sidebar.info("Logged out")
else:
    st.sidebar.info("Not logged in")


# Register page

if page == "Register":
    st.header("Register New Student")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if not name or not email or not password:
            st.warning("Please fill in all fields.")
        else:
            payload = {
                "name": name,
                "email": email,
                "password": password,
            }
            try:
                resp = requests.post(f"{API_BASE_URL}/register", json=payload)
                if resp.status_code in (200, 201):
                    data = resp.json()
                    st.success(f"Registered successfully! ID: {data['id']}")
                else:
                    try:
                        detail = resp.json().get("detail", resp.text)
                    except Exception:
                        detail = resp.text
                    st.error(f"Registration failed: {detail}")
            except requests.exceptions.ConnectionError:
                st.error("Cannot reach API. Is FastAPI running at 127.0.0.1:8000?")



# student Login page

elif page == "Login":
    st.header("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not email or not password:
            st.warning("Please enter email and password.")
        else:
            payload = {"email": email, "password": password}
            try:
                resp = requests.post(f"{API_BASE_URL}/login", json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    access_token = data["access_token"]
                    set_token(access_token)
                    st.success("Login successful! Token stored in session.")
                else:
                    try:
                        detail = resp.json().get("detail", resp.text)
                    except Exception:
                        detail = resp.text
                    st.error(f"Login failed: {detail}")
            except requests.exceptions.ConnectionError:
                st.error("Cannot reach API. Is FastAPI running at 127.0.0.1:8000?")



# My Profile page (/me + interests + resources)

elif page == "My Profile":
    st.header("My Profile")

    if not st.session_state.access_token:
        st.info("You must login first to see your profile.")
    else:
        # Load profile button
        if st.button("Load my profile"):
            try:
                resp = requests.get(f"{API_BASE_URL}/me", headers=get_headers())
                if resp.status_code == 200:
                    student = resp.json()
                    st.session_state.current_student = student
                else:
                    try:
                        detail = resp.json().get("detail", resp.text)
                    except Exception:
                        detail = resp.text
                    st.error(f"Failed to load profile: {detail}")
            except requests.exceptions.ConnectionError:
                st.error("Cannot reach API. Is FastAPI running at 127.0.0.1:8000?")

        student = st.session_state.current_student
        if student:
            st.subheader("Student Info")
            st.write(f"**ID:** {student['id']}")
            st.write(f"**Name:** {student['name']}")
            st.write(f"**Email:** {student['email']}")
            st.write(f"**Selected interest:** {student.get('selected_interest') or 'None'}")

            st.markdown("---")
            st.subheader("Choose Your Interest")

            # Available interests (must match interest_tag values in DB)
            interests = ["AI", "Robotics", "Data Science", "Software Development"]
            default_index = 0
            if student.get("selected_interest") in interests:
                default_index = interests.index(student["selected_interest"])

            selected_interest = st.selectbox(
                "Select an interest",
                options=interests,
                index=default_index,
            )

            if st.button("Save interest and load relevant information"):
                # 1) Save selected interest
                payload = {"interest": selected_interest}
                try:
                    resp = requests.put(
                        f"{API_BASE_URL}/me/interest",
                        json=payload,
                        headers=get_headers(),
                    )
                    if resp.status_code == 200:
                        st.success(f"Interest '{selected_interest}' saved.")
                        st.session_state.current_student = resp.json()
                    else:
                        try:
                            detail = resp.json().get("detail", resp.text)
                        except Exception:
                            detail = resp.text
                        st.error(f"Failed to save interest: {detail}")
                except requests.exceptions.ConnectionError:
                    st.error("Cannot reach API to save interest.")

                # 2) Fetch resources for this interest
                try:
                    resp2 = requests.get(
                        f"{API_BASE_URL}/me/resources",
                        headers=get_headers(),
                    )
                    if resp2.status_code == 200:
                        resources = resp2.json()
                        st.session_state.last_resources = resources
                        st.success("Loaded relevant information for your interest.")
                    else:
                        try:
                            detail = resp2.json().get("detail", resp2.text)
                        except Exception:
                            detail = resp2.text
                        st.error(f"Failed to load resources: {detail}")
                except requests.exceptions.ConnectionError:
                    st.error("Cannot reach API to load resources.")

            # Display last loaded resources
            resources = st.session_state.last_resources
            if resources:
                st.markdown("### Here is the information for you:")
                st.write(f"**Interest:** {resources['interest_tag']}")
                st.write(f"**Workshops:** {resources.get('workshops') or 'None'}")
                st.write(f"**Training:** {resources.get('training') or 'None'}")
                st.write(f"**Event:** {resources.get('event') or 'None'}")

    



