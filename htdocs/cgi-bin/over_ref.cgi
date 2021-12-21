#!/usr/bin/lua

require "luci.cacheloader"
require "luci.sgi.cgi"
print ("Content-type: Text/html\n")
print (os.date("%H:%M:%S %d.%m.%Y"))
print (os.date("%Hh %Mm %Ss", luci.sys.uptime()))
print (string.format("%.2f", nixio.sysinfo().loads[1]) .. ", " .. string.format("%.2f", nixio.sysinfo().loads[2]) .. ", " .. string.format("%.2f", nixio.sysinfo().loads[3]))
