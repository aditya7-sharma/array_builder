📐 Array Builder — Streamlit + NumPy Mini Project

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
git clone https://github.com/your-username/array-builder.git
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
slice_array(s, e)	Slices the array between s and e with validation
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

This project is open-source and free to use or modify.
