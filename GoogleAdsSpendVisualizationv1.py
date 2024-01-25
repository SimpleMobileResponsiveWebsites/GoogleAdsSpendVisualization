import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('Google Ads Spend Visualization')

    st.markdown("""
    Please upload a CSV file with the following columns:
    - Keyword
    - Avg. monthly searches
    - Three month change
    - YoY change
    - Competition
    - Competition (indexed value)
    - Top of page bid (low range)
    - Top of page bid (high range)
    - Ad impression share
    - Organic average position
    - Organic impression share
    - In Account
    """)

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        required_columns = [
            'Keyword',
            'Avg. monthly searches',
            'Three month change',
            'YoY change',
            'Competition',
            'Competition (indexed value)',
            'Top of page bid (low range)',
            'Top of page bid (high range)',
            'Ad impression share',
            'Organic average position',
            'Organic impression share',
            'In Account'
        ]

        missing_columns = [col for col in required_columns if col not in data.columns]

        if not missing_columns:
            st.success("Uploaded file has all the required columns.")

            # User selects a keyword to filter for the y-axis
            keyword_to_filter = st.selectbox('Select a keyword for the y-axis', data['Keyword'].unique())

            # Filter data for the selected keyword
            keyword_data = data[data['Keyword'] == keyword_to_filter]

            # User selects the columns to visualize on the x-axis
            x_axis_options = required_columns.copy()
            x_axis_options.remove('Keyword')  # Remove 'Keyword' as it is used for y-axis
            selected_x_columns = st.multiselect('Select columns for the x-axis', x_axis_options, default=x_axis_options[1])  # Default to second column

            # Creating and displaying the graph
            if st.button("Create Graph"):
                plt.figure(figsize=(10, 6))

                # Loop through selected x-axis columns and create subplots for each
                for i, column in enumerate(selected_x_columns, 1):
                    plt.subplot(len(selected_x_columns), 1, i)
                    sns.scatterplot(x=column, y='Keyword', data=keyword_data)
                    plt.tight_layout()

                st.pyplot(plt)

        else:
            st.error(f"Uploaded file is missing the following required columns: {', '.join(missing_columns)}")

if __name__ == "__main__":
    main()
