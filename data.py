import streamlit as st

def data_app(df):
    st.title("View Data")

    with st.beta_expander("View Data"):
        st.table(df)

    st.header("Columns Summary:")

    if st.checkbox("Show Summary:"):
        st.table(df.describe())

    beta_col1,beta_col2,beta_col3 = st.beta_columns(3)   

    with beta_col1:
        if st.checkbox("Show columns name"):
            st.table(df.columns)     

    with beta_col2:
        if st.checkbox("View columns datatype"):
            dtypes_df = df.dtypes.apply(lambda x: x.name)
            st.table(dtypes_df)

    with beta_col3:
        if st.checkbox("View column data"):
            column_data = st.selectbox("Select column",tuple(df.columns))
            st.write(df[column_data])
                                 