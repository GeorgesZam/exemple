import streamlit as st
import pandas as pd

# Fonction pour traiter les données
def data_processing_function(data):
    # Logique de traitement des données personnalisée
    # Exemple : ajout d'une colonne 'Processed'
    data['Processed'] = data.apply(lambda row: row.sum(), axis=1)
    return data

# Fonction pour traiter les fichiers et générer un rapport consolidé
def process_data(files):
    combined_data = pd.DataFrame()
    for file in files:
        data = pd.read_excel(file)
        processed_data = data_processing_function(data)
        combined_data = combined_data.append(processed_data, ignore_index=True)
    combined_data.to_excel("consolidated_report.xlsx", index=False)
    return combined_data

# Titre de la page
st.title("Data Processing and Consolidation")

# Section pour télécharger des fichiers
st.header("Upload your Excel files")
uploaded_files = st.file_uploader("Choose Excel files", accept_multiple_files=True, type=["xlsx"])

if uploaded_files:
    st.write("Processing files...")
    combined_data = process_data(uploaded_files)
    st.write("Here is the consolidated data:")
    st.write(combined_data)
    
    # Lien pour télécharger le fichier consolidé
    st.write("Download the consolidated report:")
    with open("consolidated_report.xlsx", "rb") as file:
        btn = st.download_button(
            label="Download Excel",
            data=file,
            file_name="consolidated_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.write("Please upload at least one Excel file to proceed.")
