# Streamlit Experimentation

## Links

- [Getting Started](https://docs.streamlit.io/get-started)
- [Streamlit Fundamentals](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
- [API Reference](https://docs.streamlit.io/develop/api-reference)
- [Streamlit Quests](https://blog.streamlit.io/streamlit-quests-getting-started-with-streamlit/)
- [Tutorial: Single page app](https://docs.streamlit.io/get-started/tutorials/create-an-app?ref=blog.streamlit.io)
- [Streamlit Starter Kit](https://blog.streamlit.io/streamlit-app-starter-kit-how-to-build-apps-faster/) - A project template for a Streamlit application

## Guidance

### Installing

```bash
# requirements
pip install streamlit

# Demo app
streamlit hello
```

### Running

Use any of:

```bash
streamlit run your_app.py [-- script args]
python -m streamlit run your_script.py
streamlit run https://whatever/streamlit_app.py
```

## Typical Application Steps

1. Install prerequisite libraries by specifying library names in `requirements.txt`
1. Customize the theme via `.streamlit/config.toml` (optional)
1. Create an app file `streamlit_app.py`
1. Inside the app file, call `import streamlit` as st
1. Specify the app tasks (e.g. read a CSV, perform data wrangling, display a scatter plot, train an ML model, etc.)
