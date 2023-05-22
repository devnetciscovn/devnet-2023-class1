def vrf_configuration(vrf_name, rd, rt_import='', rt_export=''):
    rt_import_value = rt_import if rt_import else rd
    rt_export_value = rt_export if rt_export else rd

    lst = [f'vrf {vrf_name}',
           f'rd {rd}',
           f'route-target import {rt_import_value}',
           f'route-target export {rt_export_value}']

    return "\n".join(lst)

username = 'admin'
password = '249898s09f#adfafdaf'
