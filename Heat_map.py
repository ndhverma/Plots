import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Heatmap with CSV Upload')

# Create file uploader
uploaded_file = st.file_uploader('Upload a CSV file', type='csv')

# If a file was uploaded
if uploaded_file is not None:
    # Read the data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write('Original Data')
    st.write(df)

    # Create the heatmap
    fig, ax = plt.subplots()
    sns.heatmap(data=df.corr(), ax=ax, annot=True, cmap='coolwarm')
    ax.set_title('Heatmap')

    # Display the plot
    st.pyplot(fig)
else:
    st.write('Upload a CSV file.')
