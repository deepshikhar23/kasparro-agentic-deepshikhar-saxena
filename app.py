import streamlit as st
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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
        with st.spinner("Running AI Agents..."):
            try:
                app = KasparroOrchestrator()
                # We run the pipeline (which saves the files to data/output)
                app.start_pipeline(raw_text)
                status_box.text("Pipeline finished. Loading results...")
                
                # 2. Read the generated files directly from output folder
                output_dir = "data/output"
                
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
                    st.subheader(prod_data.get('page_meta', {}).get('title', 'Product Page'))
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        hero = prod_data.get('hero_section', {})
                        st.markdown(f"**Headline:** {hero.get('headline', 'N/A')}")
                        st.markdown(f"**Price:** {hero.get('price_display', 'N/A')}")
                    
                    with col2:
                        st.markdown("**Ingredients:**")
                        ingredients = prod_data.get('details_section', {}).get('ingredients_list', [])
                        st.write(", ".join(ingredients))

                    with st.expander("View Full JSON"):
                        st.json(prod_data)

                with tab2:
                    faqs = faq_data.get('faqs', [])
                    for item in faqs:
                        with st.expander(f"{item.get('question', 'Q')}"):
                            st.write(item.get('answer', 'A'))
                
                with tab3:
                    st.subheader("Verdict")
                    st.write(comp_data.get('verdict', 'No verdict'))
                    
                    st.markdown("### Comparison Table")
                    # Check if comparison_table exists and is valid
                    if 'comparison_table' in comp_data:
                        st.dataframe(comp_data['comparison_table'])
                    else:
                        st.json(comp_data)

            except Exception as e:
                st.error(f"Error during execution: {str(e)}")