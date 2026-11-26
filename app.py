import streamlit as st
from google import genai

client = genai.Client()

st.set_page_config(
    page_title="AI WhatsApp Reply Generator",
    layout="centered"
)

st.title("AI WhatsApp Reply Generator")

st.write(
    "Paste a WhatsApp message and generate a clear and suitable reply."
)

received_message = st.text_area(
    "Received WhatsApp Message",
    placeholder="Example: Hi, can you please send me the project details?",
    height=180
)

reply_tone = st.selectbox(
    "Select Reply Tone",
    [
        "Professional",
        "Friendly",
        "Polite",
        "Formal",
        "Short and Direct",
        "Customer Support"
    ]
)

reply_language = st.selectbox(
    "Select Reply Language",
    [
        "English",
        "Hindi",
        "Hinglish"
    ]
)

additional_instruction = st.text_input(
    "Additional Instruction",
    placeholder="Example: Mention that I will send the details tomorrow"
)

if st.button(
    "Generate Reply",
    type="primary",
    use_container_width=True
):

    if received_message.strip() == "":
        st.warning("Please enter the received WhatsApp message.")

    else:
        prompt = f"""
You are a WhatsApp message reply assistant.

Create a suitable reply to the following WhatsApp message.

Received Message:
{received_message}

Reply Tone:
{reply_tone}

Reply Language:
{reply_language}

Additional Instruction:
{additional_instruction}

Instructions:
- Write a clear and natural WhatsApp reply.
- Follow the selected tone and language.
- Keep the reply suitable for WhatsApp.
- Do not make the reply unnecessarily long.
- Do not add headings or explanations.
- Return only the reply message.
"""

        with st.spinner("Generating reply..."):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        st.success("Reply generated successfully.")

        st.subheader("Generated Reply")

        st.text_area(
            "Reply",
            value=response.text,
            height=200,
            label_visibility="collapsed"
        )


# set GEMINI_API_KEY=your api_key (in Windows) or export GEMINI_API_KEY=your api_key (in Linux/Mac) in the terminal before running the app
# after setting the api key, run the app using the command: streamlit run app.py