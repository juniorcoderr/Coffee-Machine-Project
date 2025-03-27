## 🟤 **Coffee Machine Project – Python**

This **Coffee Machine Project** simulates a real-life coffee vending machine where users can order beverages like **Espresso**, **Latte**, and **Cappuccino**. The program checks resource availability, handles payments in **Indian currency (₹)**, and provides an option to turn off the machine or view available resources. 

---

### 📌 **Features**
- ☕ **Choose from 3 Drinks** – Espresso, Latte, and Cappuccino.  
- 📊 **Resource Management** – Tracks water, milk, and coffee quantities.  
- 💰 **Payment Handling** – Accepts ₹10, ₹5, ₹2, and ₹1 coins/notes.  
- 🔍 **Reporting System** – Displays the current status of resources and money collected.  
- 🔴 **Machine Control** – Option to turn off the machine (`off` command).  

---

### 📜 **Code Explanation & Python Concepts Used**

1. **Data Storage with Dictionaries**
   - The `MENU` dictionary stores drink recipes and prices.
   - The `resources` dictionary keeps track of available ingredients and total earnings.
   
2. **User Input Handling**
   - Users provide input to select drinks, insert money, or manage the machine (`off` or `report` commands).  
   - Input validation ensures proper handling of errors (e.g., negative or invalid input).  

3. **Conditional Statements (`if`, `elif`, `else`)**
   - Used to check user choices, manage resources, and control the machine's workflow.  
   - Determines if there are enough ingredients to prepare the selected drink.  

4. **Loops (`while True`)**
   - An infinite loop is used to continuously accept orders until the machine is turned off.
   - Nested conditions check availability and process payments.  

5. **Error Handling (`try-except` block)**
   - Ensures the program does not crash if the user enters invalid data (e.g., non-numeric input).  

6. **Calculation Logic**
   - Computes the total payment and checks if it meets the cost of the selected drink.  
   - Provides correct **change** if the user overpays.  

7. **String Formatting**
   - Uses **f-strings** to format outputs (e.g., displaying remaining resources and transaction details).  

---

### 🛠️ **How to Run the Program**
1. Ensure **Python** is installed on your system.  
2. Run the script with the command:  
   ```bash
   python coffee_machine.py
   ```
3. Follow the on-screen prompts to:
   - Select a drink.
   - Insert the correct amount in Indian currency.
   - View the resources or turn off the machine.

---

### 📌 **Enhancements You Can Try**
- Add more beverages to the menu.
- Implement an admin mode for restocking resources.
- Allow multiple currencies or digital payment options.
- Enhance the UI with a graphical interface using **Tkinter**.

Feel free to explore the code, suggest improvements, and contribute! 🍵
