import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plots_app(df):

    # st.set_option("depreciation.showPyplotGlobalUse",False)
    st.title("Visualise Data")
    st.header("Scatterplot")

    feature_list = st.multiselect("Select x-axis values:",("carwidth",'enginesize',"horsepower","drivewheel_fwd","car_company_buick"))

    for feature in feature_list:
        fig = plt.figure(figsize = (12,5))
        st.subheader(f"Scatter plot between {feature} and price ")
        sns.scatterplot(x='price',y=feature, data = df)
        st.pyplot(fig)

    st.header("Visualisation Selector")
    plot_type = st.multiselect("Select charts or plots:",("Histogram",'Box plot', 'Correlation Heatmap'))

    if("Histogram" in plot_type):
        st.subheader("Histogram")
        hist_column = st.selectbox("Select the column to create its histogram",("carwidth",'enginesize',"horsepower"))
        fig = plt.figure(figsize = (12,5))
        plt.title(f"Histogram for {hist_column}")
        plt.hist(x = df[hist_column],bins = 'sturges',edgecolor = "black" )
        st.pyplot(fig)

    if("Box Plot" in plot_type):
        st.subheader("Box Plot")
        box_column = st.selectbox("Select the column to create its histogram",("carwidth",'enginesize',"horsepower"))
        fig = plt.figure(figsize = (12,5))
        plt.title(f"Box Plot for {box_column}")
        sns.boxplot(df[box_column])
        st.pyplot(fig)  

    if("Correlation Heatmap" in plot_type):
        st.subheader("Correlation Heatmap")
        fig = plt.figure(figsize = (12,10))
        ax = sns.heatmap(df.corr(),annot = True)
        bottom,top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5,top - 0.5)
        st.pyplot(fig)        
