import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-stock-logistics-warehouse",
    description="Meta package for oca-stock-logistics-warehouse Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-scrap_reason_code',
        'odoo14-addon-stock_archive_constraint',
        'odoo14-addon-stock_available',
        'odoo14-addon-stock_available_immediately',
        'odoo14-addon-stock_available_mrp',
        'odoo14-addon-stock_available_unreserved',
        'odoo14-addon-stock_demand_estimate',
        'odoo14-addon-stock_demand_estimate_matrix',
        'odoo14-addon-stock_free_quantity',
        'odoo14-addon-stock_generate_putaway_from_inventory',
        'odoo14-addon-stock_helper',
        'odoo14-addon-stock_inventory_preparation_filter',
        'odoo14-addon-stock_location_children',
        'odoo14-addon-stock_location_lockdown',
        'odoo14-addon-stock_location_position',
        'odoo14-addon-stock_location_tray',
        'odoo14-addon-stock_location_zone',
        'odoo14-addon-stock_measuring_device',
        'odoo14-addon-stock_measuring_device_zippcube',
        'odoo14-addon-stock_move_common_dest',
        'odoo14-addon-stock_move_location',
        'odoo14-addon-stock_orderpoint_move_link',
        'odoo14-addon-stock_packaging_calculator',
        'odoo14-addon-stock_picking_cancel_confirm',
        'odoo14-addon-stock_pull_list',
        'odoo14-addon-stock_putaway_method',
        'odoo14-addon-stock_quant_manual_assign',
        'odoo14-addon-stock_request',
        'odoo14-addon-stock_request_picking_type',
        'odoo14-addon-stock_reserve_rule',
        'odoo14-addon-stock_search_supplierinfo_code',
        'odoo14-addon-stock_vertical_lift',
        'odoo14-addon-stock_warehouse_calendar',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
