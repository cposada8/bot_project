import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

import base64
import random
import json
import os

crops_path = "./images/crops/"
app = dash.Dash(__name__)

# the lis of all the possible images
image_names = os.listdir(crops_path)

image_filename = crops_path+'cropped_screenshot_100.png' 
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div(
    children=[
        html.Div([
            html.Div(
                [
                    html.P(
                            "Seleccione imagen",
                            className="control_label",
                        ),
                    dcc.Dropdown(
                                id="imgs-list",
                                options=[{'label': "{} - {}".format(i, name), 'value': name} for i, name in enumerate(image_names)],
                                # placeholder="Seleccione Compañía",
                        ),
                ],
                className="three columns",
            ),

            html.Div(
                [
                    # html.Img(src= app.get_asset_url(crops_path+"cropped_screenshot_1.png")), #src=crops_path+"cropped_screenshot_1.png")
                    html.Img(
                        id="img-viewer",
                        src='data:image/png;base64,{}'.format(encoded_image.decode())
                        )
                ],
                className="nine columns",
            ),
        ])
    ],
)

@app.callback(
    dash.dependencies.Output("img-viewer", "src"),
    [
        dash.dependencies.Input("imgs-list", "value"),
    ]
)
def update_viewer(img_name):
    if img_name is not None:
        image_filename = crops_path+img_name
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())
        return 'data:image/png;base64,{}'.format(encoded_image.decode())
    

if __name__ == "__main__":
    app.run_server(debug=True)
