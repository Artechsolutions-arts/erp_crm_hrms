import frappe

def boot_session(bootinfo):
    logo = '/assets/arts/images/logo.png'
    bootinfo.app_logo_url = logo
    bootinfo.app_name = 'ARTS'
    
    if not bootinfo.get('website_settings'):
        bootinfo.website_settings = {}
    bootinfo.website_settings['app_name'] = 'ARTS'
    
    if bootinfo.get('app_data'):
        for app in bootinfo.app_data:
            app['app_logo_url'] = logo
            
            if app.get('app_name') == 'erpnext':
                app['app_title'] = 'ARTS'
            elif app.get('app_name') == 'frappe':
                app['app_title'] = 'Framework'
            elif app.get('app_name') == 'hrms':
                app['app_title'] = 'HRM'
