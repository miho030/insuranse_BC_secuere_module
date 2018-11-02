# -*- coding: utf-8 -*-

"""
I am the Chairman of SeaHawk Certified by KISA.

This code is Made By SeaHawk, the Computer security Club of
KyungBok University, Lee.JoonSung, Lee.HyuckJoon, Lee ji sub

This Script is designed to help classify insurance fraud.
for, support any insurance accountant's work

이 스크립트는 보험사기를 판별해내는 "보험종합설계자"의 업무를 돕기 위해 작성된 스크립트입니다.
블록체인으로 구현되며, 블록 데이터는 보험회사가 어떤 가입자의 명의로 수취인이 얼마만큼을 가져갔는지에 대하여 정의되어 있습니다.
Costermer.txt파일 참조.

기본값은 *.txt가 아닌 *.md파일입니다.

"""


# 서버 제공을 위한 flask 라이브러리 선언
from flask import Flask
from flask import request
# POST, GET등의 코드를 받아오기 위해서 사용
import json
import os
# 암호화를 위한 hashlib 임포트
import hashlib as hasher
# Genesis Block 생성, previous block 생성을 위한 날짜 모듈 임포트
import datetime as date
node = Flask(__name__)

#UI

print "#####################################################################"
print "#                                                                   #"
print "#             [ BlockChain Insurence Trading SECURE ]               #"
print "#                                                                   #"
print "#                                                                   #"
print "#                                           made by SeaHawk.TEAM    #"
print "#                          Lee.JoonSung, Lee.HyuckJoon, Lee.JiSub   #"
print "#                                                                   #"
print "#                 (C) Coypyright by SeaHawk, 2018                   #"
print "#####################################################################"


# 입력받은 값 검증을 위한 함수
def inputFilter(add_value):
    if add_value.isalpha() == True or add_value == '':
        return True
    else:
        return False

# 가입한 보험회사 이름
add_DB_Insur = raw_input("Name of the insurance company you joined: ")
# 보험금 수취자
add_DB_reciper = raw_input("What is your name?: ")
# 보험 가입자
add_DB_acount = raw_input("Who is Insurence Subscriber?: ")
# 총 지급 금액
# add_DB_price = accident_price

# DB 업데이트를 위한 입력값 검증 절차.
# 문자열을 받아오지 않기 때문에, 입력받아온 변수의 내용이 문자열인지, 숫자열인지 처리함.
while (True):
    add_value_price = raw_input("Write down the amount of insurance you have subscribed to every month: ")
    if inputFilter(add_value_price) == True:
        print "\n[!]", "Input Value is incorrect, Please input data using integer"
    else:
        print "[+]", " Correct Value is Entered! Thx! XD"
        break

while (True):
    add_value_date = raw_input("Please write down the month when you had an accident: ")
    if inputFilter(add_value_date) == True:
        print "\n[!]","Input Value is incorrect, Please input data using integer"
    else:
        print " Correct Value is Entered! Thx! XD"
        break

# 거래 장부 업데이트를 위한 정의
sum_vaule = add_value_price * 12
# 사고난 달을 기준으로 -1달 하여 처리함.
# 이유: 12개월간 5천원씩 보험금을 납부하였다. 헌데, 5월에 사고가 났다. 5월 보험금은 아직 미납이니, 4월까지만 납부 처리.
accident_date = int(add_value_date) - 1
accident_price = int(accident_date) * int(add_value_price)
# 아래 선언은, 보험 거래 장부 수정행위를 구현하기 위해서 생성했다.
add_DB_price = accident_price

print "#####################################################################"
print "#                                                                   #"
print "#                                                                   #"
print "          Great! your Accident_date is: ", add_value_date
print "          your Intsurence fee is: ", add_value_price
print "          So, your recive will be based at: ", accident_price
print "          Because, you're last monthly insurence fee is: ",accident_date
print "#                                                                   #"
print "#                                                                   #"
print "#####################################################################"



# 보험 거래 장부 임포트
# 앞의 받은 데이터는 새로운 데이터 생성을 하기 위해서
# DB가 수정되는 행위를 대신 해주는 모듈을 구축하기 위함이다.

# 이하 코드는 DB를 자동으로, 지속적으로 수정을 하기 위함이다. -> UI관련 모듈
f = open('Customer.txt', 'at')
data = [add_DB_Insur,":",add_DB_reciper,":",add_DB_acount,":",add_value_price]
# f.write(data)
f.close()

# 마이닝 주소 -> 필요 없는 기능이기에 따로 아이디어를 짜봐야한다...
# 디폴트 값은 보험사에서 회계사가 사용할 수 있도록 마이너 주소를 알려주면 될듯하다.
miner_adress = raw_input("write down about your Miner-Address. if you don't have it, Enter ' [A] ': ")


""" 
Structure of Block, Definition; 블록의 구조를 정의한다.
이 클래스 구조체는 Block이 어떻게 생겼는지 정의해준다.
"""

class Block:
    # 시작선언으로, 이 스크립트는 다음 형식을 항상 숙지해야 한다.
    # 다음 함수는 블록의 구성을 정의한다.

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index # 블록의 인덱스; 정보, 순번 등
        self.timestamp = timestamp # Next Block 생성을 위한 타임스탬프,; time.thistime.now()를 통해서 임포트한다.
        self.data = data # 블록체인에 구현될 내부 테이터
        self.previous_hash = previous_hash # 이전 블록 정의
        self.hash = self.hash_block() # 데이터 및 이전 블록의 해시를 암호화하는 해시에 대한 정의


    # 블록 암호화에 대한 정의;
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        return sha.hexdigest()

"""
Create/Definition of Genesis Block
"""
# 제네시스 블록; 기원 블록
def create_genesis_block():

    # 값 0 설정을 통해 기원 블록의 특성을 정의하고, 매뉴얼하게 구성한다.
    return Block(0, date.datetime.now(), {
        "proof-of-work": 9,
        "transactions": None
    }, "0")


"""
바로 밑의 함수는 기원 블록에서 후속 블록을 연속적으로 생성하는 함수이다.
이 함수는 체인구조에서 이전 블록을 매개변수로 사용하여 새로 생성될 블록을 만들고,
해당 데이터에 기반한 새 블록을 반환하는 함수이다.
다음 함수는 암화화 증명 역활을 하게 된다. 이 함수를 통해 과거 정보의 수정으로 인한 체인구조의
붕괴를 예방할 수 있다. 새로운 블록이 이전 블록의 정보를 해시할 때, 무결성은 새로운 블록이 생길 때마다 증가하기 때문.
"""
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "I Love Foxes" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

"""
다음 소스는 블록체인 구조화 후, 블록체인을 배분하는 코드이다.
해당 코드를 통해 앞의 함수가 적당하게 실행이 되었는지 알 수 있다.
"""
# 블록체인 테스트 실험
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 2

#for문을 이용하여 30개의 블록을 테스트로 뽑아내보자
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    previous_block = block_to_add
    print "Block #{} has been to the blockchain(For Testing! I Love Fox!!)".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)

# A completely random address of the owner of this node
# 현재 서버의 스크립트 실행인이 가지는 완전히 랜덤한 주소
# 기본적인 체인 형태를 정의해줌.
blockchain = []
blockchain.append(create_genesis_block())

# 이 노드는 트랜잭션을 가지고 있으며,
# 아래 빈 리스트에 들어갈 것이다.
this_nodes_transactions = []

# url 데이터와 모든 다른 노드와의 네트워크를 저장하는 빈 리스트
# 각 노드들과 서버가 통신하기 위한 필수 선언
peer_nodes = []

# 우리가 채굴을 하거나, 하지 않거나, 모든 상황에 적용될 수 있는 다양한 결정권
mining = True


@node.route('/txion', methods=['POST'])
def transaction():
    # 만약 들어온 요청이 POST 요청이라면,
    # 트랜잭션 데이터를 풀고 확인한다.
    new_txion = request.get_json()
    # 그라만, 이 리스트에 해당 트랜잭션 값을 넣는다.
    this_nodes_transactions.append(new_txion)
    # Because the transaction was successfully
    # submitted, we log it to our console
    print "새로운 트랜젝션이 생성되었습니다."
    print "~로부터 송신됨 : {}".format(new_txion['from'].encode('ascii','replace'))
    print "~가 수신받음 : {}".format(new_txion['to'].encode('ascii', 'replace'))
    print "용량 : {}\n".format(new_txion['amount'])

    return "[!]트랜젝션 수신 완료!\n"


@node.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain
    # Convert our blocks into dictionaries
    # 그간 노드가 가지고 있었던 블록들을 변한하기 위한 사전
    # 그래야 좀 있다가 사용될 Json Object processing에 사용할 수 있다.
    for i in range(len(chain_to_send)):
        block = chain_to_send[i]
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        chain_to_send[i] = {
            "index": block_index,
            "timestamp": block_timestamp,
            "data": block_data,
            "hash": block_hash
        }
    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send


def find_new_chains():
    # 모든 노드로부터 모든 블록 걷어오기
    other_chains = []
    for node_url in peer_nodes:
        # 각 노드에 저장되어 있는 블록을 GET 요청을 통해 가져오기.
        block = requests.get(node_url + "/blocks").content

        # Jown object를 파이썬 사전으로 변환한다.
        block = json.loads(block)
        #변환된 데이터를 아래 리스트에 추가한다.
        other_chains.append(block)
    return other_chains


def consensus():
    # 다른 모든 노드로부터 모든 블록을 GET 요청을 통해 가져온다.
    other_chains = find_new_chains()
    # 만약, 가져온 블록들이 길지 않다면,
    # 길게 만들어서 저장해야한다.
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain
    # If the longest chain isn't ours,
    # then we stop mining and set
    # our chain to the longest one
    blockchain = longest_chain


def proof_of_work(last_proof):
    # 다음 POW 작업을 위해서 아래와 같은 변수 선언!!
    incrementor = last_proof + 1
    # 9로 분할 할 수 있을 때까지 계속 증가시킨다.
    # 이전 블록들을 전부 POW 작업에 사용한다.
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    # 만약에 해당 숫자가 찾아진다면,
    # 해당 값을 POW 작업에 사용할 수 있도록
    # 반환한다.
    return incrementor


@node.route('/mine', methods=['GET'])
def mine():
    # 이전에 작업했던 마이닝 기록을 가져온다.
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']

    proof = proof_of_work(last_proof)

    # 트랜잭션을 생성하는 것으로, 마이너는 보상을 받을 수 있다.
    this_nodes_transactions.append(
        {"from": "network", "to": miner_address, "amount": 1}
    )
    # 새로운 블록 생성하는 부분
    new_block_data = {
        "proof-of-work": proof,
        "transactions": list(this_nodes_transactions)
    }
    new_block_index = last_block.index + 1
    new_block_timestamp = this_timestamp = date.datetime.now()
    last_block_hash = last_block.hash
    this_nodes_transactions[:] = []

    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )
    blockchain.append(mined_block) # 체인 생성
    # Json관련 선언들
    return json.dumps({
        "index": new_block_index,
        "timestamp": new_block_timestamp,
        "data": new_block_data,
        "hash": last_block_hash
    }) + "\n"

node.run()

""" 
Structure of Block, Definition; 블록의 구조를 정의한다.
이 클래스 구조체는 Block이 어떻게 생겼는지 정의해준다.
"""

class Block:
    # 시작선언으로, 이 스크립트는 다음 형식을 항상 숙지해야 한다.
    # 다음 함수는 블록의 구성을 정의한다.

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index # 블록의 인덱스; 정보, 순번 등
        self.timestamp = timestamp # Next Block 생성을 위한 타임스탬프,; time.thistime.now()를 통해서 임포트한다.
        self.data = data # 블록체인에 구현될 내부 테이터
        self.previous_hash = previous_hash # 이전 블록 정의
        self.hash = self.hash_block() # 데이터 및 이전 블록의 해시를 암호화하는 해시에 대한 정의


    # 블록 암호화에 대한 정의;
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        return sha.hexdigest()

"""
Create/Definition of Genesis Block
"""
# 제네시스 블록; 기원 블록
def create_genesis_block():

    # 값 0 설정을 통해 기원 블록의 특성을 정의하고, 매뉴얼하게 구성한다.
    return Block(0, date.datetime.now(), {
        "proof-of-work": 9,
        "transactions": None
    }, "0")

"""
바로 밑의 함수는 기원 블록에서 후속 블록을 연속적으로 생성하는 함수이다.
이 함수는 체인구조에서 이전 블록을 매개변수로 사용하여 새로 생성될 블록을 만들고,
해당 데이터에 기반한 새 블록을 반환하는 함수이다.
다음 함수는 암화화 증명 역활을 하게 된다. 이 함수를 통해 과거 정보의 수정으로 인한 체인구조의
붕괴를 예방할 수 있다. 새로운 블록이 이전 블록의 정보를 해시할 때, 무결성은 새로운 블록이 생길 때마다 증가하기 때문.
"""

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "I LOVE Fox!!" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

"""
다음 소스는 블록체인 구조화 후, 블록체인을 배분하는 코드이다.
해당 코드를 통해 앞의 함수가 적당하게 실행이 되었는지 알 수 있다.
"""
# 블록체인 테스트 실험
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 2

#for문을 이용하여 30개의 블록을 테스트로 뽑아내보자
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    previous_block = block_to_add
    print "Block #{} has been to the blockchain(For Testing! I Love Fox!!)".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)

# A completely random address of the owner of this node
# 현재 서버의 스크립트 실행인이 가지는 완전히 랜덤한 주소
# 기본적인 체인 형태를 정의해줌.
blockchain = []
blockchain.append(create_genesis_block())

# 이 노드는 트랜잭션을 가지고 있으며,
# 아래 빈 리스트에 들어갈 것이다.
this_nodes_transactions = []

# url 데이터와 모든 다른 노드와의 네트워크를 저장하는 빈 리스트
# 각 노드들과 서버가 통신하기 위한 필수 선언
peer_nodes = []

# 우리가 채굴을 하거나, 하지 않거나, 모든 상황에 적용될 수 있는 다양한 결정권
mining = True


@node.route('/txion', methods=['POST'])
def transaction():
    # 만약 들어온 요청이 POST 요청이라면,
    # 트랜잭션 데이터를 풀고 확인한다.
    new_txion = request.get_json()
    # 그라만, 이 리스트에 해당 트랜잭션 값을 넣는다.
    this_nodes_transactions.append(new_txion)
    # Because the transaction was successfully
    # submitted, we log it to our console
    print "새로운 트랜젝션이 생성되었습니다."
    print "~로부터 송신됨 : {}".format(new_txion['from'])
    print "~가 수신받음 : {}".format(new_txion['to'])
    print "용량 : {}\n".format(new_txion['amount'])

    return "[!]트랜젝션 수신 완료!\n"


@node.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain
    # Convert our blocks into dictionaries
    # 그간 노드가 가지고 있었던 블록들을 변한하기 위한 사전
    # 그래야 좀 있다가 사용될 Json Object processing에 사용할 수 있다.
    for i in range(len(chain_to_send)):
        block = chain_to_send[i]
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        chain_to_send[i] = {
            "index": block_index,
            "timestamp": block_timestamp,
            "data": block_data,
            "hash": block_hash
        }
    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send


def find_new_chains():
    # 모든 노드로부터 모든 블록 걷어오기
    other_chains = []
    for node_url in peer_nodes:
        # 각 노드에 저장되어 있는 블록을 GET 요청을 통해 가져오기.
        block = requests.get(node_url + "/blocks").content

        # Jown object를 파이썬 사전으로 변환한다.
        block = json.loads(block)
        #변환된 데이터를 아래 리스트에 추가한다.
        other_chains.append(block)
    return other_chains


def consensus():
    # 다른 모든 노드로부터 모든 블록을 GET 요청을 통해 가져온다.
    other_chains = find_new_chains()
    # 만약, 가져온 블록들이 길지 않다면,
    # 길게 만들어서 저장해야한다.
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain
    # If the longest chain isn't ours,
    # then we stop mining and set
    # our chain to the longest one
    blockchain = longest_chain


def proof_of_work(last_proof):
    # 다음 POW 작업을 위해서 아래와 같은 변수 선언!!
    incrementor = last_proof + 1
    # 9로 분할 할 수 있을 때까지 계속 증가시킨다.
    # 이전 블록들을 전부 POW 작업에 사용한다.
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    # 만약에 해당 숫자가 찾아진다면,
    # 해당 값을 POW 작업에 사용할 수 있도록
    # 반환한다.
    return incrementor


@node.route('/mine', methods=['GET'])
def mine():
    # 이전에 작업했던 마이닝 기록을 가져온다.
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']

    proof = proof_of_work(last_proof)

    # 트랜잭션을 생성하는 것으로, 마이너는 보상을 받을 수 있다.
    this_nodes_transactions.append(
        {"from": "network", "to": miner_address, "amount": 1}
    )
    # 새로운 블록 생성하는 부분
    new_block_data = {
        "proof-of-work": proof,
        "transactions": list(this_nodes_transactions)
    }
    new_block_index = last_block.index + 1
    new_block_timestamp = this_timestamp = date.datetime.now()
    last_block_hash = last_block.hash
    this_nodes_transactions[:] = []

    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )
    blockchain.append(mined_block) # 체인 생성
    # Json관련 선언들
    return json.dumps({
        "index": new_block_index,
        "timestamp": new_block_timestamp,
        "data": new_block_data,
        "hash": last_block_hash
    }) + "\n"

node.run()
