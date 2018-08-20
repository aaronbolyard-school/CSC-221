SOURCE = set(['chicken', 'fox', 'grain', 'man'])
DESTINATION = set()

def transfer_to(obj):
	if obj in SOURCE:
		DESTINATION.add(obj)
		SOURCE.remove(obj)

def transfer_from(obj):
	if obj in DESTINATION:
		SOURCE.add(obj)
		DESTINATION.remove(obj)

def verify(side):
	safe = True

	if not 'man' in side:
		if 'chicken' in side and 'fox' in side:
			print("Oh no, the fox ate the chicken!")
			safe = False

		if 'chicken' in side and 'grain' in side:
			print("Oh no, the chicken at the grain!")
			safe = False

	return safe

def verify_both():
	safe_source = verify(SOURCE)
	safe_destination = verify(DESTINATION)
	if safe_source and safe_destination:
		print("Everything is good!")	

def main():
	print("The Man takes the Chicken across the river.")
	transfer_to('man')
	transfer_to('chicken')
	verify_both()

	print("The Man goes back empty handed.")
	transfer_from('man')
	verify_both()

	print("The Man takes the Fox across the river.")
	transfer_to('man')
	transfer_to('grain')
	verify_both()

	print("The Man goes back with the Chicken.")
	transfer_from('man')
	transfer_from('chicken')
	verify_both()

	print("The Man takes the Grain across the River.")
	transfer_to('man')
	transfer_to('fox')
	verify_both()

	print("The Man goes back empty handed.")
	transfer_from('man')
	verify_both()

	print("The Man takes the Chicken across the River.")
	transfer_to('man')
	transfer_to('chicken')
	verify_both()

	print("Hopefully that worked!")

main()
