#!/bin/sh

. /usr/lib/libmodcgi.sh
[ -r /etc/options.cfg ] && . /etc/options.cfg

check "$ISC_DHCP_RESTART_MULTID" yes:restart_multid
check "$ISC_DHCP_WRAPPER"        yes:multid_wrapper

sec_begin '$(lang de:"Starttyp" en:"Start type")'
cgi_print_radiogroup_service_starttype "enabled" "$ISC_DHCP_ENABLED" "" "" 0
cat << EOF
<p>
<input type="hidden"   name="multid_wrapper" value="no">
<input type="checkbox" name="multid_wrapper" value="yes" $multid_wrapper_chk id="e2">
<label for="e2"> $(lang de:"vor multid starten" en:"start before multid")</label>
</p>
<hr>
ISC_DHCP_RESTART_MULTID: $ISC_DHCP_RESTART_MULTID
ISC_DHCP_WRAPPER:        $ISC_DHCP_WRAPPER
<hr>
EOF
sec_end

sec_begin '$(lang de:"Konfiguration" en:"Configuration")'
cat << EOF
<input type="hidden" name="multid_wrapper" value="yes">
<p>
$(lang de:"Optionale Parameter:" en:"Optional parameters:")
<input type="text" name="cmdline" size="55" maxlength="250" value="$(html "$ISC_DHCP_CMDLINE")">
</p>
EOF
# if [ "$FREETZ_AVMDAEMON_DISABLE_DHCP" != "y" ]; then
cat << EOF
<p>
<input type="hidden"   name="restart_multid" value="no">
<input type="checkbox" name="restart_multid" value="yes" $restart_multid_chk id="e1">
<label for="e1"> $(lang de:"multid restarten" en:"restart multid")</label>
</p>
EOF
# fi
sec_end
