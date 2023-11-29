print("data visualization--------------------")

import numpy as np
from data_cleaning import data_cleaning
from feature_engineering import feature_eng
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
import io
import plotly.express as px
from PIL import Image
import seaborn as sns
import matplotlib as plt

categ = []
numer = []
a = []

def data_visu():
    data = data_cleaning()
    
    for col in data.columns:
        if data[col].dtypes == object:
            categ.append(col)
        else:
            numer.append(col)

    # print("categ-----------", categ)
    # print("numer------------", numer)

    # data_num = data[numer]
    # data_num_corr = data_num.corr()
    # fig = go.Figure()
    # fig.add_trace(
    #     go.Heatmap(
    #         x = data_num_corr.columns,
    #         y = data_num_corr.index,
    #         z = np.array(data_num_corr),
    #         text=data_num_corr.values,
    #         texttemplate='%{text:.2f}',
            
    #     )
    # )
    # fig.update_layout(template='plotly_dark')
    # fig.update_xaxes(showgrid=False)
    # fig.update_yaxes(showgrid=False)
    # a.append(fig)
    # fig.show()

    dataset = feature_eng()
    columns = ['isFraud', 'newbalanceDest', 'oldbalanceOrg', 'newbalanceOrig', 'amount', 'type']
    subset_df = dataset[columns]
    data_num_corr = subset_df.corr()
    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
            x = data_num_corr.columns,
            y = data_num_corr.index,
            z = np.array(data_num_corr),
            text=data_num_corr.values,
            texttemplate='%{text:.2f}',
            
        )
    )
    fig.update_layout(template='plotly_dark')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    a.append(fig)
    # fig.show()

    for numerical_feature in numer:
        fig = px.box(data, y=numerical_feature)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False,zeroline=True,zerolinewidth=4)
        a.append(fig)
        # fig.show()

    for numerical_feature in numer:
        fig = ff.create_distplot([data[numerical_feature]], [numerical_feature], show_rug=False)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(title_text=numerical_feature, showgrid=False)
        fig.update_yaxes(showgrid=False)
        a.append(fig)
        # fig.show()
    
    for categorical_feature in categ:
        fig = px.histogram(data, x=categorical_feature)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        a.append(fig)
        # fig.show()

    figures = a
    image_list = [pio.to_image(fig, format='png', width=1440, height=900, scale=1.5) for fig in figures]
    for index, image in enumerate(image_list):
        with io.BytesIO() as tmp:
            tmp.write(image)  # write the image bytes to the io.BytesIO() temporary object
            image = Image.open(tmp).convert('RGB')  # convert and overwrite 'image' to prevent creating a new variable
            image_list[index] = image  # overwrite byte image data in list, replace with PIL converted image data
    
    # pop first item from image_list, use that to access .save(). Then refer back to image_list to append the rest
    image_list.pop(0).save(r'./Health_care_usecase#615.pdf', 'PDF',
                    save_all=True, append_images=image_list, resolution=100.0)
    

    return data

data_visu()