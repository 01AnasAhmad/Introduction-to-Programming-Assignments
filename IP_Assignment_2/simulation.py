# Name - Anas Ahmad
# Roll No - 2020023
"""
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.
- DO NOT modify/delete the given functions.
- DO NOT import any python libraries. You may only import a2.py.
- Make sure to return value as specified in the function description.
- Remove the pass statement from the function when you implement it.
- Do not create any global variables in this module.
"""
from a2 import *


def main():
    print("Hello Programmer ! Welcome.Please Note for Funtionality to work you first")
    print("Need to Enter 1 as Query ! Menu of Program is as follows:- ")
    print("---------------------------------------------------------------------------")
    print("-----------------------MENU BAR FOR DIFFERENT QUERIES:---------------------")
    print("---------------------------------------------------------------------------")
    print("|Query code|| Function Name                ||Parameters||")
    print("     1 --    READ DATA FROM FILE             Records                       ")
    print("     2 --    FILTER BY FIRST NAME            Records,First Name            ")
    print("     3 --    FILTER BY LAST NAME             Records,Last Name             ")
    print("     4 --    FILTER BY FULL NAME             Records,Full Name             ")
    print("     5 --    FILTER BY AGE RANGE             Records,Min Age,Max Age       ")
    print("     6 --    COUNT BY GENDER                 Records                       ")
    print("     7 --    FILTER BY ADDRESS               Records,Address               ")
    print("     8 --    FIND ALUMNI                     Records,Institute Name        ")
    print("     9 --    FIND TOPPER OF EACH INSTITUTE   Records                       ")
    print("     10--    FIND BLOOD DONORS               Records,Person ID             ")
    print("     11--    GET COMMON FRIENDS              Records,List of person ID     ")
    print("     12--    IS RELATED                      Records,Person ID,Friend ID   ")
    print("     13--    DELETE BY ID                    Records,Person ID             ")
    print("     14--    ADD FRIEND                      Records,Person ID,Friend ID   ")
    print("     15--    REMOVE FRIEND                   Records,Person ID,Friend ID   ")
    print("     16--    ADD EDUCATION                   Records,Person ID ,Institute Name,")
    print("                                             Ongoing,Percentage           ")
    flag = 0
    flag2 = 0
    while True:
        if flag2 == 0:
            id_code = int(input("Enter the ID code to Read the Records:"))
            flag2 = 1
        else:
            id_code = int(input("Enter The Query :"))
        if id_code == -1:
            print("You are exiting the Functionality !")
            break
        elif id_code == 1:
            record = read_data_from_file(file_path="data.json")
            flag = 1
            print("You Now Have Read The Records")

        elif flag == 1:
            if id_code == 2:
                print("2 -- FILTER BY FIRST NAME")
                fname = input("Enter First Name:")
                print(filter_by_first_name(record, fname))
            elif id_code == 3:
                print("3 -- FILTER BY LAST NAME")
                lname = input("Enter Last Name:")
                print(filter_by_last_name(record, lname))
            elif id_code == 4:
                fullname = input("Enter Full Name:")
                print("4 -- FILTER BY FULL NAME")
                print(filter_by_full_name(record, fullname))
            elif id_code == 5:
                print("5 -- FILTER BY AGE RANGE")
                minage = int(input("Enter Min Age:"))
                maxage = int(input("Enter Max Age:"))
                print(filter_by_age_range(record, minage, maxage))
            elif id_code == 6:
                print("6 -- COUNT BY GENDER")
                print(count_by_gender(record))
            elif id_code == 7:
                print("7 -- FILTER BY ADDRESS")
                add = {}
                hno = input("enter house number :")
                if len(hno) != 0:
                    add["house_no"] = int(hno)
                blck = input("enter block number:")
                if len(blck) != 0:
                    add["block"] = blck
                twn = input("enter the town:")
                if len(twn) != 0:
                    add["town"] = twn
                cty = input("enter the city")
                if len(cty) != 0:
                    add["city"] = cty
                ste = input("enter the state:")
                if len(ste) != 0:
                    add["state"] = ste
                pin = input("enter pincode:")
                if len(pin) != 0:
                    add["pincode"] = pin
                print(filter_by_address(record, add))
            elif id_code == 8:
                print("8 -- FIND ALUMNI")
                inn = input("Enter The Institute Name:")
                print(find_alumni(record, inn))
            elif id_code == 9:
                print("9 -- FIND TOPPER OF EACH INSTITUTE")
                print(find_topper_of_each_institute(record))
            elif id_code == 10:
                print("10-- FIND BLOOD DONORS")
                receiver_person = int(input("Enter Receiver Person's ID:"))
                print(find_blood_donors(record, receiver_person))
            elif id_code == 11:
                print("11-- GET COMMON FRIENDS")
                print("Enter ID Codes in space separated manner:")
                print("It Should be in the Records else it will be removed")
                lis_d2 = list(map(int, input().rstrip().split()))
                print(get_common_friends(record, lis_d2))
            elif id_code == 12:
                print("12-- IS RELATED")
                a = int(input("Enter person 1 ID"))
                b = int(input("Enter person 2 ID"))
                print(is_related(record, a, b))
            elif id_code == 13:
                print("13-- DELETE BY ID")
                per_id = int(input("enter person's ID to delete record:"))
                record = delete_by_id(record, per_id)
                print("RECORD DELETED!")
            elif id_code == 14:
                print("14-- ADD FRIEND")
                per1_id = int(input("Enter person ID:"))
                fr_id = int(input("Enter Friend's ID:"))
                record = add_friend(record, per1_id, fr_id)
                print("PERSON ADDED!")
            elif id_code == 15:
                print("15-- REMOVE FRIEND")
                per2_id = int(input("Enter Person's ID:"))
                fr1_id = int(input("Enter Friend's ID:"))
                record = remove_friend(record, per2_id, fr1_id)
                print("FRIEND REMOVED!")
            elif id_code == 16:
                per3_id = int(input("Enter Person's ID:"))
                instt = int(input("Enter the INSTITUTE NAME:"))
                ongoings = input("Enter Boolean Value:")
                if ongoings:
                    percentages = 0
                else:
                    percentages = float(input("Enter Percentage:"))
                print(add_education(record, per3_id, instt, ongoings, percentages))


if __name__ == '__main__':
    main()
