from shiny.express import input, ui, render
from pathlib import Path
import pandas as pd
from shinywidgets import render_plotly
import plotly.express as px
from data_import import df

ui.h1("Penguin Dashboard")
with ui.sidebar(bg="#f8f8f8"):
    ui.input_slider(id='mass', label='Maximum body mass (grams) to display', min=2000, max=8000, value=6000)

with ui.layout_columns():
    with ui.card():
        'Bill dimensions by species'

        @render_plotly
        def plot():
            df_subset = subset_by_upper_bound(df, 'body_mass_g', input.mass())
            if input.show_species():
                return px.scatter(df_subset, x='bill_depth_mm', y='bill_length_mm', color='species')
            else:
                return px.scatter(df_subset, x='bill_depth_mm', y='bill_length_mm')
        
        ui.input_checkbox('show_species', 'Show Species', value=True)

    with ui.card():
        'Raw Data'

        @render.data_frame
        def data():
            return subset_by_upper_bound(df, 'body_mass_g', input.mass())

def subset_by_upper_bound(df: pd.DataFrame, column_name: str, max_value):
    return df[df[column_name] < max_value]
