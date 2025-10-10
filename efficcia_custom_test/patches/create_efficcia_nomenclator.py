import json
import frappe
import random
import string

DOCTYPE = "Efficcia Doc"
FILE_PATH = frappe.get_app_path("efficcia_custom_test", "nomenclators", "efficcia_doctype_test.json")


def load_nomenclator(file_path):
    """Carga los registros desde el JSON"""
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def clear_existing_records(doctype):
    """Elimina todos los registros existentes del Doctype"""
    frappe.db.delete(doctype)


def record_exists(doctype, custom_name):
    """Verifica si ya existe un registro con el mismo nombre"""
    return frappe.db.exists(doctype, {"custom_name": custom_name})


def create_record(entry):
    """Crea un nuevo registro del nomenclador"""
    doc = frappe.new_doc(DOCTYPE)
    doc.custom_name = entry.get("custom_name")
    doc.save(ignore_permissions=True)


def create_random_records(cantidad=5):
    """Crea registros aleatorios adicionales"""
    for _ in range(cantidad):
        nombre_aleatorio = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        doc = frappe.new_doc(DOCTYPE)
        doc.custom_name = nombre_aleatorio
        doc.save(ignore_permissions=True)


def execute():
    """Punto de entrada del patch"""
    nomenclator = load_nomenclator(FILE_PATH)
    clear_existing_records(DOCTYPE)

    for entry in nomenclator:
        if not record_exists(DOCTYPE, entry["custom_name"]):
            create_record(entry)

    # Crear algunos aleatorios adicionales
    create_random_records(cantidad=10)

    frappe.db.commit()
    frappe.logger().info(f"✅ Nomenclador '{DOCTYPE}' cargado correctamente con {len(nomenclator)} + 10 aleatorios.")
