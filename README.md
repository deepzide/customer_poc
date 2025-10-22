# ERP Base

#### `apps.json`
Define las aplicaciones que se instalarán en el entorno con sus repositorios y branches:

EX:

```json
[
  {
    "url": "https://github.com/frappe/erpnext",
    "branch": "version-15"
  },
  {
    "url": "https://github.com/deepzide/erp_base.git", 
    "branch": "main"
  }
]
```

#### `custom.txt`
Lista las aplicaciones personalizadas que se instalarán, una por línea:

```
erpnext
efficcia_custom_test
```
Nota: El desarrollo custom debe estar en apps.json y en custom.txt

## Tareas Pendientes

### Próximos Pasos

- [ ] **Prueba de Custom App**: Hacer una PoC con este repositorio
- [ ] **Inicio de Proyecto Cliente**: Empezar con el proyecto del cliente, siguiendo el flujo de trabajo de fork de repositorios
- [ ] **Definir rama de production**
- [ ] **Realizar Snapshoot de la instancia en produccion antes de hacer un cambio**
- [ ] **Hacer script de backup de la base de datos hacia un bucket S3 para mayor seguridad**
- [ ] **Prueba de Disaster recovery**

### Reglas de Operación

Para mantener la estabilidad y seguridad del entorno de producción:

- **Horario Laboral**: No modificar producción en horario laboral
- **Backup Obligatorio**: Tomar backup completo de la instancia antes de realizar cualquier cambio en producción
- **Ventana de Mantenimiento**: Los cambios en producción deben realizarse fuera del horario laboral o durante ventanas de mantenimiento programadas
