from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(cr, version):
    # 19.0: odoo/modules/migration.py accetta come nomi dei parametri solo
    # `cr`/`_cr` e `version`/`_version`, e inspect.signature() segue
    # `__wrapped__` fino a questa funzione invece di fermarsi al wrapper di
    # openupgradelib. Il decoratore continua a passare un env.
    env = cr
    if openupgrade.table_exists(
        env.cr, "printing_tray"
    ) and not openupgrade.table_exists(env.cr, "printing_tray_input"):
        openupgrade.rename_models(env.cr, [("printing.tray", "printing.tray.input")])
        openupgrade.rename_tables(env.cr, [("printing_tray", "printing_tray_input")])
        openupgrade.rename_fields(
            env,
            [
                (
                    "ir.actions.report",
                    "ir_actions_report",
                    "printer_tray_id",
                    "printer_input_tray_id",
                ),
                (
                    "printing.report.xml.action",
                    "printing_report_xml_action",
                    "printer_tray_id",
                    "printer_input_tray_id",
                ),
                (
                    "res.users",
                    "res_users",
                    "printer_tray_id",
                    "printer_input_tray_id",
                ),
            ],
        )
