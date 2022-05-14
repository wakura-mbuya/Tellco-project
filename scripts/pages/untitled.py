#load the data to be used
@st.cache()
def load_data(filename):
    data = pd.read_csv(filename)
    return data
    

#create the containers on the page
header = st.container()
handset_types = st.container()
manufacturers=st.container()
handset_manufacturers = st.container()
visualization = st.container()

data_df=load_data('../data/user_overview.csv')
user_info= load_data('../data/user_app_usage.csv')




with header:
    st.title("User Overview Analysis")
    
    
with handset_types:
    st.header("Top 10 handset used by customers")
    df=data_df['Handset Type'].value_counts().reset_index(name="count")
    df.columns = ['Handset Type', 'Total Handsets']
    st.write(df.head(10))
    
with manufacturers:
    st.header("Top 3 handset manufacturers")
    df=data_df['Handset Manufacturer'].value_counts().reset_index(name="count")
    df.columns = ['Handset Manufacturer', 'Total Handsets']
    st.write(df.head(3))
    
    
with handset_manufacturers:
    st.header("Top 5 handsets by top 3 handset manufacturers")
    
    #Group the data we have based on Handset Manufacturers and obtain the top 5 handset types for the top 3 handsets
    manufacturer_group =  data_df.groupby(['Handset Manufacturer'])
    #st.write(manufacturer_group['Handset Type'].value_counts().loc['Apple'].head())
    
    #create the 3 columns for the 3 top handset manufacturers
    apple_col, samsung_col, huawei_col = st.columns(3)
    
    #set up the apple column
    apple_col.subheader("Top 5 handsets by Apple")
    apple_col.write(manufacturer_group['Handset Type'].value_counts().loc['Apple'].head())
    
    #set up the samsung column
    samsung_col.subheader("Top 5 handsets by Samsung")
    samsung_col.write(manufacturer_group['Handset Type'].value_counts().loc['Samsung'].head())
    
    #set up the huawei column, 
    huawei_col.subheader("Top 5 handsets by Huawei")
    huawei_col.write(manufacturer_group['Handset Type'].value_counts().loc['Huawei'].head())

with visualization:
    st.header('Total data volumes for each application used by the users')
    
    #create the columns
    selection_col, visualize_col = st.columns(2)
    app = selection_col.selectbox("Which application do you want to view its total data volumnes?", options=['Social Media', 'Google', 'Email','Youtube', 'Gaming', 'Netflix', 'Other'], index= 0)
    
    fig = px.histogram(user_info, x=app)
    visualize_col.write(fig)

    
    