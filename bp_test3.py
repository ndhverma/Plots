import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Violin Plot with CSV Upload')

# Create file uploader
uploaded_file = st.file_uploader('Upload a CSV file', type='csv')

# If a file was uploaded
if uploaded_file is not None:
    # Read the data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write('Original Data')
    st.write(df)

    # Get user input for x-axis and y-axis labels
    x_label = st.text_input('Enter x-axis label', 'Columns')
    y_label = st.text_input('Enter y-axis label', 'Values')

    # Create the violin plot
    fig, ax = plt.subplots()
    sns.violinplot(data=df, ax=ax)
    ax.set_title('Violin Plot')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Display the plot
    st.pyplot(fig)
else:
    st.write('Upload a CSV file.')
