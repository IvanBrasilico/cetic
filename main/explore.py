import pandas as pd
import streamlit as st
import os

from download_data import do_downloads


@st.cache()
def get_files():
    do_downloads()
    dirlist = [name for name in os.listdir('bases')
               if os.path.isdir(os.path.join('bases', name))]
    return {dirname: os.listdir(os.path.join('bases', dirname)) for dirname in dirlist}


directories = get_files()
st.title('Streamlit Cetic.br app')
option_dir = st.selectbox(
    'Qual diretório?',
    list(directories.keys()))
option = st.selectbox(
    'Qual arquivo?',
    directories[option_dir])
'You selected: ', option
df = pd.read_excel(os.path.join('bases', option_dir, option), engine="odf")

if st.checkbox('Show dataframe', True):
    df
