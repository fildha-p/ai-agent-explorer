import streamlit as st
import os
from openai import OpenAI
from pydantic import BaseModel
from typing import List
import requests

st.set_page_config(page_title="AI Agent SDK Explorer", page_icon="🤖", layout="wide")

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    cooking_time: int
    instructions: List[str]

def recipe_generator(dish_name: str, client: OpenAI) -> Recipe:
    prompt = f"""
Generate a recipe for {dish_name}.

Return valid JSON only.
Use exactly this structure:
{{
  "title": "string",
  "ingredients": ["string", "string"],
  "cooking_time": 20,
  "instructions": ["step 1", "step 2"]
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a recipe generator. Respond in JSON only."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    recipe_data = response.choices[0].message.content
    return Recipe.model_validate_json(recipe_data)

def web_research_agent(query: str) -> str:
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    abstract = data.get("Abstract", "")
    return abstract if abstract else "No abstract available"

st.title("🤖 AI Agent Explorer")
st.markdown("Explore the capabilities of your AI agents.")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if not api_key:
        st.warning("Please enter your OpenAI API key to use AI agents.")

tab1, tab2 = st.tabs(["🍳 Recipe Generator", "🔍 Web Research"])

with tab1:
    st.header("Recipe Generator")
    dish = st.text_input("What would you like to cook?", placeholder="e.g. Pasta Carbonara")

    if st.button("Generate Recipe", key="recipe_btn"):
        if not api_key:
            st.error("API Key missing!")
        elif not dish.strip():
            st.error("Please enter a dish name.")
        else:
            try:
                client = OpenAI(api_key=api_key)
                with st.spinner("Chef AI is thinking..."):
                    recipe = recipe_generator(dish, client)

                    st.success(f"Recipe for {recipe.title} ready!")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Ingredients")
                        for ing in recipe.ingredients:
                            st.write(f"- {ing}")

                    with col2:
                        st.subheader("Details")
                        st.write(f"**Cooking Time:** {recipe.cooking_time} minutes")

                    st.subheader("Instructions")
                    for i, step in enumerate(recipe.instructions, start=1):
                        st.write(f"{i}. {step}")

            except Exception as e:
                st.error(f"Error generating recipe: {e}")

with tab2:
    st.header("Web Research")
    query = st.text_input("What do you want to research?", placeholder="e.g. Artificial Intelligence")

    if st.button("Research", key="research_btn"):
        if not query.strip():
            st.error("Please enter a topic.")
        else:
            with st.spinner("Researching..."):
                result = web_research_agent(query)
                st.info(result)