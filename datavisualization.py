print("data visulization-------")
from data_cleaning import data_cleaning
from feature_engineering import feature_eng
import pandas as pd
import plotly.express as px
# from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
import io
from PIL import Image
a =[]
def data_visualization():
    dataset = feature_eng()
    col=list(dataset.columns)
    col.remove("isFraud")
    print(col)
    for i in col:
        fig = px.box(dataset, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}.jpg")
        # a.append(fig)

    for i in col:
        fig = px.histogram(dataset, y=i, marginal="box")
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        # fig.show()
        fig.write_image(f"{i}_hist.jpg")
        # a.append(fig)
        
    # for i in col:
    #     fig = ff.create_distplot(dataset, y=i, marginal="box")
    #     fig.update_layout(template='plotly_dark')
    #     fig.update_xaxes(showgrid=False, zeroline=False)
    #     fig.update_yaxes(showgrid=False, zeroline=False)
    #     # fig.show()
    #     fig.write_image(f"{i}_displot.jpg")
    #     # a.append(fig)
    
    df=dataset.drop("isFraud",axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("img.jpg")
    # a.append(fig)
    
    return dataset

data_visualization()
