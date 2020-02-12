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
global image_index
image_index = -1    # to keep track of the index images


app.layout = html.Div(
    children=[
        # hidden divs to store some variables
        html.Div(id='img-index', style={'display': 'none'}),

        html.Div([
            html.Div(
                [
                    html.P(
                            "Seleccione imagen",
                            className="control_label",
                        ),
                    dcc.Dropdown(
                                id="imgs-list",
                                options=[{'label': name, 'value': i} for i, name in enumerate(image_names)],
                                # placeholder="Seleccione Compañía",
                        ),

                    dcc.RadioItems(
                        id='yaxis-type',
                        options=[{'label': i, 'value': i} for i in ['dislike', 'like', 'super like']],
                        value='Linear',
                        labelStyle={'display': 'inline-block'}
                    ),

                    html.Button('next', id='next-btn', style={"textAlignt": "center"}),
                ],
                className="three columns",
                style={
                    'textAlign': 'center',
                },
            ),

            html.Div(
                [
                    html.Img(
                        id="img-viewer",
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
def update_viewer(img_index):
    if img_index is not None:
        global image_index
        image_index = img_index

        img_name = image_names[image_index]
        print(image_index, " ->image name is:", img_name)
        image_filename = crops_path+img_name
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())
        return 'data:image/png;base64,{}'.format(encoded_image.decode())


@app.callback(
    dash.dependencies.Output("imgs-list", "value"),
    [
        dash.dependencies.Input("next-btn", "n_clicks"),
    ]
)
def update_img_list(n_clicks):
    if n_clicks is not None:
        global image_index
        new_index = (image_index + 1) % len(image_names)
        image_index = new_index

        return new_index


if __name__ == "__main__":
    app.run_server(debug=True)
