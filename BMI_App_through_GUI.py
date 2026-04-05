import tkinter as tk
import csv
from matplotlib import pyplot as plt

window=tk.Tk()
window.title("MY BMI App")
window.geometry("550x800")
window.configure(bg="#86B1D6")
data=[]
names=[]
bmi=[]

tk.Label(window, text="BMI Calculator",bg="#1D1F20",fg="white",font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(window,text="Enter the Name:",bg="#86B1D6", fg="#161897",font=("Arial",14,"bold")).pack(pady=8)
name_entry=tk.Entry(window ,width=25,font=("Arial",12))
name_entry.pack(pady=4)

tk.Label(window,text="Enter the Weight (kg):",bg="#86B1D6", fg="#161897",font=("Arial",14,"bold")).pack(pady=8) #give vertical spacing
weight_entry=tk.Entry(window,width=25,font=("Arial",12))
weight_entry.pack(pady=4)

tk.Label(window,text="Enter the Height (m):",bg="#86B1D6", fg="#161897",font=("Arial",14,"bold")).pack(pady=8)
height_entry=tk.Entry(window,width=25,font=("Arial",12))
height_entry.pack(pady=4)

def Calculate_BMI():
    try:
        name=name_entry.get()
        weight=float(weight_entry.get())
        height=float(height_entry.get())
        BMI=weight/(height*height)
        
        if BMI<=18.5:
            category="underweight"
        elif BMI<=25:
            category="normal"
        elif BMI<30:
            category="overweight"
        else:
            category="obese"

        with open("bmi_data.csv","a",newline="")as file:
            writer=csv.writer(file)
            writer.writerow([name,weight,height,round(BMI,2)])

        result_label.config(text=f"{name}, Your BMI is: {round(BMI,2)} ({category})",bg="#EAF4FF", fg="#003366",font=("arial",13,"bold"))
        data.append((name,weight,height,BMI))
        print(data)
        
    except ValueError:
        result_label.config(text="Please enter the valid input:")

def view_history():
    history_entry.delete("1.0",tk.END)
    try:
        with open("bmi_data.csv","r")as file:
            reader=csv.reader(file)
            for row in reader:
                history_entry.insert(tk.END,f"Name: {row[0]}, Weight: {row[1]}, Height: {row[2]}, BMI: {row[3]}\n")

    except FileNotFoundError:
        history_entry.insert(tk.END,"No history found yet")

def trends_analysis():
    names.clear() # cleaning the previous list 
    bmi.clear()    # so that no duplication value in graph
    try:
        with open("bmi_data.csv","r")as file:
            reader=csv.reader(file)
            for row in reader:
                names.append(row[0])
                bmi.append(float(row[3]))
        if not names or not bmi:
            print("NO Data to plot")
            return
        plt.figure(figsize=(8,5))
        plt.plot(names,bmi,marker="o")
        plt.title("BMI Trend Analysis")
        plt.xlabel("Users")
        plt.ylabel("bmi")
        plt.xticks(rotation=45)# help to easy to read
        plt.grid(True)# show vertical and horizontal line
        plt.show()
        print(names)
        print(bmi)
    except FileNotFoundError:
        print("File not find")
    except ValueError:
        print("Invalid data in csv")

def clear_fields():
    name_entry.delete(0,tk.END)
    weight_entry.delete(0,tk.END)
    height_entry.delete(0,tk.END)       #delete entry 
    history_entry.delete("1.0",tk.END)  #delete text widget 1= first line ,0= zero character
    result_label.config(text="")

tk.Button(window,text="Calculate", command=Calculate_BMI,bg="#007BFF", fg="white",font=("Arial",12,"bold"),relief="flat",width=15).pack(pady=10)# calculate button

result_label=tk.Label(window,text="")
result_label.pack(pady=4)

tk.Button(window,text="View History",command=view_history,bg="#007BFF", fg="white",font=("Arial",12,"bold"),relief="flat",width=15).pack(pady=10)#history button

history_entry=tk.Text(window,height=10,width=60, bg="#F8F9FA",fg="#333333",font=("Consolas", 10))
history_entry.pack(pady=15)
tk.Button(window,text="Analyse",command=trends_analysis,bg="#007BFF", fg="white",font=("Arial",12,"bold"),relief="flat",width=15).pack(pady=8)
tk.Button(window,text="Clear",command=clear_fields,bg="#007BFF", fg="white",font=("Arial",12,"bold"),relief="flat",width=15).pack(pady=40)

window.mainloop()