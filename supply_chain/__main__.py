from block import Block
from block_chain import BlockChain
from stakeholders_credentials import stakeholders
from products import products
import numpy as np

block_chain = BlockChain(Block)
# print(block_chain.chain)

# last_block = block_chain.last_block
# last_proof_no = last_block.proof_no
# proof_no = block_chain.proof_of_work(last_proof_no)
# data = 'Bob Geldof'
# last_hash = last_block.calculate_hash()
# new_block = block_chain.construct_block(proof_no, last_hash, data)
# print(block_chain.chain)

def addBlock(data):
    last_block = block_chain.last_block
    last_proof_no = last_block.proof_no
    proof_no = block_chain.proof_of_work(last_proof_no)
    data = data
    last_hash = last_block.calculate_hash()
    new_block = block_chain.construct_block(proof_no, last_hash, data)
    print(block_chain.chain)

def shipToManufacturer(prod, username):
    prod['orderId'] = np.random.randint(10000)
    p = prod.copy()
    p['shipped to']='manufacturer'
    p['owner']=username
    addBlock(p)

def shipToDistributor(prod, username):
    p = prod.copy()
    p['shipped to']='distributor'
    addBlock(p)

def shipToOwner(prod, username):
    p = prod.copy()
    p['shipped to']='owner'
    addBlock(p)

def Login():
    login = False
    username = None
    usertype = None
    while not login:
        print("\t----login----")
        print("username:")
        username = input()
        if username == 'exit':
            exit()
        print("\npassword:")
        password = input()
        for stake_h in stakeholders:
            if(stake_h['username']==username and stake_h['password']==password):
                print("logged in succesfully!")
                usertype = stake_h['type']
                login = True
                break
        if not login:
            print("try again")
    return (username, usertype)

def showOrders(username):
    orders = []
    blocks_data = []
    for block in reversed(block_chain.chain):
        #check validity
        if block.data != 0:
            block_chain.check_validity(block, block_chain.chain[block.index - 1])
        if block.data != 0 and block.data["owner"] == username:
            found = False
            for (id_,name) in orders:
                if id_==block.data["orderId"]:
                    found = True
                    break
            if found==False:
                orders.append((block.data["orderId"],block.data["name"]))
                blocks_data.append(block.data)   
    for o in orders:
        (id_ , name) = o
        print(id_,'\t',name)
    return blocks_data

def trackOrder(id_):
    track_route = []
    for block in reversed(block_chain.chain):
        if block.data != 0 and str(block.data["orderId"]) == id_:
            data = block.data.copy()
            data["time"] = block.timestamp
            track_route.append(data)
    while track_route:
        route = track_route.pop()
        print(route["orderId"],"\t",route["time"],"\tshipped to: ",route["shipped to"])
def userMenu(username):
    while True:
        print(
            "\n1. show orders\n2. show products\n3. track order"
        )
        option = input()
        if option == '1':
            showOrders(username)
        elif option == '2':
            for prod in products:
                print(prod['name'],'\t\t',prod['id'],'\n')
            print('\nenter ID of product you want to purchase:\n')
            id_ = input()
            for prod in products:
                if id_ == prod['id']:
                    shipToManufacturer(prod, username)
                    print('order for ',prod,' has been placed!')
        elif option == '3':
            data =showOrders(username)
            print("enter order ID you want to track:")
            id_ = input()
            trackOrder(id_)

        elif option == 'exit':
            return

def showManufacturing():
    shipped = []
    manufacturing = []
    blocks_data = []
    for block in reversed(block_chain.chain):
        #check validity
        if block.data != 0:
            block_chain.check_validity(block, block_chain.chain[block.index - 1])
        if block.data != 0 and (block.data["shipped to"] == "distributor" or block.data["shipped to"] == "owner"):
            shipped.append(block.data["orderId"])
        elif block.data != 0 and block.data["orderId"] not in shipped:
            blocks_data.append(block.data)
            manufacturing.append((block.data["orderId"], block.data["name"]))
    for m in manufacturing:
        (id_,name) = m
        print(id_,"\t",name)
    return blocks_data


def showDistrubution():
    shipped = []
    distributing = []
    blocks_data = []
    for block in reversed(block_chain.chain):
        #check validity
        if block.data != 0:
            block_chain.check_validity(block, block_chain.chain[block.index - 1])
        if block.data != 0 and (block.data["shipped to"] == "owner"):
            shipped.append(block.data["orderId"])
        elif block.data != 0 and block.data["shipped to"]=='distributor' and block.data["orderId"] not in shipped:
            blocks_data.append(block.data)
            distributing.append((block.data["orderId"], block.data["name"]))
    for d in distributing:
        (id_,name) = d
        print(id_,"\t",name)
    return blocks_data

def manufacturerMenu():
    while True:    
        print(
            "\n1. show orders in manufacturing\n2. ship product to distributor"
        )
        option = input()
        if option == '1':
            showManufacturing()
        elif option == "2":
            data = showManufacturing()
            id_ = input()
            for prod in data:
                if str(prod['orderId']) == id_:
                    shipToDistributor(prod,id_)
        elif option == "exit":
            break

def distributorMenu():
    while True:    
        print(
            "\n1. show orders in distribution\n2. ship product to owner"
        )
        option = input()
        if option == '1':
            showDistrubution()
        elif option == "2":
            data = showDistrubution()
            id_ = input()
            for prod in data:
                if str(prod['orderId']) == id_:
                    shipToOwner(prod,id_)
        elif option == "exit":
            break

while True:
    username, usertype = Login()
    if usertype == 'user':
        userMenu(username)
    elif usertype == 'manufacturer':
        manufacturerMenu()
    elif usertype == 'distributor':
        distributorMenu()
