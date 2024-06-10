# Import python packages
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
#from st_aggrid import AgGrid


# Write directly to the app
st.title(":lock: Adding Exception User :unlock:")
st.write(
    """Fill User Details
    """
)


user_id = st.text_input("MQID (only numbers without 'MQ')")
#st.write('User MQID: ', user_id)

user_email = st.text_input('MQ_EMAIL', key='user_email')
#st.write('User MQ Email: ', user_email)

# Display the Profile Options List SiS App
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.up_rls.profile").select(col('PROFILE_DESCRIPTION'))
#st.dataframe(data=my_dataframe, use_container_width=True)

profile = st.selectbox(
    "Access Level: ",
    my_dataframe,
    placeholder="Select..."
    )

#st.write('User Access Level: ', profile)

if profile: 
    # Build a SQL Insert Statement & Test It
    my_insert_stmt = """ insert into smoothies.up_rls.user_masterlist(mqid, mq_email, profile)
            values ('""" + user_id + """', '""" + user_email + """', '""" + profile + """')"""

    # Add a Submit Button
    time_to_insert = st.button('Submit')

    # Insert the Order into Snowflake
    if time_to_insert: 
        #IF Block dependent on the submit button being clicked by the customer
        session.sql(my_insert_stmt).collect()
        st.success('User is added, ' + user_email, icon="✅")
        




