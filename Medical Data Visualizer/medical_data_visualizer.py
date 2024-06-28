import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (((df.weight*10000)/(df.height.pow(2))) > 25).astype('int64')

# 3
df["cholesterol"] = (df["cholesterol"]>1).astype('int64')
df["gluc"] = (df["gluc"]>1).astype('int64')

# 4
def draw_cat_plot():
    
    df_cat = pd.melt(df,id_vars="cardio",value_vars=["active","alco","cholesterol","gluc","overweight","smoke"])


    # 6
    #df_cat = None
    

    # 7



    # 8
    fig = sns.catplot(data=df_cat,x="variable",hue="value",col="cardio",kind="count").set_axis_labels(x_var="variable",y_var="total").fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)) ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(10,8),dpi=250) 

    # 15
    ax = sns.heatmap(corr,linewidth=1,center=0.0,vmin=-0.16,vmax=0.32,mask=mask,annot=True,fmt=".1f",cbar_kws={'shrink':0.4,'format':'%.2f'})


    # 16
    fig.savefig('heatmap.png')
    return fig
