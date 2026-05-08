app_name = 'arts'
app_title = 'AR Tech Solutions'
app_publisher = 'AR Tech Solutions'
app_description = 'AR Tech Solutions Branding'
app_email = 'info@artechsolution.co.in'
app_license = 'Proprietary'
app_logo_url = '/assets/arts/images/logo.png'

website_context = {
    'favicon': '/assets/arts/images/favicon.png',
    'splash_image': '/assets/arts/images/logo.png',
}

app_include_css = ['/assets/arts/css/arts_branding.css']
app_include_js = ['/assets/arts/js/arts_branding.js']
web_include_css = ['/assets/arts/css/arts_branding.css']
web_include_js = ['/assets/arts/js/arts_branding.js']

boot_session = 'arts.boot.boot_session'

# Portability: Ensure these translations are applied on any site
translation_overrides = {
    'ERPNext': 'AR Tech Solutions',
    'Frappe HR': 'HRM',
    'HRMS': 'HRM'
}
