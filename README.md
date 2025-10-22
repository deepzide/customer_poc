# ERP Base

A streamlined ERP deployment template for managing Frappe/ERPNext applications and custom developments.

## Configuration Files

### [`apps.json`](apps.json)
Defines the applications to be installed with their repositories and branches.

**Example:**
```json
[
  {
    "url": "https://github.com/frappe/erpnext",
    "branch": "version-15"
  },
  {
    "url": "https://github.com/deepzide/<REPO>.git",
    "branch": "<BRANCH>"
  }
]
```

### [`custom.txt`](custom.txt)
ADD custom applications to be installed (one per line).

**Example:**
```
erpnext
<DEV_CUSTOM>
```

**Important:** When adding custom development, both configuration files must be updated:
- Add the repository URL and branch to [`apps.json`](apps.json)
- Add the application name to [`custom.txt`](custom.txt)



### Próximos Pasos

- [ ] **Escoger una version de frappe fija. Cuando se actualiza a un realease grande se reinicia el proceso de setup** 
- [ ] **Prueba de Custom App**: Hacer una PoC con este repositorio
- [ ] **Inicio de Proyecto Cliente**: Empezar con el proyecto del cliente
- [ ] **Definir rama de production**
- [ ] **Realizar Snapshoot de la instancia en produccion antes de hacer un cambio**
- [ ] **Hacer script de backup de la base de datos hacia un bucket S3 (AWS) para mayor seguridad**
- [ ] **Prueba de Disaster recovery**
- [ ] **Agregar DNS a cada IP** 
- [ ] **Buscar manera de que los developers puedan ver los logs (++ pipeline)**

### Reglas de Operación

Para mantener la estabilidad y seguridad del entorno de producción:

- **Horario Laboral**: No modificar producción en horario laboral
- **Backup Obligatorio**: Tomar backup completo de la instancia antes de realizar cualquier cambio en producción
- **Ventana de Mantenimiento**: Los cambios en producción deben realizarse fuera del horario laboral o durante ventanas de mantenimiento programadas


## Operational Guidelines

To ensure production environment stability and security:

- **Working Hours:** Avoid production modifications during business hours
- **Mandatory Backup:** Complete instance backup required before any production changes
- **Maintenance Windows:** Production changes must occur outside business hours or during scheduled maintenance
