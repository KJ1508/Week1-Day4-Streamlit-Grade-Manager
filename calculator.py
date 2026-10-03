def calculator():
	print("Select operation:")
	print("1. Add (+)")
	print("2. Subtract (-)")
	print("3. Multiply (*)")
	print("4. Divide (/)")
	print("5. Exit")

	while True:
		choice = input("\nEnter choice (1/2/3/4/5): ")

		if choice == "5":
			print("Exiting calculator. Goodbye!")
			break

		if choice not in ("1", "2", "3", "4"):
			print("Invalid choice. Enter 1 to 5.")
			continue

		try:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
		except ValueError:
			print("Please enter valid numbers.")
			continue

		if choice == "1":
			print("Result:", num1 + num2)
		elif choice == "2":
			print("Result:", num1 - num2)
		elif choice == "3":
			print("Result:", num1 * num2)
		elif choice == "4":
			if num2 == 0:
				print("Cannot divide by zero.")
			else:
				print("Result:", num1 / num2)


calculator()
