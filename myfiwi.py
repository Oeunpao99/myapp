import streamlit as st
import csv

def record_borrowing(name, purpose, date, address, amount):
    with open('borrowings.csv', 'a', newline='', encoding='utf-8') as csvfile:  # Specify encoding='utf-8'
        fieldnames = ['Name', 'Purpose', 'Date', 'Address', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Check if the file is empty, if so, write the header
        csvfile.seek(0, 2)
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow({'Name': name, 'Purpose': purpose, 'Date': date, 'Address': address, 'Amount': amount})


def main():
    st.title("Borrowing Recording App")
    name = st.text_input("Enter the name of the person who borrowed money:")
    purpose = st.text_input("Enter the purpose of borrowing:")
    date = st.date_input("Enter the date of borrowing:")
    address = st.text_input("Enter the address of borrowing:")
    amount = st.number_input("Enter the amount borrowed ($):", min_value=0.0)
    
    if st.button("Record Borrowing"):
        record_borrowing(name, purpose, str(date), address, amount)
        st.success("Borrowing recorded successfully!")

if __name__ == "__main__":
    main()
