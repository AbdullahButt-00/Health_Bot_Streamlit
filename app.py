import base64
import google.generativeai as genai

# === API Configuration ===
encoded_api_key = "QUl6YVN5QWwyclhPcW9pMlpveFE2Q1Z3T1ZqUURHeXBBZTNIVFVn"

def decode_api_key(encoded_api_key):
    decoded_bytes = base64.b64decode(encoded_api_key.encode("utf-8"))
    decoded_str = str(decoded_bytes, "utf-8")
    return decoded_str

genai.configure(api_key=decode_api_key(encoded_api_key))
llm = genai.GenerativeModel(model_name="gemini-1.5-pro")
convo = llm.start_chat()

# === Embedded Doctor Data ===
DOCTOR_DATA = {
    "doctor_name": [
        "Dr. John Smith",
        "Dr. Emily Davis",
        "Dr. Michael Brown",
        "Dr. Sarah Johnson",
        "Dr. Daniel Lee",
        "Dr. Olivia Martinez",
        "Dr. William Garcia",
        "Dr. Ava Wilson",
        "Dr. James White",
        "Dr. Sophia Taylor"
    ],
    "specialty": [
        "Cardiologist",
        "Dermatologist",
        "Orthopedic",
        "Pediatrician",
        "Neurologist",
        "Ophthalmologist",
        "ENT Specialist",
        "Psychiatrist",
        "Endocrinologist",
        "Gastroenterologist"
    ],
    "available_timings": [
        "10:00 AM - 1:00 PM",
        "2:00 PM - 5:00 PM",
        "9:00 AM - 12:00 PM",
        "1:00 PM - 4:00 PM",
        "11:00 AM - 2:00 PM",
        "3:00 PM - 6:00 PM",
        "8:00 AM - 11:00 AM",
        "1:00 PM - 3:00 PM",
        "10:00 AM - 12:00 PM",
        "2:00 PM - 4:00 PM"
    ]
}

# === Chat Interface Logic ===
def chat_interface(mode, user_input):
    """Handle chat interactions based on the selected mode."""
    if mode == "General OPD":
        return handle_general_opd(user_input)
    elif mode == "Medical Advice":
        return medical_consultance(user_input, mode)
    else:
        return "Please select a valid mode."

# === General OPD Handler ===
def handle_general_opd(user_input):
    """Process General OPD queries."""
    if user_input.lower() == "list all doctors":
        return format_doctor_data()
    elif "specialist" in user_input.lower():
        specialty = user_input.split("specialist in ")[-1].strip()
        return filter_doctors_by_specialty(specialty)
    else:
        return "Sorry, I couldn't understand your query. Please ask about doctors or specialties."

def format_doctor_data():
    """Format all doctor data for display."""
    result = []
    for name, specialty, timing in zip(DOCTOR_DATA["doctor_name"], DOCTOR_DATA["specialty"], DOCTOR_DATA["available_timings"]):
        result.append(f"{name}, {specialty}, Available: {timing}")
    return "\n".join(result)

def filter_doctors_by_specialty(specialty):
    """Filter doctors by their specialty."""
    result = []
    for name, spec, timing in zip(DOCTOR_DATA["doctor_name"], DOCTOR_DATA["specialty"], DOCTOR_DATA["available_timings"]):
        if specialty.lower() in spec.lower():
            result.append(f"{name}, {spec}, Available: {timing}")
    return "\n".join(result) if result else f"No doctors found for the specialty '{specialty}'."

# === Medical Consultation Logic ===
def medical_consultance(script, mode):
    """Provide medical consultations based on user input."""
    if mode == "General OPD":
        prompt = f"""
            - Provide General OPD services, including doctor availability and specialties.
            - Use the following data for answers:
              {DOCTOR_DATA}.
            - Answer queries clearly without suggesting medicines or diets.
            - Keep the output simple and easy to understand by the user.
            - Do not reply with useless information such as "I'm sorry, but I cannot provide medical advice."
            User Input: {script}
            """
    elif mode == "Medical Advice":
        prompt = f"""
            - Act as a doctor providing personalized advice.
            - Recommend medicines and diet plans based on symptoms or conditions.
            - If it asks any General OPD question, reply "KINDLY CHOOSE 'General OPD' mode as this is not my work."
            User Input: {script}
            """

    try:
        response = convo.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error Occurred: {e}"


# import base64
# import pandas as pd
# import google.generativeai as genai


# # === API Configuration ===
# encoded_api_key = "QUl6YVN5QWwyclhPcW9pMlpveFE2Q1Z3T1ZqUURHeXBBZTNIVFVn"

# def decode_api_key(encoded_api_key):
#     decoded_bytes = base64.b64decode(encoded_api_key.encode('utf-8'))
#     decoded_str = str(decoded_bytes, 'utf-8')
#     return decoded_str

# genai.configure(api_key=decode_api_key(encoded_api_key))
# llm = genai.GenerativeModel(model_name="gemini-1.5-pro")
# convo = llm.start_chat()


# # === Doctor Data Handling ===
# def load_doctors_data(file_path="doctors.csv"):
#     """Load doctor data from a CSV file."""
#     try:
#         return pd.read_csv(file_path)
#     except FileNotFoundError:
#         return pd.DataFrame(columns=["doctor_name", "specialty", "available_timings"])

# def get_doctor_details(specialty=None):
#     """Retrieve doctor details, optionally filtered by specialty."""
#     doctors_data = load_doctors_data()
#     if specialty:
#         doctors_data = doctors_data[doctors_data['specialty'].str.contains(specialty, case=False, na=False)]
#     return doctors_data


# # === Chat Interface Logic ===
# def chat_interface(mode, user_input):
#     """Handle chat interactions based on the selected mode."""
#     if mode == "General OPD":
#         doctors_data = get_doctor_details()
#         if user_input.lower() == "list all doctors":
#             return doctors_data.to_dict(orient="records")
#         elif "specialist" in user_input.lower():
#             specialty = user_input.split("specialist in ")[-1]
#             filtered_data = get_doctor_details(specialty)
#             return filtered_data.to_dict(orient="records")
#         else:
#             return "Sorry, I couldn't understand your query. Please ask about doctors or specialties."

#     elif mode == "Medical Advice":
#         return medical_consultance(user_input, mode)
#     else:
#         return "Please select a valid mode."


# # === Medical Consultation Logic ===
# def medical_consultance(script, mode):
#     """Provide medical consultations based on user input."""
#     if mode == "General OPD":
#         prompt = f"""
#             - Provide General OPD services, including doctor availability and specialties.
#             - In the General OPD/Consultant services, users can ask medical-related questions. They can inquire about doctors, their specialties, and available consultation times.
#             - Answer queries clearly without suggesting medicines or diets.
#             - Keep the output simple and easy to understand by the user.
#             - Do not reply with useless information such as "I'm sorry, but I cannot provide medical advice."
#             - Output must not contain any other info, e.g., tips or medicines.
#             - Output should only contain answers to the user's questions, no extra description.
#             - use doctors.csv to check names for doctors, their specialties, and available consultation times.
#             - You can answer general chat briefly to understand the context or query of user.
#             User Input: {script}
#             """
#     elif mode == "Medical Advice":
#         prompt = f"""
#             - Act as a doctor providing personalized advice.
#             - Recommend medicines and diet plans based on symptoms or conditions.
#             - If it asks any General OPD question, reply "KINDLY CHOOSE 'General OPD' mode as this is not my work.
#             - Output should also contain medicine and diet plan recommendations.
#             - Suggest suitable diet plans tailored to the user's medica.
#             - Users can input their symptoms or diagnosed diseases
#             - Do not reply with useless information such as "I'm sorry, but I cannot provide medical advice."
#             User Input: {script}
#             """

#     try:
#         response = convo.send_message(prompt)
#         return response.text
#     except Exception as e:
#         return f"Error Occurred: {e}"
