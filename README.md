# report-print-send, Odoo 19.0

Loose copy of the two modules that carry the STeSI patches. Every other module of
the repository comes from OCA.

| Module | Version | Pull request |
|---|---|---|
| `base_report_to_printer` | 19.0.1.2.4 | `19.0-fix-passing-doc_format` |
| `printer_zpl2` | 19.0.1.0.0 | `19.0-mig-printer_zpl2` |

## The two patches

`base_report_to_printer`, `print_document` forwards `doc_format` to `print_file`.
Held back in the signature, a ZPL label reached CUPS as a plain file and the queue
driver printed its source as text. `printer_zpl2` sends `doc_format="raw"`, and
`_set_option_doc_format` turns it into the CUPS option that skips the filters. The
regression came in with `b75c6b0`, which extracted the CUPS backend into its own
module.

`base_report_to_printer`, `data/neutralize.sql` checks that
`printing_report_xml_action.active` exists before it writes to it, so the
neutralization of a database restored from an older version does not abort.

`printer_zpl2` is the 19.0 migration, plus the label field list, whose domain never
saw the context and came back empty.

## Install

Add this directory to `addons_path`. `printer_zpl2` depends on
`base_report_to_printer_cups`, which is not here: take it from OCA 19.0 and put it
on the addons path as well, ahead of nothing in particular, since neither module
here overrides it. It needs `pycups`.

The branches of the two pull requests keep the full repository, with the OCA
history. This branch holds a single commit and no history of its own.

## Credits

Authors: Odoo Community Association (OCA)

Contributors: see each module's `readme/CONTRIBUTORS.md`. STeSI patches by
Michele Di Croce &lt;dicroce.m@stesi.eu&gt;.
