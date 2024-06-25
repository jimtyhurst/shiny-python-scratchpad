from shiny.express import input, ui, render
from pathlib import Path
import pandas as pd
from shinywidgets import render_plotly
import plotly.express as px

file_path = Path(__file__).parent / "penguins.csv"

df = pd.read_csv(file_path)

ui.h1("My Penguin Dashboard")
with ui.sidebar(bg="#f8f8f8"):
    ui.input_slider(id='mass', label='Maximum body mass (grams) to display', min=2000, max=8000, value=6000)

with ui.layout_columns():
    with ui.card():
        'Bill dimensions by species'

        @render_plotly
        def plot():
            df_subset = df[df['body_mass_g'] < input.mass()]
            if input.show_species():
                return px.scatter(df_subset, x='bill_depth_mm', y='bill_length_mm', color='species')
            else:
                return px.scatter(df_subset, x='bill_depth_mm', y='bill_length_mm')
        
        ui.input_checkbox('show_species', 'Show Species', value=True)

    with ui.card():
        'Raw Data'

        @render.data_frame
        def data():
            return df[df['body_mass_g'] < input.mass()]
