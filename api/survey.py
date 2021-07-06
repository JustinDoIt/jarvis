
import pandas as pd


import argparse

def test_01():
    import sys 
    sys.path.append("../../friday")
    from pubmed_query import query_pubmed, fetch_articles

    # get query language
    query = '("Nature biotechnology"[Journal]) AND (("2020/01/01"[Date - Publication] : "2020/12/31"[Date - Publication]))'
    # search PubMed using query
    id_list = query_pubmed(query)
    # fetch paper information using pmids
    df = fetch_articles(id_list[:5]) 





# def parse_args():
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument('--keywords', '-k', help='the keywords to query the PubMed', required=True)
# 	parser.add_argument('--out', '-o', help='output csv file name', required=False)
# 	parser.add_argument('--verb', '-v', help='(optional) shows program progress', default=False, required=False)
# 	# parser.add_argument("--help", '-h', description="")
# 	return parser.parse_args()
	

# def main():
# 	args = parse_args()
# 	seqs_df = _parse_fasta(args.fasta)
# 	if args.out:
# 		easy_synthesis_with_seqs(seqs_df, save_path=args.out) # 指定输出
# 	else:
# 		easy_synthesis_with_seqs(seqs_df) # 默认输出文件为 tmp.csv


def _search_pubmed(query):
    query = input("Please input your query, enter 0 to see example")
    if query == "0":
        print("query can be the following format:")
        print("\t\t ")
        print("\t\t gene editing")


def main():
    user = {
        "zhangjq": "nichishima",
        "cuimengfei": "123456",
        "yangxue": "111"
    }
    print("===============================================")
    print("Welcome to JARVIS(Just A Research Versatile Intelligence Service) program.")
    username = input("Please input your username")
    print("===============================================")
    while True:
        print("===============================================")
        print("Welcome, sir")
        print("1. search PubMed")
        print("2. manage literature")
        print("3. ")
        print("0. quit")
        option = input("what can I do for you? sir")
        print("===============================================")
        if option == "1":
            print("query finished!")
        elif option == "2":
            print("manage out")


def hello_world_1():
    print(r"""
______/\\\\\\\\\\\_____/\\\\\\\\\_______/\\\\\\\\\______/\\\________/\\\__/\\\\\\\\\\\_____/\\\\\\\\\\\___        
 _____\/////\\\///____/\\\\\\\\\\\\\___/\\\///////\\\___\/\\\_______\/\\\_\/////\\\///____/\\\/////////\\\_       
  _________\/\\\______/\\\/////////\\\_\/\\\_____\/\\\___\//\\\______/\\\______\/\\\______\//\\\______\///__      
   _________\/\\\_____\/\\\_______\/\\\_\/\\\\\\\\\\\/_____\//\\\____/\\\_______\/\\\_______\////\\\_________     
    _________\/\\\_____\/\\\\\\\\\\\\\\\_\/\\\//////\\\______\//\\\__/\\\________\/\\\__________\////\\\______    
     _________\/\\\_____\/\\\/////////\\\_\/\\\____\//\\\______\//\\\/\\\_________\/\\\_____________\////\\\___   
      __/\\\___\/\\\_____\/\\\_______\/\\\_\/\\\_____\//\\\______\//\\\\\__________\/\\\______/\\\______\//\\\__  
       _\//\\\\\\\\\______\/\\\_______\/\\\_\/\\\______\//\\\______\//\\\________/\\\\\\\\\\\_\///\\\\\\\\\\\/___ 
        __\/////////_______\///________\///__\///________\///________\///________\///////////____\///////////_____
    """)

def hello_world_2():
    print("""
    

     ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
     ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
     ██║███████║██████╔╝██║   ██║██║███████╗
██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
                                            

    """)
def hello_world_3():
    print("""

 ▄▄▄██▀▀▀▄▄▄       ██▀███   ██▒   █▓ ██▓  ██████ 
   ▒██  ▒████▄    ▓██ ▒ ██▒▓██░   █▒▓██▒▒██    ▒ 
   ░██  ▒██  ▀█▄  ▓██ ░▄█ ▒ ▓██  █▒░▒██▒░ ▓██▄   
▓██▄██▓ ░██▄▄▄▄██ ▒██▀▀█▄    ▒██ █░░░██░  ▒   ██▒
 ▓███▒   ▓█   ▓██▒░██▓ ▒██▒   ▒▀█░  ░██░▒██████▒▒
 ▒▓▒▒░   ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░
 ▒ ░▒░    ▒   ▒▒ ░  ░▒ ░ ▒░   ░ ░░   ▒ ░░ ░▒  ░ ░
 ░ ░ ░    ░   ▒     ░░   ░      ░░   ▒ ░░  ░  ░  
 ░   ░        ░  ░   ░           ░   ░        ░  
                                ░                

    
    """)

def hello_world_4():
    print("""
      _   _    ______     _____ ____  
     | | / \  |  _ \ \   / /_ _/ ___| 
  _  | |/ _ \ | |_) \ \ / / | |\___ \ 
 | |_| / ___ \|  _ < \ V /  | | ___) |
  \___/_/   \_\_| \_\ \_/  |___|____/ just a research versatile intelligence service
                                      
    """)

def hello_world_5():
    print("""
      ##    ###    ########  ##     ## ####  ######  
      ##   ## ##   ##     ## ##     ##  ##  ##    ## 
      ##  ##   ##  ##     ## ##     ##  ##  ##       
      ## ##     ## ########  ##     ##  ##   ######  
##    ## ######### ##   ##    ##   ##   ##        ## 
##    ## ##     ## ##    ##    ## ##    ##  ##    ## 
 ######  ##     ## ##     ##    ###    ####  ######  
    
    """)

def hello_world_6():
    print("""
  888888        d8888 8888888b.  888     888 8888888 .d8888b.  
    "88b       d88888 888   Y88b 888     888   888  d88P  Y88b 
     888      d88P888 888    888 888     888   888  Y88b.      
     888     d88P 888 888   d88P Y88b   d88P   888   "Y888b.   
     888    d88P  888 8888888P"   Y88b d88P    888      "Y88b. 
     888   d88P   888 888 T88b     Y88o88P     888        "888 
     88P  d8888888888 888  T88b     Y888P      888  Y88b  d88P 
     888 d88P     888 888   T88b     Y8P     8888888 "Y8888P"  
   .d88P                                                       
 .d88P" just a research versatile intelligence service                                                       
888P"                                                        
    """)


def hello_world_7():
    print("""
      _   _    ______     _____ ____  
     | | / \  |  _ \ \   / /_ _/ ___| 
  _  | |/ _ \ | |_) \ \ / / | |\___ \ 
 | |_| / ___ \|  _ < \ V /  | | ___) |
  \___/_/   \_\_| \_\ \_/  |___|____/   
    """)


                                                   

def hello_world_8():
    print(r"""
 _____  ______  ____    __  __  ______  ____       
/\___ \/\  _  \/\  _`\ /\ \/\ \/\__  _\/\  _`\     
\/__/\ \ \ \L\ \ \ \L\ \ \ \ \ \/_/\ \/\ \,\L\_\   
   _\ \ \ \  __ \ \ ,  /\ \ \ \ \ \ \ \ \/_\__ \   
  /\ \_\ \ \ \/\ \ \ \\ \\ \ \_/ \ \_\ \__/\ \L\ \ 
  \ \____/\ \_\ \_\ \_\ \_\ `\___/ /\_____\ `\____\
   \/___/  \/_/\/_/\/_/\/ /`\/__/  \/_____/\/_____/
    
    """)
if __name__ == "__main__":
    hello_world_1()
    hello_world_2()
    hello_world_3()
    hello_world_4()
    hello_world_5()
    hello_world_6()
    hello_world_7()
    hello_world_8()
    # main()