import streamlit as st
from stmol import showmol
import py3Dmol


def render_mol(pdb):
    pdbview = py3Dmol.view(width=600,height=600)
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'model': -1}, {"cartoon": {'color': 'spectrum'}})
    pdbview.setBackgroundColor('#fafafa')#('0xeeeeee')
    pdbview.zoomTo()
    pdbview.spin(True)
    showmol(pdbview, height = 500,width=800)


# uploaded_files = st.sidebar.file_uploader("Choose pdb files", accept_multiple_files=True)
# st.write("Uploaded Files: ",uploaded_files)
# for uploaded_file in uploaded_files:
#     st.write("Uploaded File: ",uploaded_file)
#     pdb = uploaded_file.getvalue().decode("utf-8")
#     print(pdb)
#     render_mol(pdb)