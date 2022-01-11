"""
- This is the skeleton code, wherein you have to write the logic for each of the functions defined below.
- Feel free to add new helper functions, but DO NOT modify/delete the given functions.
- You MUST complete the functions defined below, except the ones that are already defined.
"""
'''
	Description: Prints the menu as shown in the PDF
	Parameters: No parameters
	Returns: No return value
'''
def show_menu():
	print("==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*=")
	print("                   MY BAZAAR                     ")
	print("==*==*==*==*==*==*==*==*==*==*==*==*==*==*===*==*")
	print("Hello! Welcome to my Grocery Store !")
	print("Following are the products available in the shop:")
	print('-------------------------------------------------')
	print('CODE | DESCRIPTION | CATEGORY    | COST(Rs)     |')
	print('-------------------------------------------------')
	print('  0  |   T shirt   | Apparels    | 500          |')
	print('  1  |   Trousers  | Apparels    |  600         | ')
	print('  2  |   Scarf     | Apparels    |  250         | ')
	print('  3  |   Smartphone| Electronics |  20,000      | ')
	print('  4  |   iPad      | Electronics |  30,000      | ')
	print('  5  |   Laptop    | Electronics |  50,000      | ')
	print('  6  |   Eggs      | Eatables    |  5           | ')
	print('  7  |   Chocolate | Eatables    |  10          | ')
	print('  8  |   Juice     | Eatables    |  100         | ')
	print('  9  |   Milk      | Eatables    |  45          | ')
	print('------------------------------------------------ ')
def get_regular_input():
	"""
	Description: Takes space separated item codes (only integers allowed).
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	Parameters: No parameters
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	"""
	item_code = list(map(int, input('Enter the item code(space-separated)::').rstrip().split()))
	b = 0
	qty = []
	while b < len(item_code):
		if 0 <= item_code[b] <= 9:
			qty.append(item_code[b])
		else:
			print(item_code[b], ':removed as it is not in the code list provided to you!')
			item_code.remove(item_code[b])
			b = b - 1
		b = b + 1
	count, count1, count2, count3, count4, count5, count6, count7, count8, count9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	for h in range(0, len(qty)):
		if qty[h] == 0:
			count = count + 1
		elif qty[h] == 1:
			count1 = count1 + 1
		elif qty[h] == 2:
			count2 = count2 + 1
		elif qty[h] == 3:
			count3 = count3 + 1
		elif qty[h] == 4:
			count4 = count4 + 1
		elif qty[h] == 5:
			count5 = count5 + 1
		elif qty[h] == 6:
			count6 = count6 + 1
		elif qty[h] == 7:
			count7 = count7 + 1
		elif qty[h] == 8:
			count8 = count8 + 1
		elif qty[h] == 9:
			count9 = count9 + 1
	l1 = [count, count1, count2, count3, count4, count5, count6, count7, count8, count9]
	print(l1)
	return l1
def get_bulk_input():
	"""
	Description: Takes inputs (only integers allowed) from a bulk buyer.
	For details, refer PDF. Include appropriate print statements to match
	the output with the screenshot provided in the PDF.
	Parameters: No parameters
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	"""
	count, count1, count2, count3, count4, count5, count6, count7, count8, count9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	while True:
		code = [int(code) for code in input('Enter code and quantity(leave blank to stop):').split()]
		if len(code) == 0:
			print('Your List Has Been Finalized')
			break
		elif 0 <= code[0] <= 9 and code[1] >= 0:
			if code[0] == 0:
				print('You Added ', code[1], 'Tshirt')
				count = count+code[1]
			elif code[0] == 1:
				print('You Added ', code[1], 'Trousers')
				count1 = count1 + code[1]
			elif code[0] == 2:
				print('You Added ', code[1], 'Scarf')
				count2 = count2 + code[1]
			elif code[0] == 3:
				print('You Added ', code[1], 'Smartphone')
				count3 = count3 + code[1]
			elif code[0] == 4:
				print('You Added ', code[1], 'iPad')
				count4 = count4 + code[1]
			elif code[0] == 5:
				print('You Added ', code[1], 'Laptop')
				count5 = count5 + code[1]
			elif code[0] == 6:
				print('You Added ', code[1], 'Eggs')
				count6 = count6 + code[1]
			elif code[0] == 7:
				print('You Added ', code[1], 'Chocolate')
				count7 = count7 + code[1]
			elif code[0] == 8:
				print('You Added ', code[1], 'Juice')
				count8 = count8 + code[1]
			elif code[0] == 9:
				print('You Added ', code[1], 'Milk')
				count9 = count9 + code[1]
		elif (code[0] < 0 or code[0] > 9) and code[1] > 0:
			print('Invalid Code.Try Again!')
		elif (code[0] < 0 or code[0] > 9) and code[1] < 0:
			print('Invalid code and quantity.Try Again!')
		elif code[1] < 0:
			print('Invalid Quantity.Try Again!')
	l2 = [count, count1, count2, count3, count4, count5, count6, count7, count8, count9]
	print(l2)
	return l2
def print_order_details(quantities):
	"""
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	Returns: No return value
	"""
	count = 0
	for e in range(0, len(quantities)):
		if quantities[e] > 0:
			if e == 0:
				count = count+1
				print(count, '.', 'T-shirt x ', quantities[e], '      Rs 500 *', quantities[e], '=', 500*quantities[e])
			elif e == 1:
				count = count+1
				print(count, '.', 'Trouser x ', quantities[e], '     Rs 600 *', quantities[e], '=', 600*quantities[e])
			elif e == 2:
				count = count + 1
				print(count, '.', 'Scarf x ', quantities[e], '      Rs 250 *', quantities[e], '=', 250 * quantities[e])
			elif e == 3:
				count = count + 1
				print(count, '.', 'Smartphone x ', quantities[e], ' Rs 20,000 *', quantities[e], '=', 20000 * quantities[e])
			elif e == 4:
				count = count + 1
				print(count, '.', 'Ipad x ', quantities[e], '       Rs 30,000 *', quantities[e], '=', 30000 * quantities[e])
			elif e == 5:
				count = count + 1
				print(count, '.', 'Laptop x ', quantities[e], '     Rs 50,000 *', quantities[e], '=', 50000 * quantities[e])
			elif e == 6:
				count = count + 1
				print(count, '.', 'Egg x ', quantities[e], '        Rs 5 *', quantities[e], '=', 5 * quantities[e])
			elif e == 7:
				count = count + 1
				print(count, '.', 'Chocolate x ', quantities[e], '  Rs 10 *', quantities[e], '=', 10 * quantities[e])
			elif e == 8:
				count = count + 1
				print(count, '.', 'Juice x ', quantities[e], '      Rs 100 *', quantities[e], '=', 100 * quantities[e])
			elif e == 9:
				count = count + 1
				print(count, '.', 'Milk x ', quantities[e], '       Rs 45 *', quantities[e], '=', 45 * quantities[e])
def calculate_category_wise_cost(quantities):
	"""
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	Returns: A 3-tuple of integers in the following format:
	(apparels_cost, electronics_cost, eatables_cost)
	"""
	c0 = 500 * quantities[0]
	c1 = 600 * quantities[1]
	c5 = 50000 * quantities[5]
	c6 = 5 * quantities[6]
	c9 = 45 * quantities[9]
	c8 = 100 * quantities[8]
	c7 = 10 * quantities[7]
	c2 = 250 * quantities[2]
	c4 = 30000 * quantities[4]
	c3 = 20000 * quantities[3]
	f = 0
	apparelscost = c0+c1+c2
	electronicost = c3+c4+c5
	eatablescost = c6+c7+c8+c9
	if f in range(0, 3):
		if c0 >= 0 or c1 >= 0 or c2 >= 0:
			print('APPARELS: = Rs ', c0 + c1 + c2)
			f = f + 3
	if f in range(3, 6):
		if c3 >= 0 or c4 >= 0 or c5 >= 0:
			print('ELECTRONICS: = Rs ', c3 + c4 + c5)
			f = f + 3
	if f in range(6, 10):
		if c6 >= 0 or c7 >= 0 or c8 >= 0 or c9 >= 0:
			print('EATABLES: = Rs ', c6 + c7 + c8 + c9)

	return apparelscost, electronicost, eatablescost
def get_discount(cost, discount_rate):
	"""
	Description: This is a helper function. DO NOT CHANGE THIS.
	This function must be used whenever you are calculating discounts.
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1
	Returns: The discount on the cost provided.
	"""
	discount = discount_rate
	return int(cost * discount)
def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):

	"""
	Description: Calculates the discounted category-wise price, if applicable.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	Returns: A 3-tuple of integers in the following format:
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
	"""

	if apparels_cost > 0 or electronics_cost > 0 or eatables_cost > 0:
		if apparels_cost >= 2000:
			disc1 = get_discount(int(apparels_cost), 0.1)
			cost_with_discount1 = apparels_cost-disc1
			print('[APPARELS] Rs', apparels_cost, '-', disc1, '=', cost_with_discount1)
		else:
			print('Discount not applicable on APPARELS')
			cost_with_discount1 = apparels_cost
			disc1 = 0
		if electronics_cost >= 25000:
			disc2 = get_discount(int(electronics_cost), 0.1)
			cost_with_discount2 = electronics_cost-disc2
			print('[ELECTRONICS] Rs', electronics_cost, '-', disc2, '=', cost_with_discount2)
		else:
			print('Discount not applicable on ELECTRONICS')
			cost_with_discount2 = electronics_cost
			disc2 = 0
		if eatables_cost >= 500:
			disc3 = get_discount(int(eatables_cost), 0.1)
			cost_with_discount3 = eatables_cost-disc3
			print('[EATABLES] Rs', eatables_cost, '-', disc3, '=', cost_with_discount3)
		else:
			print('Discount not applicable on EATABLES')
			cost_with_discount3 = eatables_cost
			disc3 = 0
	else:
		print('Sorry!! Not Applicable for the Discount')
		disc1, disc2, disc3 = 0, 0, 0
		cost_with_discount1, cost_with_discount2, cost_with_discount3 = 0, 0, 0
	print('TOTAL DISCOUNT = Rs', disc1+disc2+disc3)
	print('TOTAL COST = Rs', cost_with_discount1+cost_with_discount2+cost_with_discount3)

	return cost_with_discount1, cost_with_discount2, cost_with_discount3
def get_tax(cost, tax):
	"""
	Description: This is a helper function. DO NOT CHANGE THIS.
	This function must be used whenever you are calculating discounts.
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1
	Returns: The tax on the cost provided.
	"""
	return int(cost * tax)
def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	"""
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	Returns: A 2-tuple of integers in the following format:
	(total_cost_including_tax, total_tax)
	"""
	if apparels_cost > 0:
		tax_1 = get_tax(apparels_cost, 0.1)
		cost1 = apparels_cost+tax_1
		print('[APPARELS] Rs', apparels_cost, '*', 0.1, '=', 'Rs', tax_1)
	else:
		tax_1 = 0
		cost1 = 0
		print('Nothing Bought from APPARELS')
	if electronics_cost > 0:
		tax_2 = get_tax(electronics_cost, 0.15)
		cost2 = electronics_cost+tax_2
		print('[ELECTRONICS] Rs', electronics_cost, '*', 0.15, '=', 'Rs', tax_2)
	else:
		tax_2 = 0
		cost2 = 0
		print('Nothing Bought from ELECTRONICS')
	if eatables_cost > 0:
		tax_3 = get_tax(eatables_cost, 0.05)
		cost3 = eatables_cost+tax_3
		print('[EATABLES] Rs', eatables_cost, '*', 0.05, '=', 'Rs', tax_3)
	else:
		tax_3 = 0
		cost3 = 0
		print('Nothing Bought from EATABLES')
	total_tax = tax_1+tax_2+tax_3
	total_cost_including_tax = cost1+cost2+cost3
	print('TOTAL TAX:', total_tax)
	print('TOTAL COST:', total_cost_including_tax)
	return total_cost_including_tax, total_tax
def apply_coupon_code(total_cost):
	"""
	Description: Takes the coupon code from the user as input (case-sensitive).
	For details, refer the PDF. Include appropriate print statements to match
	the output with the screenshot provided in the PDF.
	Parameters: The total cost (integer) on which the coupon is to be applied.
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	"""
	if total_cost < 25000:
		while 1 > 0:
			coupon = input('Enter a valid coupon code(else leave blank)::')
			if len(coupon) == 0:
				print('NO COUPON APPLIED NEITHER YOU ARE APPLICABLE!!')
				break
			elif coupon == 'HELLE25':
				print('SORRY! Not Applicable For Coupon Discount')
			elif coupon == 'CHILL50':
				print('SORRY! Not Applicable For Coupon Discount')
			else:
				print('Invalid coupon code . Please Try Again')
		total_coupon_discount = 0
		total_cost_after_coupon_dicount = total_cost
	elif total_cost >= 25000 or total_cost >= 50000:
		print('---------------------------------------------------')
		print('|                   COUPON CODE                   |')
		print('---------------------------------------------------')
		while 1 > 0:
			coupon = input('Enter a valid coupon code(else leave blank)::')
			if len(coupon) == 0:
				print('NO COUPON APPLIED')
				break
			elif coupon == 'HELLE25':
				print('congrats! Rightly entered code')
				break
			elif coupon == 'CHILL50':
				print('congrats! Rightly entered code')
				break
			else:
				print('Invalid coupon code . Please Try Again')

		if coupon == 'HELLE25':
			if total_cost >= 25000:
				disc_rate = 0.25
				total_ = get_discount(total_cost, disc_rate)
				total_coupon_discount = min(5000, total_)
				print('[HELLE25] min(5,000 ,', 'Rs', total_cost, '*', 0.25, ') = Rs', total_coupon_discount)
				print()

		elif coupon == 'CHILL50':
			if total_cost >= 50000:
				disc_rate = 0.5
				total_ = get_discount(total_cost, disc_rate)
				total_coupon_discount = min(10000, total_)
				print('[CHILL50] min(10,000 ,', 'Rs', total_cost, '*', 0.50, ') = Rs', total_coupon_discount)
				print()
			else:
				print('Not applicable as the Total cost is less than 50,000')
				while 1 > 0:
					coupon = input('Enter a valid coupon code(else leave blank)::')
					if len(coupon) == 0:
						print('NO COUPON APPLIED')
						break
					elif coupon == 'HELLE25':
						print('congrats! Rightly entered code')
						break
				if coupon == 'HELLE25':
					if total_cost >= 25000:
						disc_rate = 0.25
						total_ = get_discount(total_cost, disc_rate)
						total_coupon_discount = min(5000, total_)
						print('[HELLE25] min(5,000 ,', 'Rs', total_cost, '*', 0.25, ') = Rs', total_coupon_discount)
						print()
		else:
			total_coupon_discount = 0
			total_cost_after_coupon_dicount = total_cost

		total_coupon_discount = 0
		total_cost_after_coupon_dicount = total_cost
		print('TOTAL COUPON DISCOUNT', '=', 'Rs', total_coupon_discount)
		print('TOTAL COST = Rs', total_cost_after_coupon_dicount)
	else:
		total_coupon_discount = 0
		total_cost_after_coupon_dicount = total_cost
	print('TOTAL COUPON DISCOUNT', '=', 'Rs', total_coupon_discount)
	print('TOTAL COST = Rs', total_cost_after_coupon_dicount)
	return int(total_cost_after_coupon_dicount), int(total_coupon_discount)



def main():
	"""
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate
	print statements to match the output with the screenshots provided in the PDF.
	Parameters: No parameters
	Returns: No return value
	"""
	show_menu()
	print('---------------------------------------------------')
	while True:
		var = input('Would you like to buy in Bulk ?(Y or y / N or n)::')
		if var == 'n' or var == 'N':
			print('---------------------------------------------------')
			print('|                  ORDER DETAILS::                |')
			print('---------------------------------------------------')
			organised_input = get_regular_input()
			break
		elif var == 'Y' or var == 'y':
			print('---------------------------------------------------')
			print('|             ENTER ITEMS AND QUANTITY            |')
			print('---------------------------------------------------')
			organised_input = get_bulk_input()
			print('---------------------------------------------------')
			print('|                  ORDER DETAILS::                |')

			break
	print('---------------------------------------------------')

	print_order_details(organised_input)
	print('---------------------------------------------------')
	print('|                CATEGORY-WISE COST               |')
	print('---------------------------------------------------')
	category_cost = calculate_category_wise_cost(organised_input)
	a = category_cost[0]
	b = category_cost[1]
	c = category_cost[2]
	print('---------------------------------------------------')
	print('|                    Discounts                    |')
	print('---------------------------------------------------')
	discounted_prices_without_tax = calculate_discounted_prices(a, b, c)
	print('---------------------------------------------------')
	print('|                   TAX DETAILS                   |')
	print('---------------------------------------------------')
	discounted_prices_with_tax = calculate_tax(int(discounted_prices_without_tax[0]), int(discounted_prices_without_tax[1]), int(discounted_prices_without_tax[2]))
	cost_with_tax = discounted_prices_with_tax[0]
	apply_coupon_code(int(cost_with_tax))
	print()
	print()
	print('THANK YOU FOR YOUR VISIT !!')



if __name__ == '__main__':
	main()
