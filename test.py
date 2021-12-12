from datetime import date

from Persona import Persona
from Estudiante import Estudiante


persona1 = Persona(1, 'Rodolfo', 'Melendez', '001-000000-000x', 'Managua',
        '7777-8888', (1998, 11, 27), 'alejandro@gmail.com')

estudiante1 = Estudiante(1,'Rodolfo', 'Melendez', '001-000000-000x', 'Managua',
        '7777-8888',(1998, 11, 27),'melendez@gmail.com', 234, 98)

print(persona1)
print(estudiante1)