import streamlit as st
from app import chat_interface


def main():
    st.set_page_config(page_title="Medical Consultation App", page_icon=":hospital:")
    apply_custom_css()

    st.markdown("<h1 style='color: black; font-family: Dyuthi;'>Medical Consultation App</h1>", unsafe_allow_html=True)

    mode = st.selectbox("Choose Mode:", ["Select", "General OPD", "Medical Advice"])

    if mode == "General OPD":
        st.header("General OPD Mode")
        chat_session(mode)
    elif mode == "Medical Advice":
        st.header("Medical Advice Mode")
        chat_session(mode)
    else:
        st.write("Please select a mode to proceed.")


def chat_session(mode):
    """Manage chat interactions within the selected mode."""
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat history
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-msg">You: {msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">Bot: {msg["content"]}</div>', unsafe_allow_html=True)

    # Input field for the user
    user_input = st.text_input("You: ", key="input")

    if st.button("Send"):
        if user_input:
            with st.spinner("Processing..."):
                # Process user input and get response
                response = chat_interface(mode, user_input)
            
            # Append user and bot messages to the session state
            st.session_state["messages"].append({"role": "user", "content": user_input})
            st.session_state["messages"].append({"role": "bot", "content": response})
            st.experimental_rerun()


def apply_custom_css():
    """Apply custom CSS for styling."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dyuthi&display=swap');
        .reportview-container { background: #f0f2f6; }
        .sidebar .sidebar-content { background: #f0f2f6; }
        h1 { color: black; font-family: 'Dyuthi', sans-serif; }
        .stButton>button { background-color: white; color: black; border: 2px solid black; padding: 5px 15px; border-radius: 5px; font-size: 16px; }
        .stButton>button:hover { background-color: #f0f0f0; }
        .user-msg { text-align: left; background-color: #f1f1f1; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
        .bot-msg { text-align: left; background-color: #e1ecf4; color: black; font-weight: bold; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
        </style>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()


# import streamlit as st
# from app import chat_interface, get_doctor_details


# def main():
#     st.set_page_config(page_title="Medical Consultation App", page_icon=":hospital:")
#     apply_custom_css()

#     st.markdown("<h1 style='color: black; font-family: Dyuthi;'>Medical Consultation App</h1>", unsafe_allow_html=True)

#     mode = st.selectbox("Choose Mode:", ["Select", "General OPD", "Medical Advice"])

#     if mode == "General OPD":
#         st.header("General OPD Mode")
#         chat_session(mode)
#     elif mode == "Medical Advice":
#         st.header("Medical Advice Mode")
#         chat_session(mode)
#     else:
#         st.write("Please select a mode to proceed.")


# def chat_session(mode):
#     """Manage chat interactions within the selected mode."""
#     if "messages" not in st.session_state:
#         st.session_state["messages"] = []

#     user_input = st.text_input("You: ", key="input")

#     if st.button("Send"):
#         if user_input:
#             with st.spinner("Processing..."):
#                 response = chat_interface(mode, user_input)
#             st.session_state["messages"].append({"role": "user", "content": user_input})
#             st.session_state["messages"].append({"role": "bot", "content": response})
#             st.experimental_rerun()

#     for msg in st.session_state["messages"]:
#         if msg["role"] == "user":
#             st.markdown(f'<div class="user-msg">You: {msg["content"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="bot-msg">Bot: {msg["content"]}</div>', unsafe_allow_html=True)


# def apply_custom_css():
#     """Apply custom CSS for styling."""
#     st.markdown("""
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=Dyuthi&display=swap');
#         .reportview-container { background: #f0f2f6; }
#         .sidebar .sidebar-content { background: #f0f2f6; }
#         h1 { color: black; font-family: 'Dyuthi', sans-serif; }
#         .stButton>button { background-color: white; color: black; border: 2px solid black; padding: 5px 15px; border-radius: 5px; font-size: 16px; }
#         .stButton>button:hover { background-color: #f0f0f0; }
#         .user-msg { text-align: left; background-color: #f1f1f1; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
#         .bot-msg { text-align: left; background-color: #e1ecf4; color: black; font-weight: bold; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
#         </style>
#     """, unsafe_allow_html=True)


# if __name__ == "__main__":
#     main()
