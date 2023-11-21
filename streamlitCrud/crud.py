# import userful libraries
import mysql.connector
import streamlit as st

# Establish connection to mysql server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud_streamlit"
)

my_cursor = db.cursor()
print('Connection establish!')

# Create streamlit app
st.title('CRUD operation with mysql')

# Display options for CRUD operations
crud_options = st.sidebar.selectbox('Select CRUD operation', options=(['Create', 'Read', 'Update', 'Delete']))

# perform selected crud operation
if crud_options == "Create":
    st.subheader('Create a record')
    firstname = st.text_input('Enter your first name:')
    lastname = st.text_input('Enter your last name:')
    phone = st.text_input('Enter your phone number:')
    email = st.text_input('Enter your email address:')
    if st.button('Create User'):
        sql = "insert into users(first_name,last_name,phone_number,email) values(%s,%s,%s,%s)"
        val = (firstname, lastname, phone, email)

        # Execute sql query
        my_cursor.execute(sql, val)
        db.commit()
        st.success('User Created successfully into the database!')

# Read Record
elif crud_options == "Read":
    st.subheader('Read  records')
    sql = "select * from users"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    for row in result:
        st.write(row)

# Update Record
elif crud_options == "Update":
    st.subheader('Update a record')
    id = st.number_input('Enter ID')
    firstname = st.text_input('Enter new first name:')
    lastname = st.text_input('Enter new last name:')
    phone = st.text_input('Enter new phone number:')
    email = st.text_input('Enter new email address:')
    if st.button('Update user'):
        sql = 'update users set first_name=%s,last_name=%s,phone_number=%s,email=%s where id=%s'
        val = (firstname, lastname, phone, email, id)
        my_cursor.execute(sql, val)
        db.commit()
        st.success('User updated successfully!')

# Delete record
else:
    st.subheader('Delete a record')
    id = st.number_input('Enter ID', min_value=1)
    if st.button('Delete user'):
        sql = "delete from users where id=%s"
        val = (id,)
        my_cursor.execute(sql, val)
        db.commit()
        st.success("User deleted successfully!")