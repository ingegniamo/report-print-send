-- The `active` column of printing_report_xml_action is missing on a database
-- upgraded from an earlier version, since the module adds it only once it is
-- updated. Neutralization runs before that, on the restored dump, so an
-- unguarded UPDATE raises "column active does not exist" and aborts the build.
update printing_printer set active=false;
update ir_act_report_xml set printing_printer_id=null;
do $$
begin
    if exists (
        select 1 from information_schema.columns
         where table_name = 'printing_report_xml_action'
           and column_name = 'active'
    ) then
        update printing_report_xml_action set active=false;
    end if;
end $$;
