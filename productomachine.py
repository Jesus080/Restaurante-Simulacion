class TuringMachine:
    def _init_(self, tape):
        self.tape = list(tape) + [" "]  # Añadir un espacio en blanco al final de la cinta para simular el delimitador
        self.head = 0  # Posición inicial del cabezal
        self.state = 'J'  # Estado inicial

    def step(self):
        # Lee el valor actual en la cinta
        current_symbol = self.tape[self.head]
        
        # Lógica de transición entre estados
        if self.state == 'J':
            if current_symbol == '1':
                self.tape[self.head] = '0'
                self.head += 1
                self.state = 'K'
                
        elif self.state == 'K':
            if current_symbol == '1':
                self.tape[self.head] = '0'
                self.head += 1
                self.state = 'A'

        elif self.state == 'A':
            if current_symbol == '0':
                self.head += 1
            elif current_symbol == '1':
                self.head += 1
                self.state = 'B'

        elif self.state == 'B':
            if current_symbol == '1':
                self.head += 1
                self.state = 'C'

        elif self.state == 'C':
            if current_symbol == " ":
                self.tape[self.head] = '0'
                self.head -= 1
                self.state = 'D'

        elif self.state == 'D':
            if current_symbol == '1':
                self.head -= 1
            elif current_symbol == '0':
                self.head -= 1
                self.state = 'E'

        elif self.state == 'E':
            if current_symbol == '0':
                self.head -= 1
                self.state = 'F'

        elif self.state == 'F':
            if current_symbol == '0':
                self.tape[self.head] = '1'
                self.head += 1
                self.state = 'A'

        # Verifica si llegó a la finalización
        if self.state == '@':
            return False  # Detener si se llega al estado de aceptación
        return True

    def run(self):
        while self.step():
            print(f"Estado: {self.state} | Cinta: {''.join(self.tape)} | Cabezal: {self.head}")
        # Imprimir la cinta final sin espacios en blanco al final
        print("Cinta final:", ''.join(self.tape).rstrip())

# Entrada inicial de la cinta
initial_tape = "11011"

# Crear una instancia de la máquina de Turing con la cinta inicial
tm = TuringMachine(initial_tape)

# Ejecutar la máquina de Turing
tm.run()