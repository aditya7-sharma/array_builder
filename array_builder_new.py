import numpy as np
import streamlit as st

if "array" not in st.session_state:
    st.session_state.array = None


class Array_builder:
    def __init__(self,data):
        # data = [float(x) for x in data]
        self.data = np.array(data)
        

    def slice_array(self,s,e):
        # if s.digit() and e.isdigit():
        start = int(s)
        end = int(e)
        if start<0 or end<0:
             st.error("The indices can't be negative")
             return None
        elif start>=end:
             st.error("The start can't be greater than end")
             return None
        elif start<0 or end>len(self.data):
             st.error("The indices are out of range")
             return None
        return self.data[start:end]
    
    def reshape(self):
        m = int(st.number_input("Enter the row: ",min_value = 1))
        n = int(st.number_input("Enter the column: ",min_value = 1))
        try:
            return self.data.reshape(m, n)
        except:
            st.error("Invalid shape! Total elements mismatch.")
            # return None


    def shape(self):
        return np.shape(self.data)
    
    def size(self):
        return np.size(self.data)
    
    def dtype(self):
        return self.data.dtype
    
    def summary(self):
        # slice_array()
        info = {
            "shape": self.shape(),
            "size":  self.size(),
            "dtype": self.dtype()
        }
        return info

    
if __name__ == "__main__":
    st.title("Array Builder")
    with st.expander("What can you do in project"):
        st.write("1. To create array")
        st.write("2. To Slice created array")
        st.write("3. To Reshape created array")
        st.write("4. To Get Summary of the created array")
        # st.write("1. To create array")

    if st.session_state.array is not None:
         st.subheader("Entered Array")
         st.write(st.session_state.array.data)

    choice = st.text_input("Enter your choice: ")

    if choice == "1":
                value = st.text_input("Enter the value sep by space:").split()
                if st.button("Create Array"):
                    if value:
                        st.session_state.array = Array_builder(value)
                        st.success("You created an array")

    if choice == "2":
                array = st.session_state.array

                if array is None:
                    st.error("Create an array first!")
                    st.stop()
                
                s = st.number_input("Enter start point: ",key = "start",min_value = 0,step = 1)
                e = st.number_input("Enter end point: ",key = "end",min_value = 0,step = 1)
                slice = st.button("Slice")
                if slice:
                     sliced = array.slice_array(s,e)
                     if sliced is not None:
                          st.write(f"Sliced array: {sliced}")
                          st.success("Array sliced successfully")
                        # else:
                            #   st.warning("Band bj gya")
    if choice == "4":
           array = st.session_state.array

           if array is None:
                st.error("Create an array first!")
                st.stop()
        #    if value:
           summary = array.summary()
             

            #  st.write(f"reshaped matrix: {summary["reshape"]}")
           st.subheader("Summary of the above matrix")
           st.write(f"Shape of matrix: {summary['shape']}")
           st.write(f"Datatype of matrix: {summary['dtype']}")
           st.write(f"Size of matrix: {summary['size']}")

    if choice == "3":
         array = st.session_state.array

         if array is None:
            st.error("Create an array first!")
            st.stop()
         
         reshaped_value = array.reshape()
         if reshaped_value is not None:
          st.success("Array reshaped Successfully")
          st.write(f"This is the reshaped matrix {reshaped_value}")

st.sidebar.title("About this project")

st.sidebar.markdown("""📐 Array Builder — Streamlit + NumPy Mini Project

Array Builder is a simple interactive web application built using Streamlit and NumPy.
It allows users to:

✔ Create arrays
                    
✔ Slice arrays
                    
✔ Reshape arrays
                    
✔ View summary (shape, size, datatype)

This project is perfect for beginners learning Python, NumPy, OOP, and Streamlit UI development.

🚀 Features
                    
✅ 1. Create Array

Enter space-separated values to instantly generate a NumPy array.

✅ 2. Slice Array

Choose start and end index using numeric input fields.
Uses: self.data[start:end]
             
Includes validations for:

Negative indices
                    
start > end
                    
Out-of-range indices

✅ 3. Reshape Array

Reshape your array using user-defined rows and columns.

Uses: self.data.reshape(m, n)

Automatically checks shape compatibility

✅ 4. Summary

Displays useful information:

Shape
Size
Datatype

Example:

{
  "shape": [3, 3],
  "size": 9,
  "dtype": "int64"
}

🛠 Technologies Used

Python 3
NumPy
Streamlit

📦 Installation & Setup
1. Clone the repository
git clone https://github.com/aditya7-sharma/array-builder.git
                    
cd array-builder

2. Install dependencies
pip install streamlit numpy

3. Run the application
streamlit run app.py

📁 Project Structure
array-builder/
                    
│
                    
├── app.py          # main Streamlit app
                    
├── README.md       # project documentation
                    
└── requirements.txt

🧩 Class: Array_builder
Method	Description        
slice_array(s, e)	
 
Slices the array between s and e with validation
                    
reshape()	Reshapes the array into m × n
                    
shape()	Returns shape of array
                    
size()	Returns total number of elements
                    
dtype()	Returns datatype
                    
summary()	Returns {shape, size, dtype}
                    
🖥️ UI Flow

The app includes:

Title section
Feature list (Expander)
Input fields based on selected operation
Sidebar description
Persistent array storage using st.session_state

📚 Example Usage
Input
10 20 30 40 50

Slice (1 to 4)
['20' '30' '40']

Reshape (1 × 5)
[['10' '20' '30' '40' '50']]

👨‍💻 Author

Made with ❤️ by Aditya

📜 License

This project is open-source and free to use or modify.""")

         
            
