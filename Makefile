include $(TOPDIR)/rules.mk

LUCI_TITLE:=NetPing LuCI
LUCI_DEPENDS:=

include $(TOPDIR)/feeds/luci/luci.mk

# call BuildPackage - OpenWrt buildroot signature