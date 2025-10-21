# ERP Base

## Descripción del Proyecto



## Flujo de Trabajo para Nuevos Clientes

### 1. Fork de Repositorios Base

Cuando llega un nuevo cliente, se deben forkar los siguientes repositorios:

- **Frappe Docker**: `https://github.com/frappe/frappe_docker`
- **Módulos necesarios**: ERPNext y cualquier módulo personalizado requerido

**Para múltiples clientes**: Cada cliente debe tener su propio fork de cada repositorio, manteniendo ambientes completamente aislados.

### 2. Estructura de Archivos de Configuración

En cada fork de cliente, se deben crear dos archivos de configuración:

#### `apps.json`
Define las aplicaciones que se instalarán en el entorno con sus repositorios y branches:

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

## Tareas Pendientes

### Próximos Pasos

- [ ] **Prueba de Custom App**: Que Cesaar pruebe la aplicación personalizada `efficcia_custom_test` para validar su funcionamiento
- [ ] **Inicio de Proyecto Cliente**: Empezar con el proyecto del cliente, siguiendo el flujo de trabajo de fork de repositorios

### Reglas de Operación

Para mantener la estabilidad y seguridad del entorno de producción:

- **Horario Laboral**: No modificar producción en horario laboral (Lunes a Viernes 9:00 AM - 6:00 PM)
- **Backup Obligatorio**: Tomar backup completo de la instancia antes de realizar cualquier cambio en producción
- **Ventana de Mantenimiento**: Los cambios en producción deben realizarse fuera del horario laboral o durante ventanas de mantenimiento programadas


