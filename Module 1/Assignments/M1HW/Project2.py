# Aaron Bolyard
# 2018-08-30
# Calculates pay.
# M1HW Project 2 CSC-221

import Common

# The additional compensation for overtime pay.
# This value is multiplied by what the employee would
# have regularly been paid during that time.
OVERTIME_COMP = 1.5

def main():
	weekly_pay = Common.get_float("Enter the employee's hourly wage:", lambda x: x > 0)
	regular_hours = Common.get_float("Enter the employee's regular hours:", lambda x: x > 0)
	overtime_hours = Common.get_float("Enter the employee's overtime hours:", lambda x: x > 0)

	gross_pay = weekly_pay * regular_hours + weekly_pay * overtime_hours * OVERTIME_COMP

	print(str.format("The employee earned ${0:.02f}.", gross_pay))

if __name__ == "__main__":
	main()
