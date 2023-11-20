import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re


df = pd.read_csv("UpdatedResumeDataSet.csv")



def create_visualization():
    
    # Count the number of resumes in each Category
    Category_counts = df['Category'].value_counts()

    # Create a bar chart of the Category counts
    fig, ax = plt.subplots()
    sns.barplot(x=Category_counts.index, y=Category_counts.values, ax=ax)
    ax.set(xlabel="Category", ylabel="Count", title="Distribution of Resume Categories")
    ax.tick_params(rotation=90)

    # Display the visualization
    st.pyplot(fig)


# Function to display a subset of the data
def display_data_subset():
    # Select a random subset of the data
    subset = df.sample(n=100, random_state=1)

    # Display the subset data using st.dataframe
    st.dataframe(subset)


# Create Streamlit app
def main():
    st.title("Resume Screening Dataset Analysis")
    st.title("What is the distribution of different categories of resumes in the dataset?")
    
    # Display the visualization
    st.subheader("Distribution of Resume Categories")
    create_visualization()

    # Display a subset of the data
    st.subheader("Subset of Data")
    display_data_subset()


if __name__ == '__main__':
    main()