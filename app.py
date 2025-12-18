import streamlit as st
import json
import os
from src.core.orchestrator import KasparroOrchestrator

# Basic setup
st.set_page_config(page_title="Kasparro Content Engine", layout="wide")
st.title("Kasparro Content Engine")

# Input section
raw_text = st.text_area("Paste Raw Product Text Here", height=150)

if st.button("Generate Assets"):
    if not raw_text:
        st.warning("Please enter some text.")
    else:
        status_box = st.empty()
        status_box.text("Initializing pipeline...")
        
        # 1. Run the backend
        # We wrap this in a spinner so the UI doesn't freeze visually
        with st.spinner("Running AI Agents..."):
            app = KasparroOrchestrator()
            app.start_pipeline(raw_text)
        
        status_box.text("Pipeline finished. Loading results...")

        # 2. Read the generated files directly from output folder
        # This is a simple way to get data without changing backend code
        output_dir = "data/output"
        
        try:
            with open(f"{output_dir}/product_page.json", "r", encoding="utf-8") as f:
                prod_data = json.load(f)
            
            with open(f"{output_dir}/faq.json", "r", encoding="utf-8") as f:
                faq_data = json.load(f)

            with open(f"{output_dir}/comparison_page.json", "r", encoding="utf-8") as f:
                comp_data = json.load(f)

            # 3. Display Results
            st.success("Generation Complete")
            
            tab1, tab2, tab3 = st.tabs(["Product Page", "FAQs", "Competitor Analysis"])

            with tab1:
                st.subheader(prod_data['page_meta']['title'])
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Headline:** {prod_data['hero_section']['headline']}")
                    st.markdown(f"**Price:** {prod_data['hero_section']['price_display']}")
                
                with col2:
                    st.markdown("**Ingredients:**")
                    st.write(", ".join(prod_data['details_section']['ingredients_list']))

                with st.expander("View Full JSON"):
                    st.json(prod_data)

            with tab2:
                for item in faq_data['faqs']:
                    with st.expander(f"{item['question']}"):
                        st.write(item['answer'])
            
            with tab3:
                st.subheader("Verdict")
                st.write(comp_data['verdict'])
                
                st.markdown("### Comparison Table")
                st.dataframe(comp_data['comparison_table'])

        except Exception as e:
            st.error(f"Error loading output files: {e}")