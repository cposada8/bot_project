import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

from datetime import datetime
import base64
import random
import json
import os

import utils

crops_path = "./images/crops/"
database_path = "./databases/"
database_name = "database.csv"

save_every = 5 # parameter to control savings of the database

app = dash.Dash(__name__)
application = app.server
app.scripts.config.serve_locally = True


# global variables to keep track of them
global image_index
image_index = -1    # to keep track of the index images

global user_name
user_name = None
global image_name
image_name = None
global rank
rank = None

# read the database
global database
database = pd.read_csv(database_path + database_name, sep=";")

# the lis of all the possible images
image_names = os.listdir(crops_path)
# get rid of ranked images
image_names = list(set(image_names)-set(database["image_name"]))
image_names.sort()

def save_register_in_database():
    global database, image_name, user_name, rank

    now = datetime.now()
    now_str = now.strftime("%d/%m/%Y %H:%M:%S")

    data = {
        "image_name": [image_name],
        "user": [user_name],
        "rank": [rank],
        "date_str": [now_str]
    }

    register = pd.DataFrame(data, columns=["image_name", "user", "rank", "date_str"])

    database = database.append(register)
    print("the df is now:")
    print(database.shape)

    # saving the database
    if database.shape[0] % save_every == 0:
        print("...saving the database...")
        database.to_csv(database_path+database_name, sep=";", index=False)


app.layout = html.Div(
    children=[
        # hidden divs to store some variables
        html.Div(id='hidden1', style={'display': 'none'}),

        html.Div([
            html.Div(
                [
                    dcc.Input(
                        id="user-input",
                        placeholder="ingrese un usuario",
                    ),

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
                        id='rank-radio',
                        options=[{'label': i, 'value': i} for i in ['dislike', 'like', 'super like']],
                        value='Linear',
                        labelStyle={'display': 'inline-block'}
                    ),

                    html.Button('rank', id='rank-btn', style={"textAlignt": "center"}),
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
        # update global variables
        global image_index
        image_index = img_index
        global image_name
        image_name = image_names[image_index]

        img_name = image_name
        image_filename = crops_path+img_name
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())
        return 'data:image/png;base64,{}'.format(encoded_image.decode())


@app.callback(
    dash.dependencies.Output("hidden1", "children"),
    [
        dash.dependencies.Input("rank-radio", "value"),
        dash.dependencies.Input("user-input", "value"),  
    ]
)
def update_global_vars(rank_radio, user_input):
    global rank, user_name
    rank = rank_radio
    user_name = user_input



@app.callback(
    dash.dependencies.Output("imgs-list", "value"),
    [
        dash.dependencies.Input("rank-btn", "n_clicks"),
    ]
)
def update_img_list(n_clicks):

    # 1. save the register of actual image rank into database
    global image_name
    if image_name is not None:
        # save register in database
        save_register_in_database()

    if n_clicks is not None:
        global image_index
        new_index = (image_index + 1) % len(image_names)
        image_index = new_index

        return new_index


if __name__ == "__main__":
    app.run_server(debug=False, port=8000)
