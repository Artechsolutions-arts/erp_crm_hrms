import frappe

def execute():
    frappe.init(site='frontend')
    frappe.connect()
    frappe.set_user('Administrator')

    print('--- Fixing Desk Branding ---')

    # 1. Update arts boot.py to aggressively override bootinfo
    boot_py = """import frappe

def boot_session(bootinfo):
    # Override app logo
    bootinfo.app_logo_url = '/assets/arts/images/logo.png'
    
    # Override app name
    bootinfo.app_name = 'ARTS'
    
    # Override website settings
    if not bootinfo.get('website_settings'):
        bootinfo.website_settings = {}
    bootinfo.website_settings['app_name'] = 'ARTS'
    
    # Override module/app names in bootinfo.app_data if present
    if bootinfo.get('app_data'):
        for app in bootinfo.app_data:
            if app.get('app_name') == 'erpnext':
                app['app_title'] = 'ARTS'
            if app.get('app_name') == 'frappe':
                app['app_title'] = 'Framework'
                
    # Override active workspaces if they contain Frappe or ERPNext
    if bootinfo.get('workspaces'):
        for ws in bootinfo.workspaces:
            if 'ERPNext' in ws.get('title', ''):
                ws['title'] = ws['title'].replace('ERPNext', 'ARTS')
            if 'Frappe' in ws.get('title', ''):
                ws['title'] = ws['title'].replace('Frappe', 'ARTS')
"""

    with open('/home/frappe/frappe-bench/apps/arts/arts/boot.py', 'w') as f:
        f.write(boot_py)
    print("Updated boot.py")

    # 2. Add more translations just in case
    translations = {
        'ERPNext': 'ARTS',
        'Frappe HR': 'HRM',
        'Frappe Framework': 'Framework',
    }
    for source, target in translations.items():
        existing = frappe.db.exists('Translation', {'source_text': source})
        if not existing:
            doc = frappe.get_doc({
                'doctype': 'Translation',
                'language': 'en',
                'source_text': source,
                'translated_text': target,
            })
            doc.insert(ignore_permissions=True)

    # 3. Rename any remaining workspaces
    for ws in frappe.get_all('Workspace', fields=['name', 'title']):
        if 'ERPNext' in ws.title or 'Frappe' in ws.title:
            new_title = ws.title.replace('ERPNext', 'ARTS').replace('Frappe', 'ARTS')
            frappe.db.set_value('Workspace', ws.name, 'title', new_title)
            print(f"Renamed workspace {ws.name} to {new_title}")

    frappe.db.commit()
    frappe.clear_cache()
    print('Done.')

execute()
