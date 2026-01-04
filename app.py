'''
Streamlit App for CrewAI Research and Blog Crew
USING PYTHON 3.11.9
'''

import streamlit as st
import os
from pathlib import Path
from src.crew import ResearchAndBlogCrew
import time

# Page configuration
st.set_page_config(
    page_title="Research & Blog Agent",
    page_icon="📝",
    layout="wide",
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #1565C0;
    }
    .output-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #1E88E5;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'crew_running' not in st.session_state:
    st.session_state.crew_running = False
if 'research_report' not in st.session_state:
    st.session_state.research_report = None
if 'blog_post' not in st.session_state:
    st.session_state.blog_post = None

# Header
st.markdown('<div class="main-header">📝 Research & Blog Agent</div>',
            unsafe_allow_html=True)
st.markdown('<div class="sub-header">Powered by Ollama & CrewAI - Generate comprehensive research reports and engaging blog posts</div>', unsafe_allow_html=True)


# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🎯 Enter Your Topic")
    topic = st.text_input(
        "What would you like to research and write about?",
        placeholder="e.g., Electric Vehicles, Artificial Intelligence, Climate Change...",
        help="Enter any topic you want the AI agents to research and create content about"
    )

with col2:
    st.header("🚀 Action")
    st.write("")  # Spacing
    run_button = st.button("Generate Content", type="primary",
                           disabled=st.session_state.crew_running)

# Run the crew
if run_button and topic:
    st.session_state.crew_running = True
    st.session_state.research_report = None
    st.session_state.blog_post = None

    with st.spinner("🤖 AI Agents are working on your request..."):
        try:
            # Create progress indicators
            progress_container = st.container()
            with progress_container:
                st.subheader("📊 Progress")
                progress_bar = st.progress(0)
                status_text = st.empty()

                # Update progress - Research phase
                status_text.text(
                    "🔍 Research Agent: Gathering information and creating detailed report...")
                progress_bar.progress(25)

                # Run the crew
                inputs = {"topic": topic}
                crew_instance = ResearchAndBlogCrew()

                # Update progress - Blog writing phase
                status_text.text(
                    "✍️ Blog Writer Agent: Crafting engaging blog post...")
                progress_bar.progress(50)

                # Execute the crew
                result = crew_instance.crew().kickoff(inputs=inputs)

                # Update progress - Finalizing
                status_text.text("📝 Finalizing outputs...")
                progress_bar.progress(75)

                # Read the generated files
                research_report_path = Path("outputs/research_report.md")
                blog_post_path = Path("outputs/blog_post.md")

                if research_report_path.exists():
                    with open(research_report_path, 'r', encoding='utf-8') as f:
                        st.session_state.research_report = f.read()

                if blog_post_path.exists():
                    with open(blog_post_path, 'r', encoding='utf-8') as f:
                        st.session_state.blog_post = f.read()

                progress_bar.progress(100)
                status_text.text("✅ Content generation complete!")
                time.sleep(1)

            st.success(
                "🎉 Successfully generated research report and blog post!")

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.exception(e)

        finally:
            st.session_state.crew_running = False

elif run_button and not topic:
    st.warning("⚠️ Please enter a topic before generating content.")

# Display results
if st.session_state.research_report or st.session_state.blog_post:
    st.markdown("---")
    st.header("📄 Generated Content")

    # Create tabs for the outputs
    tab1, tab2 = st.tabs(["📊 Research Report", "📝 Blog Post"])

    with tab1:
        if st.session_state.research_report:
            st.markdown(st.session_state.research_report)

            # Download button for research report
            st.download_button(
                label="⬇️ Download Research Report",
                data=st.session_state.research_report,
                file_name="research_report.md",
                mime="text/markdown"
            )
        else:
            st.info("Research report will appear here after generation.")

    with tab2:
        if st.session_state.blog_post:
            st.markdown(st.session_state.blog_post)

            # Download button for blog post
            st.download_button(
                label="⬇️ Download Blog Post",
                data=st.session_state.blog_post,
                file_name="blog_post.md",
                mime="text/markdown"
            )
        else:
            st.info("Blog post will appear here after generation.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>Built with Ollama & CrewAI | Powered by Streamlit</p>
    </div>
""", unsafe_allow_html=True)
