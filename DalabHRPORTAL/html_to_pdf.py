import pdfkit

html_files = [
    'dashboard.html', 'employee-master.html', 'bulk-operations.html', 'documents.html', 'kyc.html',
    'bank-details.html', 'statutory.html', 'positions-tree.html', 'assets.html', 'profile.html',
    'alerts.html', 'manager-replacement.html', 'employee-self-service.html'
]

for html in html_files:
    pdfkit.from_file(html, html.replace('.html', '.pdf')) 