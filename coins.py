import random
#����������� ������� � ���������� ��������
coins_counter = int(input ("���������� �����? "))
coins = []
while coins_counter > 0:
	random_one = round(random.random())
	if random_one == 1:
		coins.append("�")
	else:
		coins.append("�")
	coins_counter = coins_counter - 1

print (coins)

counter1 = 0
counter2 = 0
for coin in coins:
	if coin == "�":
		counter1 = counter1 + 1
	if coin == "�":
		counter2 = counter2 + 1
#� ��������� ������ ������� ����������� ���������� �����		
flip_counts = str(min(counter1, counter2))

ru = ""
if ((flip_counts[-1] == "1" and len(flip_counts) == 1) or (flip_counts[-1] == "1" and len(flip_counts) >= 1 and flip_counts[-2] != "1")):
    ru = "�"
if ((flip_counts[-1] in  ["2", "3", "4"] and len(flip_counts) == 1) or (flip_counts[-1] in  ["2", "3", "4"] and len(flip_counts) >= 1 and flip_counts[-2] != "1")):
    ru = "�"
print('����� ����������� ������� ' + flip_counts + " �����" + ru)