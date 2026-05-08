// AR Tech Solutions - Final Branding Polish
$(document).ready(function() {
    const COMPANY_NAME = 'AR Tech Solutions';
    const HR_NAME = 'HRM';
    
    function replaceText() {
        // Target all text nodes to be absolutely sure
        $(':contains(\"Frappe HR\"), :contains(\"ERPNext\"), :contains(\"Frappe\")').each(function() {
            if ($(this).children().length === 0) {
                var text = $(this).text();
                if (text.includes('Frappe HR')) text = text.replace(/Frappe HR/g, HR_NAME);
                if (text.includes('ERPNext')) text = text.replace(/ERPNext/g, COMPANY_NAME);
                if (text.includes('Frappe')) text = text.replace(/Frappe/g, COMPANY_NAME);
                $(this).text(text);
            }
        });

        // Specific fix for the large subtitle in screenshots
        $('.sidebar-item-subtitle, .sidebar-header div, .workspace-header .title-text').each(function() {
             var text = $(this).text().trim();
             if (text === 'Frappe HR') $(this).text(HR_NAME);
             if (text === 'ERPNext') $(this).text(COMPANY_NAME);
        });

        if (document.title.includes('ERPNext')) document.title = document.title.replace(/ERPNext/g, COMPANY_NAME);
    }

    replaceText();
    setInterval(replaceText, 1000);
});
