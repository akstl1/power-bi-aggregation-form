import webbrowser
import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import requests
import plotly.express as px

app = dash.Dash()
server=app.server

# create app layout

app.layout = html.Div([
    html.Div([
        html.H1("Power BI Data Aggregation Query Builder"),
        html.H3("Enter Previous Table Name:"),
        dcc.Input(id='previous_table_name', value="Pivoted Table"),
        html.H3("Enter Variable To Group By:"),
        dcc.Input(id='group_by_variable', value="ProjectID"),
        html.H3("Enter First or Last:"),
        dcc.Dropdown([{'label':'First','value':'First'},{'label':'Last','value':'Last'}],value="Last",id="first_last")

    ],style={'width':'177px'}),
    html.Div([
        html.H3("Enter Relevant Column Names Below:"),
        dcc.Input(id='first_input_area', placeholder="First Variable"),
        dcc.Input(id='second_input_area', placeholder="Second Variable"),
        dcc.Input(id='third_input_area', placeholder="Third Variable"),
        dcc.Input(id='fourth_input_area', placeholder="Fourth Variable"),
        dcc.Input(id='fifth_input_area', placeholder="Fifth Variable"),
        dcc.Input(id='sixth_input_area', placeholder="Sixth Variable"),
        dcc.Input(id='seventh_input_area', placeholder="Seventh Variable"),
        dcc.Input(id='eigth_input_area', placeholder="Eigth Variable"),
        dcc.Input(id='ninth_input_area', placeholder="Ninth Variable"),
        dcc.Input(id='tenth_input_area', placeholder="Tenth Variable"),
        dcc.Input(id='eleventh_input_area', placeholder="Eleventh Variable"),
        dcc.Input(id='twelfth_input_area', placeholder="Twelfth Variable"),
        dcc.Input(id='thirteenth_input_area', placeholder="Thirteenth Variable"),
        dcc.Input(id='fourteenth_input_area', placeholder="Fourteenth Variable"),
        dcc.Input(id='fifteenth_input_area', placeholder="Fifteenth Variable"),
        dcc.Input(id='sixteenth_input_area', placeholder="Sixteenth Variable"),
        dcc.Input(id='seventeenth_input_area', placeholder="Seventeenth Variable"),
        dcc.Input(id='eighteenth_input_area', placeholder="Eighteenth Variable"),
        dcc.Input(id='nineteenth_input_area', placeholder="Nineteenth Variable"),
        dcc.Input(id='twentieth_input_area', placeholder="Twentieth Variable"),
        dcc.Input(id='twenty_first_input_area', placeholder="Twentyfirst Variable"),
        dcc.Input(id='twenty_second_input_area', placeholder="Twentysecond Variable"),
        dcc.Input(id='twenty_third_input_area', placeholder="Twentythird Variable"),
        dcc.Input(id='twenty_fourth_input_area', placeholder="Twentyfourth Variable"),
        dcc.Input(id='twenty_fifth_input_area', placeholder="Twentyfifth Variable"),
        dcc.Input(id='twenty_sixth_input_area', placeholder="Twentysixth Variable"),
        dcc.Input(id='twenty_seventh_input_area', placeholder="Twentyseventh Variable"),
        dcc.Input(id='twenty_eigth_input_area', placeholder="Twentyeigth Variable"),
        dcc.Input(id='twenty_ninth_input_area', placeholder="Twentyninth Variable"),
        dcc.Input(id='thirtieth_input_area', placeholder="Thirtieth Variable"),
        dcc.Input(id='thirty_first_input_area', placeholder="Thirtyfirst Variable"),
        dcc.Input(id='thirty_second_input_area', placeholder="Thirtysecond Variable"),
        dcc.Input(id='thirty_third_input_area', placeholder="Thirtythird Variable"),
        dcc.Input(id='thirty_fourth_input_area', placeholder="Thirtyfourth Variable"),
        dcc.Input(id='thirty_fifth_input_area', placeholder="Thirtyfifth Variable"),
        dcc.Input(id='thirty_sixth_input_area', placeholder="Thirtysixth Variable"),
        dcc.Input(id='thirty_seventh_input_area', placeholder="Thirtyseventh Variable"),
        dcc.Input(id='thirty_eigth_input_area', placeholder="Thirtyeigth Variable"),
        dcc.Input(id='thirty_ninth_input_area', placeholder="Thirtyninth Variable"),
        dcc.Input(id='fortieth_input_area', placeholder="Fortieth Variable"),
        dcc.Input(id='forty_first_input_area', placeholder="Fortyfirst Variable"),
        dcc.Input(id='forty_second_input_area', placeholder="Fortysecond Variable"),
        dcc.Input(id='forty_third_input_area', placeholder="Fortythird Variable"),
        dcc.Input(id='forty_fourth_input_area', placeholder="Fortyfourth Variable"),
        dcc.Input(id='forty_fifth_input_area', placeholder="Fortyfifth Variable"),
        dcc.Input(id='forty_sixth_input_area', placeholder="Fortysixth Variable"),
        dcc.Input(id='forty_seventh_input_area', placeholder="Fortyseventh Variable"),
        dcc.Input(id='forty_eigth_input_area', placeholder="Fortyeigth Variable"),
        dcc.Input(id='forty_ninth_input_area', placeholder="Fortyninth Variable"),
        dcc.Input(id='fiftieth_input_area', placeholder="Fiftieth Variable"),
        dcc.Input(id='fifty_first_input_area', placeholder="Fiftyfirst Variable"),
        dcc.Input(id='fifty_second_input_area', placeholder="Fiftysecond Variable"),
        dcc.Input(id='fifty_third_input_area', placeholder="Fiftythird Variable"),
        dcc.Input(id='fifty_fourth_input_area', placeholder="Fiftyfourth Variable"),
        dcc.Input(id='fifty_fifth_input_area', placeholder="Fiftyfifth Variable"),
        dcc.Input(id='fifty_sixth_input_area', placeholder="Fiftysixth Variable"),
        dcc.Input(id='fifty_seventh_input_area', placeholder="Fiftyseventh Variable"),
        dcc.Input(id='fifty_eigth_input_area', placeholder="Fiftyeigth Variable"),
        dcc.Input(id='fifty_ninth_input_area', placeholder="Fiftyninth Variable"),
        dcc.Input(id='sixtieth_input_area', placeholder="Sixtieth Variable")
    ]),
    html.Div([
        html.H2("Final Query Result:"),
        html.H3(id="final_output_string", children='No input yet')

    ])


])

@app.callback(Output('final_output_string','children'),
                [Input('previous_table_name', 'value')],
                [Input('group_by_variable', 'value')],
                [Input('first_last', 'value')],
                [Input('first_input_area', 'value')],
                [Input('second_input_area', 'value')],
                [Input('third_input_area', 'value')],
                [Input('fourth_input_area', 'value')],
                [Input('fifth_input_area', 'value')],
                [Input('sixth_input_area', 'value')],
                [Input('seventh_input_area', 'value')],
                [Input('eigth_input_area', 'value')],
                [Input('ninth_input_area', 'value')],
                [Input('tenth_input_area', 'value')],
                [Input('eleventh_input_area', 'value')],
                [Input('twelfth_input_area', 'value')],
                [Input('thirteenth_input_area', 'value')],
                [Input('fourteenth_input_area', 'value')],
                [Input('fifteenth_input_area', 'value')],
                [Input('sixteenth_input_area', 'value')],
                [Input('seventeenth_input_area', 'value')],
                [Input('eighteenth_input_area', 'value')],
                [Input('nineteenth_input_area', 'value')],
                [Input('twentieth_input_area', 'value')],
                [Input('twenty_first_input_area', 'value')],
                [Input('twenty_second_input_area', 'value')],
                [Input('twenty_third_input_area', 'value')],
                [Input('twenty_fourth_input_area', 'value')],
                [Input('twenty_fifth_input_area', 'value')],
                [Input('twenty_sixth_input_area', 'value')],
                [Input('twenty_seventh_input_area', 'value')],
                [Input('twenty_eigth_input_area', 'value')],
                [Input('twenty_ninth_input_area', 'value')],
                [Input('thirtieth_input_area', 'value')],
                [Input('thirty_first_input_area', 'value')],
                [Input('thirty_second_input_area', 'value')],
                [Input('thirty_third_input_area', 'value')],
                [Input('thirty_fourth_input_area', 'value')],
                [Input('thirty_fifth_input_area', 'value')],
                [Input('thirty_sixth_input_area', 'value')],
                [Input('thirty_seventh_input_area', 'value')],
                [Input('thirty_eigth_input_area', 'value')],
                [Input('thirty_ninth_input_area', 'value')],
                [Input('fortieth_input_area', 'value')],
                [Input('forty_first_input_area', 'value')],
                [Input('forty_second_input_area', 'value')],
                [Input('forty_third_input_area', 'value')],
                [Input('forty_fourth_input_area', 'value')],
                [Input('forty_fifth_input_area', 'value')],
                [Input('forty_sixth_input_area', 'value')],
                [Input('forty_seventh_input_area', 'value')],
                [Input('forty_eigth_input_area', 'value')],
                [Input('forty_ninth_input_area', 'value')],
                [Input('fiftieth_input_area', 'value')],
                [Input('fifty_first_input_area', 'value')],
                [Input('fifty_second_input_area', 'value')],
                [Input('fifty_third_input_area', 'value')],
                [Input('fifty_fourth_input_area', 'value')],
                [Input('fifty_fifth_input_area', 'value')],
                [Input('fifty_sixth_input_area', 'value')],
                [Input('fifty_seventh_input_area', 'value')],
                [Input('fifty_eigth_input_area', 'value')],
                [Input('fifty_ninth_input_area', 'value')],
                [Input('sixtieth_input_area', 'value')],
                )
def update_final_string(previous_table_name,
                        group_by_variable,
                        first_last,
                        first_input_area,
                        second_input_area,
                        third_input_area,
                        fourth_input_area,
                        fifth_input_area,
                        sixth_input_area,
                        seventh_input_area,
                        eigth_input_area,
                        ninth_input_area,
                        tenth_input_area,
                        eleventh_input_area,
                        twelfth_input_area,
                        thirteenth_input_area,
                        fourteenth_input_area,
                        fifteenth_input_area,
                        sixteenth_input_area,
                        seventeenth_input_area,
                        eighteenth_input_area,
                        nineteenth_input_area,
                        twentieth_input_area,
                        twenty_first_input_area,
                        twenty_second_input_area,
                        twenty_third_input_area,
                        twenty_fourth_input_area,
                        twenty_fifth_input_area,
                        twenty_sixth_input_area,
                        twenty_seventh_input_area,
                        twenty_eigth_input_area,
                        twenty_ninth_input_area,
                        thirtieth_input_area,
                        thirty_first_input_area,
                        thirty_second_input_area,
                        thirty_third_input_area,
                        thirty_fourth_input_area,
                        thirty_fifth_input_area,
                        thirty_sixth_input_area,
                        thirty_seventh_input_area,
                        thirty_eigth_input_area,
                        thirty_ninth_input_area,
                        fortieth_input_area,
                        forty_first_input_area,
                        forty_second_input_area,
                        forty_third_input_area,
                        forty_fourth_input_area,
                        forty_fifth_input_area,
                        forty_sixth_input_area,
                        forty_seventh_input_area,
                        forty_eigth_input_area,
                        forty_ninth_input_area,
                        fiftieth_input_area,
                        fifty_first_input_area,
                        fifty_second_input_area,
                        fifty_third_input_area,
                        fifty_fourth_input_area,
                        fifty_fifth_input_area,
                        fifty_sixth_input_area,
                        fifty_seventh_input_area,
                        fifty_eigth_input_area,
                        fifty_ninth_input_area,
                        sixtieth_input_area
                        ):
    first_part = '=Table.Group(#\"'+previous_table_name+'", {"'+group_by_variable+'"},{'
    data=[first_input_area,
          second_input_area,
          third_input_area,
          fourth_input_area,
          fifth_input_area,
          sixth_input_area,
          seventh_input_area,
          eigth_input_area,
          ninth_input_area,
          tenth_input_area,
          eleventh_input_area,
          twelfth_input_area,
          thirteenth_input_area,
          fourteenth_input_area,
          fifteenth_input_area,
          sixteenth_input_area,
          seventeenth_input_area,
          eighteenth_input_area,
          nineteenth_input_area,
          twentieth_input_area,
          twenty_first_input_area,
          twenty_second_input_area,
          twenty_third_input_area,
          twenty_fourth_input_area,
          twenty_fifth_input_area,
          twenty_sixth_input_area,
          twenty_seventh_input_area,
          twenty_eigth_input_area,
          twenty_ninth_input_area,
          thirtieth_input_area,
          thirty_first_input_area,
          thirty_second_input_area,
          thirty_third_input_area,
          thirty_fourth_input_area,
          thirty_fifth_input_area,
          thirty_sixth_input_area,
          thirty_seventh_input_area,
          thirty_eigth_input_area,
          thirty_ninth_input_area,
          fortieth_input_area,
          forty_first_input_area,
          forty_second_input_area,
          forty_third_input_area,
          forty_fourth_input_area,
          forty_fifth_input_area,
          forty_sixth_input_area,
          forty_seventh_input_area,
          forty_eigth_input_area,
          forty_ninth_input_area,
          fiftieth_input_area,
          fifty_first_input_area,
          fifty_second_input_area,
          fifty_third_input_area,
          fifty_fourth_input_area,
          fifty_fifth_input_area,
          fifty_sixth_input_area,
          fifty_seventh_input_area,
          fifty_eigth_input_area,
          fifty_ninth_input_area,
          sixtieth_input_area
          ]
    col_list_string = ''
    for datum in data:
        if datum:
            col_list_string+='{"'+datum+'", each List.'+first_last+'(List.RemoveNulls(['+datum+']))},'
    col_list_string=col_list_string[:-1]
    return first_part+col_list_string+'})'

# app.layout = html.Div([
#     html.Div([
#                 html.Hr(),
#                 html.Div([dcc.Dropdown(id='pokemon-name',options=[{'label':i.capitalize(),'value':i} for i in poke_names_list], value='bulbasaur')],style={'width':'20%', 'margin-left':'auto','margin-right':'auto'}),
#                 html.Div([html.H1(id='pokemon-name-id')], style={'text-align':'center'}),
#                 html.Div([
#                     html.Div([html.Img(id="pokemon-sprite")],style={'display':'inline-block', 'width':'20%','height':'300px', 'margin-right':'60px','margin-left':'80px', 'text-align':'center','vertical-align':'top' }),
#                     html.Div([
#                         html.Div([html.P(id='pokemon-description'),
#                         html.Div([
#                             html.Div([html.P(id='pokemon-height')]),
#                             html.Div([html.P(id='pokemon-weight')])
#                             ])
#                             ]),
#                             html.P(id='pokemon-ability'),
#                             html.P(id='pokemon-type')], style={'display':'inline-block', 'width':'30%','height':'300px','background-color':'#30a7d7', 'vertical-align':'top', 'padding-left':'10px','padding-right':'10px', 'border-radius':'10px'}),
#                             html.Div([dcc.Graph(id='graph')], style={'display':'inline-block','width':'30%', 'margin-left':'40px'})
#
#                     ], style={'height':'300px'})
#
#
# ])
# ], style={'background-color':'LightCyan', 'padding-bottom':'275px'})

#create callback to get pokemon stats for above elements

# @app.callback(Output('pokemon-name-id','children'),
#               Output('pokemon-description','children'),
#               Output('pokemon-ability','children'),
#               Output('pokemon-type','children'),
#               Output('pokemon-height','children'),
#               Output('pokemon-weight','children'),
#               Output('pokemon-sprite','src'),
#               Output('pokemon-sprite','style'),
#                 [Input('pokemon-name', 'value')])


# def name_and_id(poke_input):
#
#     ## Pokemon Species Data Request
#     pokemon_species_request = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(poke_input)+"/")
#     species_data = pokemon_species_request.json()
#
#     ## Pokemon  Table Data Request
#     pokemon_request = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(poke_input)+"/")
#     pokemon_data = pokemon_request.json()
#
#     ## Name And Id callback_
#     name=species_data['name'].capitalize()
#     id=str(species_data['id'])
#     while len(id)<3:
#         id='0'+id
#
#     ## Description callback
#     entry=species_data['flavor_text_entries'][0]['flavor_text'].replace('\x0c',' ')
#
#     ## Ability Data
#     abilities_json=pokemon_data['abilities']
#     abilities = []
#     for ability in abilities_json:
#         abilities.append(ability['ability']['name'].capitalize())
#
#     ## Types Data
#     types_json=pokemon_data['types']
#     types = []
#     for type in types_json:
#         types.append(type['type']['name'].capitalize())
#
#     ## Height Data
#     height=pokemon_data['height']/10
#
#     ## Weight Data
#     weight=pokemon_data['height']/10
#
#     ## Sprite Data_
#     id=str(species_data['id'])
#
#     ## return statement
#     return "{} #{}".format(name, id),"Description: {}".format(entry),"Abilities: "+', '.join(abilities),"Types: "+', '.join(types),"Height: {} m".format(height),"Weight: {} kg".format(weight),"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/"+id+".png", {'width':'275px', 'text-align':'center'}


if __name__=="__main__":
    app.run_server()
