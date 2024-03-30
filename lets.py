import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAKOjtXWhQKL_wDbFkSYPbfmtQYj2vUMCs")

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 50, 
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.title('Project Planner')

project_idea = st.text_area("Describe your coding project idea:", height=150)
must_have_features = st.text_input("List must-have features:")
tech_stack = st.text_input("Enter technology stack of your project:")
timeline = st.text_input("What is your timeline for this project?")

if st.button('Generate Project Charter'):
    if project_idea and must_have_features and tech_stack and timeline:
        prompt = (
            f"The coding project idea is: {project_idea}\n"
            f"The must-have features for launch are: {must_have_features}\n"
            f"The technology stack for the project is: {tech_stack}\n"
            f"The expected timeline for the project is: {timeline}\n\n"

            "Please analyze the project details and generate a draft project charter document covering the following aspects:\n\n"

            "- One-paragraph summarizing the project objectives, key requirements, and outcomes\n"
            "- High-level user flow diagrams showing the key screens and user journey (provide multiple examples using mermaid JS syntax if required)\n"
            "- Breakdown of the high-level technical design and architecture\n" 
            "- Weekly project plan from design, development, testing to launch\n"
            "- Job roles required like frontend, backend, devops engineers, etc.\n"
            "- Technology stack required to build the product\n"
            "- Initial effort estimation overview across product, engineering, testing\n"
            "- Biggest areas of risks and assumptions to validate\n\n"
            "- Additinal Suggessions for project\n\n"

            "For the Agile process flow diagram, please use the mermaid JS syntax, for example:\n\n"

            "Exaple No. 1:\n\n"

            "```mermaid\n"
            "flowchart TD\n"
            "    A[Project Kickoff] --> B[Iteration 1 Planning]\n"
            "    B --> C{Sprint 1}\n"
            "    C --> D{Sprint Review & Retrospective}\n"
            "    D --> E[Iteration 2 Planning]\n"
            "    E --> F{Sprint 2}\n"
            "    F --> G{Sprint Review & Retrospective}\n"
            "    G --> H{...}\n"
            "    H --> I[Final Review & Project Closure]\n"
            "```\n\n"

            """Example No. 2:\n\n"

            ```mermaid\n"
            "flowchart TD\n"
            "    A[Ecommerce] --> B{View product} \n"
            "    B --> C{Add to cart}\n"
            "    C --> D[Payment]\n"
            "    D --> E[Order confirmed]\n"
            "```\n\n"""

            """Example No. 3:\n\n"
            '''mermaid\\n"           
            "flowchart TD\\n"           
              " A[Social Media App] --> B{Login/Signup}\\n"          
                " B --> C{News Feed}\\n"           
                " C --> D{Post Content}\\n"           
                " D --> E{View Profile}\\n"           
                "\n\n"""

            "Provide comprehensive details in each charter section for clarity. Ensure it sets up the key technical guidelines, resource planning, and execution roadmap based on the information provided."
        )

        response = model.generate_content([prompt])
        st.write(response.text)
    else:
        st.error("Please complete all fields to generate the project charter.")