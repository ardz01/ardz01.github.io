import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import random

app = dash.Dash(__name__)

# Simulated data (replace with actual data)
locations = ['Location A', 'Location B']
crop_suggestions_data = {location: random.uniform(5, 15) for location in locations}
planting_times_data = {location: random.uniform(20, 40) for location in locations}
weather_data = {location: random.uniform(25, 35) for location in locations}

# Layout
app.layout = html.Div([
    html.H1("Farmers' Recommendations Dashboard", style={'text-align': 'center'}),
    
    # User Input Form
    html.Div([
        html.Label("Select Location:"),
        dcc.Dropdown(
            id='location-dropdown',
            options=[{'label': loc, 'value': loc} for loc in locations],
            value=locations[0],
        ),
        
        html.Label("Landholdings (acres):"),
        dcc.Input(id='land-input', type='number', value=5),
        
        html.Label("Microclimate Type:"),
        dcc.RadioItems(
            id='microclimate-radio',
            options=[
                {'label': 'Warm', 'value': 'warm'},
                {'label': 'Moderate', 'value': 'moderate'},
                {'label': 'Cool', 'value': 'cool'}
            ],
            value='warm',
        ),
        
        html.Label("Preferred Crop Type:"),
        dcc.Dropdown(
            id='crop-type-dropdown',
            options=[
                {'label': 'Cereal Crops', 'value': 'cereal'},
                {'label': 'Fruits', 'value': 'fruit'},
                {'label': 'Vegetables', 'value': 'vegetable'}
            ],
            multi=True,
            value=['cereal'],
        ),
    ], style={'margin-bottom': '20px'}),
    
    # Recommendations Section
    html.Div([
        html.H2("Drought-Resistant Crop Suggestions"),
        dcc.Graph(id='crop-suggestions-plot'),
    ], style={'margin-bottom': '40px'}),
    
    html.Div([
        html.H2("Optimized Planting Times"),
        dcc.Graph(id='planting-times-plot'),
    ], style={'margin-bottom': '40px'}),
    
    # Weather Section
    html.Div([
        html.H2("Real-time Weather Data"),
        html.P("Temperature (°C):", style={'margin-bottom': '5px'}),
        html.Div(id='weather-output', style={'font-size': '20px'}),
    ]),
])

# Callbacks
@app.callback(
    [Output('crop-suggestions-plot', 'figure'),
     Output('planting-times-plot', 'figure'),
     Output('weather-output', 'children')],
    [Input('location-dropdown', 'value'),
     Input('land-input', 'value'),
     Input('microclimate-radio', 'value'),
     Input('crop-type-dropdown', 'value')]
)
def update_recommendations(selected_location, landholdings, microclimate, crop_types):
    # Simulated personalized recommendations
    crop_suggestion_score = random.uniform(5, 15) + landholdings * 0.2
    
    # Adjust planting times based on microclimate
    if microclimate == 'warm':
        planting_time = random.uniform(20, 30)
    elif microclimate == 'moderate':
        planting_time = random.uniform(25, 35)
    else:
        planting_time = random.uniform(30, 40)
    
    # Update crop suggestions plot
    crop_fig = px.bar(
        x=[selected_location],
        y=[crop_suggestion_score],
        labels={'y': 'Crop Suggestion Score'},
        title='Drought-Resistant Crop Suggestions',
    )

    # Update planting times plot
    planting_fig = px.bar(
        x=[selected_location],
        y=[planting_time],
        labels={'y': 'Optimal Planting Time (Days)'},
        title='Optimized Planting Times',
    )

    # Update weather output
    weather_output = f"{weather_data[selected_location]:.2f}°C"

    return crop_fig, planting_fig, weather_output

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)