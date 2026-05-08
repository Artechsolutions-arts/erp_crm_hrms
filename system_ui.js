// AR Tech Solutions - Deep Branding Override

document.addEventListener('DOMContentLoaded', function() {
    // Override the About dialog
    if (frappe && frappe.ui && frappe.ui.toolbar) {
        frappe.ui.toolbar.show_about = function() {
            var dialog = new frappe.ui.Dialog({ title: 'About ARTS' });
            dialog.msg_area = dialog.body;
            $(dialog.msg_area).html(
                '<div style="padding: 15px;">' +
                '<p><b>AR Tech Solutions</b></p>' +
                '<p>Driven By Innovation</p>' +
                '<hr>' +
                '<p class="text-muted">Version: ' + (frappe.boot.versions ? JSON.stringify(frappe.boot.versions) : '16') + '</p>' +
                '<p class="text-muted">&copy; AR Tech Solutions. All rights reserved.</p>' +
                '</div>'
            );
            dialog.show();
        };
    }

    // Replace document title
    if (document.title.indexOf('ERPNext') > -1) {
        document.title = document.title.replace('ERPNext', 'ARTS');
    }
    if (document.title.indexOf('Frappe') > -1) {
        document.title = document.title.replace('Frappe', 'ARTS');
    }

    // MutationObserver to catch dynamic title changes and replace the hardcoded SVG logo
    var observer = new MutationObserver(function() {
        if (document.title.indexOf('ERPNext') > -1) {
            document.title = document.title.replace(/ERPNext/g, 'ARTS');
        }
        if (document.title.indexOf('Frappe') > -1) {
            document.title = document.title.replace(/Frappe/g, 'ARTS');
        }
        
        // Replace Frappe Cube SVG with our logo image in the sidebar toggle
        var frappeIcons = document.querySelectorAll('use[href="#es-line-frappe"]');
        frappeIcons.forEach(function(icon) {
            var parentSvg = icon.parentElement;
            if (parentSvg && parentSvg.parentElement && parentSvg.parentElement.classList.contains('sidebar-toggle-icon')) {
                parentSvg.parentElement.innerHTML = '<img src="/assets/arts/images/logo.png" style="width:24px; height:24px; object-fit:contain;" alt="ARTS">';
            }
        });
    });
    
    observer.observe(document.body, { childList: true, subtree: true });
    var titleEl = document.querySelector('title');
    if (titleEl) {
        observer.observe(titleEl, { childList: true });
    }
});
