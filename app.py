import streamlit as st


def main():
    st.set_page_config(page_title="LangChain Bot", page_icon=":robot:")

    st.header("LangChain Bot :robot:")
    st.text_input("Ask a quesstion about the website")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your knowledge base here")
        st.button("Process")


if __name__ == "__main__":
    main()
