def update_server_info(file_name,key,value):
    with open(file_name,'r') as file:
        lines = file.readlines()

    with open(file_name,'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)
file = 'server.config'
key_name = 'TIMEOUT'
valuee = '50'
update_server_info(file,key_name,valuee)