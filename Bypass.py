import requests,os
os.system("cls")
os.system("color 0F")
os.system("title Reeeaeeection Byeeeeeeepasser")
count = int(0)
print("""
        ██████  ██    ██ ███████     ██████  ██    ██ ███████    
        ██   ██  ██  ██  ██          ██   ██  ██  ██  ██  
        ██████    ████   █████       ██████    ████   █████     
        ██   ██    ██    ██          ██   ██    ██    ██      
        ██████     ██    ███████     ██████     ██    ███████        
................................................................... 
................................................................... 
................................................................... 
................................................................... 
................................................................... 
................................................................... 

        ██████  ██    ██ ██████   █████  ███████ ███████
        ██   ██  ██  ██  ██   ██ ██   ██ ██      ██    
        ██████    ████   ██████  ███████ ███████ ███████
        ██   ██    ██    ██      ██   ██      ██      ██
        ██████     ██    ██      ██   ██ ███████ ███████
                                                          
                                                                                                                                                                                       
	Tokens must already be in the server!
""")
#I was going to add proxy support but decided if there are bad proxies etc id needa redo them and decided it'd make this too complicated, and I may as well make it a complete raid tool but that's already been done so yeahhhh



tokenfile = input(" > Token File Name? Include the extension!\n > ")


emojiurl = input("\n\n > Open up inspect element and go in network. \n > React on your account and you'll see a request in the Name Section.\n > It will be called  [%40me]  you can search that in filter and find it too!\n > Go to request url and copy a link that should look like\n > https://discord.com/api/v8/channels/123123123/messages/123123123/reactions/%A0%B1%C2%D3/%40me \n \n > ")

os.system("cls")
with open(tokenfile, 'r') as f:
    for line in f.readlines():
        token = line.strip()
        token = token.replace('"','')
        headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        a = requests.put(f"{emojiurl}", headers=headers, timeout=10).status_code
        if a == 204:
            count = count + 1
            print(" + Token Reacted!")
        else:
            print(" - Error Reacting")
        os.system(f"title Successful Reactions [{count}]")
input(f" + Finished -- Reactions Done [{count}]\n > ")


