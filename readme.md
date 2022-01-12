NetPing OpenWRT WEB schema
https://netping.atlassian.net/wiki/spaces/NW/pages/3598975563/OWRT-WEB-netping-schema+WEB+APP+web+OpenWRT
!!!Этот пакет удаляет некоторые конфигурационные файлы luci-base, luci-mod-*
В случае необходимости их восстановления недостаточно удалить пакет, нужно переустановить соответствующие модули с заменой файлов.
Для установки через make: make install
После устройство нужно перезагрузить, чтобы отработал инициализационный скрипт. Интерфейс станет от NetPing.
