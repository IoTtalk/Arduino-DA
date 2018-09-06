file = open ('/etc/rc.local','w')

file.write('''# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

boot-complete-notify

(sleep 0;python -u /root/DAI.py)

exit 0''')
file.close()
