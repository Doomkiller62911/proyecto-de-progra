import tkinter as tk
import tkinter.messagebox

seat=2000
time=2000
movie=2000


total = seat + time + movie 
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

def show_message():
    tkinter.messagebox.showinfo("Factura", "La pelicula: 2000.                                                                               El horario: 2000.                                                                               El asiento: 2000.                                                                               TOTAL:6000")

book_button = tk.Button(root, text="Pagar", padx=10, pady=10, command=show_message)

book_button.pack()


selected_seat_label = tk.Label(root, text="")
selected_seat_label.pack()


def select_seat(seat_id):
    selected_seat_label.config(text=f"Asiento seleccionado: {seat_id}")


root.mainloop()
