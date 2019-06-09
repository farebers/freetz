#!/bin/sh

. /usr/lib/libmodcgi.sh
[ -r /etc/options.cfg ] && . /etc/options.cfg

check "$ISC_DHCP_RESTART_MULTID" yes:restart_multid

sec_begin '$(lang de:"Starttyp" en:"Start type")'
cgi_print_radiogroup_service_starttype "enabled" "$ISC_DHCP_ENABLED" "" "" 0
sec_end

sec_begin '$(lang de:"Konfiguration" en:"Configuration")'
# if [ "$FREETZ_AVMDAEMON_DISABLE_DHCP" != "y" ]; then
cat << EOF
<p>
<input type="hidden"   name="restart_multid" value="no">
<input type="checkbox" name="restart_multid" value="yes" $restart_multid_chk id="e1">
<label for="e1"> $(lang de:"multid restarten" en:"restart multid")</label>
</p>
EOF
cat << EOF
<p>
$(lang de:"Optionale Parameter:" en:"Optional parameters:")
<input type="text" name="cmdline" size="55" maxlength="250" value="$(html "$ISC_DHCP_CMDLINE")">
</p>
EOF
# fi
sec_end
