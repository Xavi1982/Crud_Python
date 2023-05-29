import socketserver

global PORT

class MyUPDHandler(socketserver.BaseRequestHandler):
    """Clase MyUPDHandler.
    
    Clase que nos permite configurar los mètodos del servidor.
    
    """
    def handle(self):
        """Método mediante el cual creamos el archivo *servidor.txt*,
        donde recopilaremos la actividad de la apliciación y la enviaremos
        mediante el servidor.

        """
        archivo = open('servidor.txt', 'a')
        data = self.request[0].strip()
        socket = self.request[1]
        
        print('Se ingresará a servidor.txt: ',data.decode("UTF-8"))
        archivo.write(data.decode('UTF-8') + '\n')
        archivo.close()
        
        value2 = 0xA0
        packed_data_2 = bytearray()
        packed_data_2 += value2.to_bytes(1, "big")
        socket.sendto(packed_data_2, self.client_address)

        
if __name__ == "__main__":
    HOST , PORT = "localhost", 15200
    with socketserver.UDPServer((HOST, PORT), MyUPDHandler) as servidor:
        servidor.serve_forever()