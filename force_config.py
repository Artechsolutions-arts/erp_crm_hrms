import frappe

def execute():
    frappe.init(site='frontend')
    frappe.connect()
    frappe.set_user('Administrator')

    print('--- Forcing Deep Branding Updates ---')
    logo_path = '/assets/arts/images/logo.png'
    app_name = 'ARTS'

    # System Settings
    frappe.db.set_single_value('System Settings', 'app_name', app_name)
    
    # Website Settings
    ws = frappe.get_doc('Website Settings')
    ws.app_name = app_name
    ws.app_logo = logo_path
    ws.splash_image = logo_path
    ws.favicon = '/assets/arts/images/favicon.png'
    ws.brand_html = f'<img src="{logo_path}" style="height:28px;width:auto;object-fit:contain;" alt="{app_name}">'
    ws.save(ignore_permissions=True)

    # Navbar Settings
    try:
        ns = frappe.get_doc('Navbar Settings')
        ns.app_logo = logo_path
        ns.save(ignore_permissions=True)
    except Exception as e:
        print(f"Could not update Navbar Settings: {e}")

    # Translations
    translations = {
        'ERPNext': app_name,
        'Frappe Framework': app_name,
        'Frappe': app_name,
        'Frappe HR': 'HRM',
        'Welcome to Frappe!': f'Welcome to {app_name}!',
        'Welcome to Frappe HR': f'Welcome to {app_name} HRM',
        'Login to {0}': 'Login to ARTS',
        'Powered by ERPNext': ' ',
        'ERPNext updated to': f'{app_name} updated to',
    }
    
    for source, target in translations.items():
        existing = frappe.db.exists('Translation', {'source_text': source, 'language': 'en'})
        if existing:
            frappe.db.set_value('Translation', existing, 'translated_text', target)
        else:
            doc = frappe.get_doc({
                'doctype': 'Translation',
                'language': 'en',
                'source_text': source,
                'translated_text': target,
            })
            doc.insert(ignore_permissions=True)

    # Workspaces
    workspaces_to_rename = {
        'ERPNext Settings': 'Settings',
        'Frappe HR': 'HRM',
        'Frappe Framework': 'Framework'
    }
    for old, new in workspaces_to_rename.items():
        if frappe.db.exists('Workspace', old):
            frappe.db.set_value('Workspace', old, 'title', new)

    frappe.db.commit()
    frappe.clear_cache()
    print('Branding forced and cache cleared.')

execute()
