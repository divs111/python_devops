import os
class utilities:
    def show_disk_space(self):
        os.system("df -h")
    def show_ram(self):
        os.system("vm_stat")
    def show_system_details(self):
        print(os.uname().sysname)

machine = utilities()  
#object- machine ias an object here that can reuse this class
machine.show_ram()
#machine.show_disk_space()
machine.show_system_details()