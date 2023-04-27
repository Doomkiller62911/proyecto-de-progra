import tkinter as tk
import tkinter.messagebox

seat=2000
time=2000
movie=2000

    
nombre = input("Ingrese el nombre del cliente: ")
cedula = int(input("Ingrese el número de cédula del cliente: "))
correo = input("Ingrese su correo electrónico: ")
personas = int(input("Ingrese la cantidad de personas para la reserva: "))
total = seat + time + movie 
total_completo = total * personas
root = tk.Tk()
root.title("Sistema de Reserva de Peliculas")


movie_frame = tk.Frame(root, padx=10, pady=10)
movie_label = tk.Label(movie_frame, text="Select a movie:")
movie_label.pack(side=tk.LEFT)

movie_var = tk.StringVar()
movie_choices = ["Avengers: Endgame", "The Matrix", "Star Wars: The Rise of Skywalker"]
movie_dropdown = tk.OptionMenu(movie_frame, movie_var, *movie_choices)
movie_dropdown.pack(side=tk.LEFT)

movie_frame.pack()


time_frame = tk.Frame(root, padx=10, pady=10)
time_label = tk.Label(time_frame, text="Selecciona un horario:")
time_label.pack(side=tk.LEFT)

time_var = tk.StringVar()
time_choices = ["10:00am", "2:00pm", "6:00pm"]
time_dropdown = tk.OptionMenu(time_frame, time_var, *time_choices)
time_dropdown.pack(side=tk.LEFT)

time_frame.pack()


pay = tk.Frame(root, padx=10, pady=10)
tpay = tk.Label(pay, text="Selecciona un metodo de pago:")
tpay.pack(side=tk.LEFT)

vpay = tk.StringVar()
lpay = ["Tarjeta", "Efectivo","Simpe"]
lpayd = tk.OptionMenu(pay, vpay, *lpay)
lpayd.pack(side=tk.LEFT)
pay.pack()

seat_frame = tk.Frame(root, padx=10, pady=10)
seat_label = tk.Label(seat_frame, text="Seleccione sus asientos:")
seat_label.pack()

num_rows = 5
num_cols = 10
seats = {}
for row in range(num_rows):
    row_frame = tk.Frame(seat_frame)
    row_frame.pack(side=tk.TOP)
    for col in range(num_cols):
        seat_id = f"{chr(row+65)}{col+1}"
        seat_button = tk.Button(row_frame, text=seat_id, width=3, height=1)
        seat_button.config(command=lambda id=seat_id: select_seat(id))
        seat_button.pack(side=tk.LEFT)
        seats[seat_id] = seat_button    

seat_frame.pack()

def factura():
    label1 = tk.Label(root, text="El precio del asiento es: " + str(seat))
    label2 = tk.Label(root, text="El precio por el horario es: " + str(time))
    label3 = tk.Label(root, text="El precio por la pelicula es: " + str(movie))
    label4 = tk.Label(root, text="El total a pagar es:  " + str(total_completo))
    label5 = tk.Label(root, text="El nombre asiento es: " + str(nombre))
    label6 = tk.Label(root, text="La cedula asignada es: " + str(cedula))
    label7 = tk.Label(root, text="El correo asignado es:  " + str(correo))
    label8 = tk.Label(root, text="La cantidad total de personas es:  " + str(personas))

    label1.pack()   
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()   
    label6.pack()
    label7.pack()
    label8.pack()
    root.mainloop()

book_button = tk.Button(root, text="Pagar", padx=10, pady=10, command=factura)

book_button.pack()


selected_seat_label = tk.Label(root, text="")
selected_seat_label.pack()


def select_seat(seat_id):
    selected_seat_label.config(text=f"Asiento seleccionado: {seat_id}")


root.mainloop()

root = tk.Tk()



