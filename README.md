# Streamlit_Widget_APP
A simple interactive Streamlit app that demonstrates user input via text boxes, sliders, and select boxes while displaying data using Pandas. It also supports CSV file uploads to dynamically update the displayed data.
# Streamlit Widget App

This repository contains a simple Streamlit application that demonstrates various interactive widgets and data handling using Pandas. The app showcases basic Streamlit functionalities like text input, sliders, select boxes, and file uploads.

## Features

- **Text Input:** Accepts a user's name.
- **Slider:** Allows users to select their age.
- **Select Box:** Lets users choose their favorite programming language.
- **Dynamic Greetings:** Displays a greeting if a name is provided.
- **Data Display:** Creates a sample CSV file from a DataFrame and displays it.
- **File Uploader:** Supports uploading a CSV file and displaying its content.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

You can install the required packages using pip:

```bash
pip install streamlit pandas numpy

Running the Application
Clone this repository to your local machine.
Navigate to the project folder:
cd /path/to/the/cloned/repository

Run the Streamlit app:
treamlit run widget_streamlit.py

The app will open in your default web browser at http://localhost:8501.
How It Works
The app displays a title using st.title.
Users are prompted to enter their name via st.text_input.
A numeric slider (st.slider) allows users to select an age.
The selected age and chosen programming language (from a st.selectbox) are displayed on the page.
If a name is entered, the app greets the user.
A sample DataFrame is created, saved as a CSV file, and its content is displayed.
Users can upload their own CSV using st.file_uploader, and if provided, the file is read and displayed.

Acknowledgments
Developed using Streamlit.
Data handling with Pandas and NumPy.
