class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors  # Lista de rotores
        self.reflector = reflector  # Reflector
        self.plugboard = plugboard  # Conexiones del plugboard
        self.rotor_positions = [0] * len(rotors)  # Posiciones iniciales de los rotores

    def rotate_rotors(self):
        # Simula el avance de los rotores
        for i in range(len(self.rotors)):
            self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26
            if self.rotor_positions[i] != 0:
                break  # Solo avanza el siguiente rotor si el anterior completa un ciclo

    def plugboard_swap(self, char):
        # Intercambia caracteres según el plugboard
        return self.plugboard.get(char, char)

    def pass_through_rotors(self, char, reverse=False):
        # Pasa el carácter a través de los rotores
        offset = ord(char) - ord('A')
        for i in range(len(self.rotors)):
            rotor = self.rotors[i] if not reverse else self.rotors[-(i+1)]
            pos = self.rotor_positions[i] if not reverse else -self.rotor_positions[-(i+1)]
            # Primero convierte el valor en rotor a un carácter
            rotor_char = chr(rotor[(offset + pos) % 26])
            offset = (ord(rotor_char) - ord('A')) % 26
        return chr(offset + ord('A'))

    def encrypt_char(self, char):
        # Pasa el carácter por el plugboard, rotores y reflector
        char = self.plugboard_swap(char)
        char = self.pass_through_rotors(char)
        char = chr(self.reflector[ord(char) - ord('A')])
        char = self.pass_through_rotors(char, reverse=True)
        char = self.plugboard_swap(char)
        self.rotate_rotors()
        return char

    def encrypt_message(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                encrypted_message += self.encrypt_char(char.upper())
        return encrypted_message


# Definición de rotores, reflector y plugboard para la máquina Enigma
rotor1 = [ord(c) for c in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]  # Rotor I
rotor2 = [ord(c) for c in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]  # Rotor II
rotor3 = [ord(c) for c in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]  # Rotor III
reflector_b = [ord(c) for c in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]  # Reflector B
plugboard = {'A': 'Z', 'Z': 'A'}  # Ejemplo de configuración de plugboard

# Crear la máquina Enigma
enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector_b, plugboard)

# Mensaje para cifrar
message = "ALEMAN"
encrypted_message = enigma.encrypt_message(message)

print(f"Mensaje original: {message}")
print(f"Mensaje cifrado: {encrypted_message}")
