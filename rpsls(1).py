#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�Ԭʫ��
���ڣ�2021��6��4��
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    else:
        return 4

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    pass #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "ֽ"
    elif number==3:
        return "����"
    else:
        return "����"
	     

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    global comp_num
    result=0
    player_num=name_to_number(player_choice)
    if player_num==0:
        if comp_num==0:
            result=0
        elif comp_num==1:
            result=-1
        elif comp_num==2:
            result=-1
        elif comp_num==3:
            result=1
        elif comp_num==4:
            result=1

		 
    elif player_num==1:
        if comp_num==0:
            result=1
        elif comp_num==1:
            result=0
        elif comp_num==2:
            result=-1
        elif comp_num==3:
            result=-1
        elif comp_num==4:
            result=1
			
    elif player_num==2:
        if comp_num==0:
            result=1
        elif comp_num==1:
            result=1
        elif comp_num==2:
            result=0
        elif comp_num==3:
            result=-1
        elif comp_num==4:
            result=-1

    elif player_num==3:
        if comp_num==0:
            result=-1
        elif comp_num==1:
            result=1
        elif comp_num==2:
            result=1
        elif comp_num==3:
            result=0
        elif comp_num==4:
            result=-1
			
    else:
        if comp_num==0:
            result=-1
        elif comp_num==1:
            result=-1
        elif comp_num==2:
            result=1
        elif comp_num==3:
            result=1
        elif comp_num==4:
            result=0
			
    if result==0:
        print("���ͼ��������һ����")
    elif result==1:
        print("��Ӯ��")
    else:
        print("�����Ӯ��")


		
	 


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
comp_num=random.randrange(0,4)
comp_choice=number_to_name(comp_num)
print(f"����ѡ����: {choice_name}")
print(f"�������ѡ����: {comp_choice}")
rpsls(choice_name)


