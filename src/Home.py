import streamlit as st
# Image at the top of the page
st.image('https://raw.githubusercontent.com/2d2f/chat/main/loopGPT.png')

#Config
st.set_page_config(layout="wide", page_title="LoopGPT")


#Contact
with st.sidebar.expander("Contact"):



    st.write("**Mail** : luc@loopearplugs.com")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>LoopGPT</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm LoopGPT, my goal is to help you better understand your data.
    I support PDF, TXT, and CSV data, with more coming soon!</h5>
    """,
    unsafe_allow_html=True)
#st.markdown("---")


#Robby's Pages
#st.subheader("🚀 Robby's Pages")
#st.write("""
#- **Robby-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (can't process the whole file just index useful parts(max 4) for respond to the user ) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html) + (soon) Summarize data
#- **Robby-Sheet** (beta): Chat on tabular data (CSV) | for precise information | can process the whole file (with python code) | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation (experimental)
#- (soon) **Robby-Youtube**: Chat on YouTube videos
#- (soon) **Robby-Lyrics**: Chat and analyze music lyrics | works by scraping lyrics from Genius
#- (soon) **Robby-Github**: Chat over GitHub repositories for understanding the code
#- (soon) **Robby-Website**: Chat with any website you provide
#""")
#st.markdown("---")


##Contributing
#st.markdown("### 🎯 Contributing")
##st.markdown("""
#**Robby is under regular development. Feel free to contribute and help me make it even more data-aware!**
#""", unsafe_allow_html=True)





