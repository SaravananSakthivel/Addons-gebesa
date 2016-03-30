# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Integration Netsuite Fields",
    "summary": "Add new fields for integration with netsuite",
    "version": "9.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://odoo-community.org/",
    "author": "<Deysy Mascorro, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "account",
        "stock",
        "product",
        "integration_progress_fields",
    ],
    "data": [
        "views/account_invoice_view.xml",
        "views/product_view.xml",
    ],
    "demo": [

    ],
    "qweb": [

    ]
}
