def update_server_config(filename,key,value):
    with open(filename,'r') as file:
        lines = file.readlines()

    with open(filename,'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

server_config_file = 'server.config'
key_name = 'MAX_CONNECTIONS'
new_value = '1000'
update_server_config(server_config_file,key_name,new_value)