import dash
from dash import html, dcc
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.express as px
import base64
import io


app = dash.Dash()
server=app.server

# create app layout
app.title="PBI Data Aggregation"
app.layout = html.Div([
    html.Div([
        html.H1("Power BI Data Aggregation Query Builder"),
        html.H3("Enter Previous Table Name:"),
        dcc.Input(id='previous_table_name', value="Pivoted Table"),
        html.H3("Enter Variable To Group By:"),
        dcc.Input(id='group_by_variable', value="ProjectID"),
        html.H3("Enter whether to keep First or Last value inputs:"),
        dcc.Dropdown([{'label':'First','value':'First'},{'label':'Last','value':'Last'}],value="Last",id="first_last",style={'width':'177px'})]),
    # html.Div([
    #     html.H3("Enter Relevant Column Names Below:"),
    #     dcc.Input(id='first_input_area', placeholder="First Variable"),
    #     dcc.Input(id='second_input_area', placeholder="Second Variable"),
    #     dcc.Input(id='third_input_area', placeholder="Third Variable"),
    #     dcc.Input(id='fourth_input_area', placeholder="Fourth Variable"),
    #     dcc.Input(id='fifth_input_area', placeholder="Fifth Variable"),
    #     dcc.Input(id='sixth_input_area', placeholder="Sixth Variable"),
    #     dcc.Input(id='seventh_input_area', placeholder="Seventh Variable"),
    #     dcc.Input(id='eigth_input_area', placeholder="Eigth Variable"),
    #     dcc.Input(id='ninth_input_area', placeholder="Ninth Variable"),
    #     dcc.Input(id='tenth_input_area', placeholder="Tenth Variable"),
    #     dcc.Input(id='eleventh_input_area', placeholder="Eleventh Variable"),
    #     dcc.Input(id='twelfth_input_area', placeholder="Twelfth Variable"),
    #     dcc.Input(id='thirteenth_input_area', placeholder="Thirteenth Variable"),
    #     dcc.Input(id='fourteenth_input_area', placeholder="Fourteenth Variable"),
    #     dcc.Input(id='fifteenth_input_area', placeholder="Fifteenth Variable"),
    #     dcc.Input(id='sixteenth_input_area', placeholder="Sixteenth Variable"),
    #     dcc.Input(id='seventeenth_input_area', placeholder="Seventeenth Variable"),
    #     dcc.Input(id='eighteenth_input_area', placeholder="Eighteenth Variable"),
    #     dcc.Input(id='nineteenth_input_area', placeholder="Nineteenth Variable"),
    #     dcc.Input(id='twentieth_input_area', placeholder="Twentieth Variable"),
    #     dcc.Input(id='twenty_first_input_area', placeholder="Twentyfirst Variable"),
    #     dcc.Input(id='twenty_second_input_area', placeholder="Twentysecond Variable"),
    #     dcc.Input(id='twenty_third_input_area', placeholder="Twentythird Variable"),
    #     dcc.Input(id='twenty_fourth_input_area', placeholder="Twentyfourth Variable"),
    #     dcc.Input(id='twenty_fifth_input_area', placeholder="Twentyfifth Variable"),
    #     dcc.Input(id='twenty_sixth_input_area', placeholder="Twentysixth Variable"),
    #     dcc.Input(id='twenty_seventh_input_area', placeholder="Twentyseventh Variable"),
    #     dcc.Input(id='twenty_eigth_input_area', placeholder="Twentyeigth Variable"),
    #     dcc.Input(id='twenty_ninth_input_area', placeholder="Twentyninth Variable"),
    #     dcc.Input(id='thirtieth_input_area', placeholder="Thirtieth Variable"),
    #     dcc.Input(id='thirty_first_input_area', placeholder="Thirtyfirst Variable"),
    #     dcc.Input(id='thirty_second_input_area', placeholder="Thirtysecond Variable"),
    #     dcc.Input(id='thirty_third_input_area', placeholder="Thirtythird Variable"),
    #     dcc.Input(id='thirty_fourth_input_area', placeholder="Thirtyfourth Variable"),
    #     dcc.Input(id='thirty_fifth_input_area', placeholder="Thirtyfifth Variable"),
    #     dcc.Input(id='thirty_sixth_input_area', placeholder="Thirtysixth Variable"),
    #     dcc.Input(id='thirty_seventh_input_area', placeholder="Thirtyseventh Variable"),
    #     dcc.Input(id='thirty_eigth_input_area', placeholder="Thirtyeigth Variable"),
    #     dcc.Input(id='thirty_ninth_input_area', placeholder="Thirtyninth Variable"),
    #     dcc.Input(id='fortieth_input_area', placeholder="Fortieth Variable"),
    #     dcc.Input(id='forty_first_input_area', placeholder="Fortyfirst Variable"),
    #     dcc.Input(id='forty_second_input_area', placeholder="Fortysecond Variable"),
    #     dcc.Input(id='forty_third_input_area', placeholder="Fortythird Variable"),
    #     dcc.Input(id='forty_fourth_input_area', placeholder="Fortyfourth Variable"),
    #     dcc.Input(id='forty_fifth_input_area', placeholder="Fortyfifth Variable"),
    #     dcc.Input(id='forty_sixth_input_area', placeholder="Fortysixth Variable"),
    #     dcc.Input(id='forty_seventh_input_area', placeholder="Fortyseventh Variable"),
    #     dcc.Input(id='forty_eigth_input_area', placeholder="Fortyeigth Variable"),
    #     dcc.Input(id='forty_ninth_input_area', placeholder="Fortyninth Variable"),
    #     dcc.Input(id='fiftieth_input_area', placeholder="Fiftieth Variable"),
    #     dcc.Input(id='fifty_first_input_area', placeholder="Fiftyfirst Variable"),
    #     dcc.Input(id='fifty_second_input_area', placeholder="Fiftysecond Variable"),
    #     dcc.Input(id='fifty_third_input_area', placeholder="Fiftythird Variable"),
    #     dcc.Input(id='fifty_fourth_input_area', placeholder="Fiftyfourth Variable"),
    #     dcc.Input(id='fifty_fifth_input_area', placeholder="Fiftyfifth Variable"),
    #     dcc.Input(id='fifty_sixth_input_area', placeholder="Fiftysixth Variable"),
    #     dcc.Input(id='fifty_seventh_input_area', placeholder="Fiftyseventh Variable"),
    #     dcc.Input(id='fifty_eigth_input_area', placeholder="Fiftyeigth Variable"),
    #     dcc.Input(id='fifty_ninth_input_area', placeholder="Fiftyninth Variable"),
    #     dcc.Input(id='sixtieth_input_area', placeholder="Sixtieth Variable")
    # ]),
    # html.Div([
    #     html.H2("Final Query Result:"),
    #     html.H3(id="final_output_string", children='No input yet')

    # ]),
    html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.H2("Final Query Result:"),
    html.Div(id='output-data-upload'),
    ])
])

def parse_contents(contents, prev_table,group_by_table,first_last,filename):
    content_type, content_string = contents.split(',')
    print(prev_table,group_by_table,first_last)
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    first_part_of_query = '=Table.Group(#\"'+prev_table+'", {"'+group_by_table+'"},{'
    column_list_string_query = ''
    df2=df.to_dict()
    column_name = list(df2.keys())[0]
    for row in range(len(df)):
        if row>=0:
            datum = df2[column_name][row]
            column_list_string_query+='{"'+datum+'", each List.'+first_last+'(List.RemoveNulls(['+datum+']))},'
    column_list_string_query=first_part_of_query+column_list_string_query[:-1]+'})'

    return html.Div([
        html.P(column_list_string_query),
        html.Hr()
    ])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              [Input('previous_table_name', 'value')],
              [Input('group_by_variable', 'value')],
              [Input('first_last', 'value')],
              State('upload-data', 'filename'),
              )
def update_output(list_of_contents, prev_table,group_by_table,first_last,list_of_names):
    if list_of_contents is not None:
        
        children = [
            parse_contents(c,prev_table,group_by_table,first_last, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children

if __name__=="__main__":
    app.run_server()





# @app.callback(Output('final_output_string','children'),
#                 [Input('previous_table_name', 'value')],
#                 [Input('group_by_variable', 'value')],
#                 [Input('first_last', 'value')],
#                 [Input('first_input_area', 'value')],
#                 [Input('second_input_area', 'value')],
#                 [Input('third_input_area', 'value')],
#                 [Input('fourth_input_area', 'value')],
#                 [Input('fifth_input_area', 'value')],
#                 [Input('sixth_input_area', 'value')],
#                 [Input('seventh_input_area', 'value')],
#                 [Input('eigth_input_area', 'value')],
#                 [Input('ninth_input_area', 'value')],
#                 [Input('tenth_input_area', 'value')],
#                 [Input('eleventh_input_area', 'value')],
#                 [Input('twelfth_input_area', 'value')],
#                 [Input('thirteenth_input_area', 'value')],
#                 [Input('fourteenth_input_area', 'value')],
#                 [Input('fifteenth_input_area', 'value')],
#                 [Input('sixteenth_input_area', 'value')],
#                 [Input('seventeenth_input_area', 'value')],
#                 [Input('eighteenth_input_area', 'value')],
#                 [Input('nineteenth_input_area', 'value')],
#                 [Input('twentieth_input_area', 'value')],
#                 [Input('twenty_first_input_area', 'value')],
#                 [Input('twenty_second_input_area', 'value')],
#                 [Input('twenty_third_input_area', 'value')],
#                 [Input('twenty_fourth_input_area', 'value')],
#                 [Input('twenty_fifth_input_area', 'value')],
#                 [Input('twenty_sixth_input_area', 'value')],
#                 [Input('twenty_seventh_input_area', 'value')],
#                 [Input('twenty_eigth_input_area', 'value')],
#                 [Input('twenty_ninth_input_area', 'value')],
#                 [Input('thirtieth_input_area', 'value')],
#                 [Input('thirty_first_input_area', 'value')],
#                 [Input('thirty_second_input_area', 'value')],
#                 [Input('thirty_third_input_area', 'value')],
#                 [Input('thirty_fourth_input_area', 'value')],
#                 [Input('thirty_fifth_input_area', 'value')],
#                 [Input('thirty_sixth_input_area', 'value')],
#                 [Input('thirty_seventh_input_area', 'value')],
#                 [Input('thirty_eigth_input_area', 'value')],
#                 [Input('thirty_ninth_input_area', 'value')],
#                 [Input('fortieth_input_area', 'value')],
#                 [Input('forty_first_input_area', 'value')],
#                 [Input('forty_second_input_area', 'value')],
#                 [Input('forty_third_input_area', 'value')],
#                 [Input('forty_fourth_input_area', 'value')],
#                 [Input('forty_fifth_input_area', 'value')],
#                 [Input('forty_sixth_input_area', 'value')],
#                 [Input('forty_seventh_input_area', 'value')],
#                 [Input('forty_eigth_input_area', 'value')],
#                 [Input('forty_ninth_input_area', 'value')],
#                 [Input('fiftieth_input_area', 'value')],
#                 [Input('fifty_first_input_area', 'value')],
#                 [Input('fifty_second_input_area', 'value')],
#                 [Input('fifty_third_input_area', 'value')],
#                 [Input('fifty_fourth_input_area', 'value')],
#                 [Input('fifty_fifth_input_area', 'value')],
#                 [Input('fifty_sixth_input_area', 'value')],
#                 [Input('fifty_seventh_input_area', 'value')],
#                 [Input('fifty_eigth_input_area', 'value')],
#                 [Input('fifty_ninth_input_area', 'value')],
#                 [Input('sixtieth_input_area', 'value')],
#                 )
# def update_final_string(previous_table_name,
#                         group_by_variable,
#                         first_last,
#                         first_input_area,
#                         second_input_area,
#                         third_input_area,
#                         fourth_input_area,
#                         fifth_input_area,
#                         sixth_input_area,
#                         seventh_input_area,
#                         eigth_input_area,
#                         ninth_input_area,
#                         tenth_input_area,
#                         eleventh_input_area,
#                         twelfth_input_area,
#                         thirteenth_input_area,
#                         fourteenth_input_area,
#                         fifteenth_input_area,
#                         sixteenth_input_area,
#                         seventeenth_input_area,
#                         eighteenth_input_area,
#                         nineteenth_input_area,
#                         twentieth_input_area,
#                         twenty_first_input_area,
#                         twenty_second_input_area,
#                         twenty_third_input_area,
#                         twenty_fourth_input_area,
#                         twenty_fifth_input_area,
#                         twenty_sixth_input_area,
#                         twenty_seventh_input_area,
#                         twenty_eigth_input_area,
#                         twenty_ninth_input_area,
#                         thirtieth_input_area,
#                         thirty_first_input_area,
#                         thirty_second_input_area,
#                         thirty_third_input_area,
#                         thirty_fourth_input_area,
#                         thirty_fifth_input_area,
#                         thirty_sixth_input_area,
#                         thirty_seventh_input_area,
#                         thirty_eigth_input_area,
#                         thirty_ninth_input_area,
#                         fortieth_input_area,
#                         forty_first_input_area,
#                         forty_second_input_area,
#                         forty_third_input_area,
#                         forty_fourth_input_area,
#                         forty_fifth_input_area,
#                         forty_sixth_input_area,
#                         forty_seventh_input_area,
#                         forty_eigth_input_area,
#                         forty_ninth_input_area,
#                         fiftieth_input_area,
#                         fifty_first_input_area,
#                         fifty_second_input_area,
#                         fifty_third_input_area,
#                         fifty_fourth_input_area,
#                         fifty_fifth_input_area,
#                         fifty_sixth_input_area,
#                         fifty_seventh_input_area,
#                         fifty_eigth_input_area,
#                         fifty_ninth_input_area,
#                         sixtieth_input_area
#                         ):
#     first_part = '=Table.Group(#\"'+previous_table_name+'", {"'+group_by_variable+'"},{'
#     data=[first_input_area,
#           second_input_area,
#           third_input_area,
#           fourth_input_area,
#           fifth_input_area,
#           sixth_input_area,
#           seventh_input_area,
#           eigth_input_area,
#           ninth_input_area,
#           tenth_input_area,
#           eleventh_input_area,
#           twelfth_input_area,
#           thirteenth_input_area,
#           fourteenth_input_area,
#           fifteenth_input_area,
#           sixteenth_input_area,
#           seventeenth_input_area,
#           eighteenth_input_area,
#           nineteenth_input_area,
#           twentieth_input_area,
#           twenty_first_input_area,
#           twenty_second_input_area,
#           twenty_third_input_area,
#           twenty_fourth_input_area,
#           twenty_fifth_input_area,
#           twenty_sixth_input_area,
#           twenty_seventh_input_area,
#           twenty_eigth_input_area,
#           twenty_ninth_input_area,
#           thirtieth_input_area,
#           thirty_first_input_area,
#           thirty_second_input_area,
#           thirty_third_input_area,
#           thirty_fourth_input_area,
#           thirty_fifth_input_area,
#           thirty_sixth_input_area,
#           thirty_seventh_input_area,
#           thirty_eigth_input_area,
#           thirty_ninth_input_area,
#           fortieth_input_area,
#           forty_first_input_area,
#           forty_second_input_area,
#           forty_third_input_area,
#           forty_fourth_input_area,
#           forty_fifth_input_area,
#           forty_sixth_input_area,
#           forty_seventh_input_area,
#           forty_eigth_input_area,
#           forty_ninth_input_area,
#           fiftieth_input_area,
#           fifty_first_input_area,
#           fifty_second_input_area,
#           fifty_third_input_area,
#           fifty_fourth_input_area,
#           fifty_fifth_input_area,
#           fifty_sixth_input_area,
#           fifty_seventh_input_area,
#           fifty_eigth_input_area,
#           fifty_ninth_input_area,
#           sixtieth_input_area
#           ]
#     col_list_string = ''
#     for datum in data:
#         if datum:
#             col_list_string+='{"'+datum+'", each List.'+first_last+'(List.RemoveNulls(['+datum+']))},'
#     col_list_string=col_list_string[:-1]
#     return first_part+col_list_string+'})'