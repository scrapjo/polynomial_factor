from sympy import symbols, expand, factor, roots, nroots, simplify, pretty_print



#2 ask user to input each coefficient, one at the time, at last to input the divisor,
#3 print out the input and ask user if its correct
	#a) if correct continue calculation, display the ansver of the polynomial division, and ask user if they want to display the rest of the factors.
	#b) if wrong, ask user which of the factors are wrong and let the user update, then move on to a

#4 when finished, give the user the option to see the calculations, and the answer.

def parse_polynomial(poly_str):
	x = symbols('x')
	return expand(poly_str)

def factor_polynomial(poly):
	return factor(poly)



#def abc_formula():
#
#
#
#def display_calculations():
#
#
#
#def display_factors():
#
#
#
#def calculate_result():




#input validation, to make sure that polynomials are in the correct format
def get_polynomial():
	while True:
		polynomial = input("input the polynomial (e.g., x**5 + 3*x**4 - 2*x**3 + 3*x**2 - 2*x + 12: ")
		print("Your polynomial are:", polynomial)
		if input("Is this polynomial correct? (y/n): ").strip().lower() in ['y', 'yes']:
			return polynomial
		
		while True:
			edit = input("Do you want to edit the polynomial? (y/n):").strip().lower()
			if edit in  ['y', 'yes']:
				polynomial = edit_polynomial(polynomial)
				print("Updated Polynomial:", polynomial)
				if input("Is this correct now? (y/n):").strip().lower() in ['y', 'yes']:
					return polynomial
			elif edit in ['n', 'no']:
				break #go back to enter a new polynomial
			else:
				print("Please enter 'y' or 'n'.")
		


def edit_polynomial(polynomial):
	terms = polynomial.replace(" ", "").replace("-","+-").split("+")
	terms = [term for term in terms if term] #remove empty strings

	print("Current terms:")
	for i in term in enumerate(terms, 1):
		print(f"{i}. {term}")

	while True:
		choice = input("Enter the number of the term you want to edit(or 'q' to finish editing): ")
		if coice.lower() == 'q':
			break
		try:
			index = int(choice) -1
			if 0 <= index < len(terms):
				new_term = input(f"Enter the new term to replace' {terms[index]}': ")
				terms[index] = new_term
			else:
				print("Invalid term number.")
		except ValueError:
			print("Please enter a valid number or 'q'.")
	return " + ".join(terms).replace("? -", "- ")



def main():
	print("\nThis program will factor polynomials")
	polynomial = get_polynomial()
	
	print(f"\nProcessing: {polynomial}")
	poly = parse_polynomial(polynomial)
	print(f"Parsed polynomial: {poly}")

	factored = factor_polynomial(poly)
	if factored != poly:
		print(f"Factored form: {pretty(factored)}")
	else:
		print("The polynomial cannot be factored further.")

	root_dict = roots(poly)
	if root_dict:
		print("\nSymbolic Roots")
		for root, multiplicity in root_dict.items():
			simplified_root = simplify(root)
			print(f"x = {simplified_root}, multiplicity: {multiplicity}")
	else:
		print("No symbolic roots found.")

	print("\nNumerical Approximations of Roots:")
	try:
		numerical_roots = nroots(poly)
		if numerical_roots:
			for i, root in enumerate(numerical_roots, 1):
				if root.is_real:
					print(f"Root {i}: {root:.6f}")
				else:
					real_part = root.as_real_imag()[0]
					imag_part = root.as_real_imag()[1]
					print(f"Root {i}: {real_part:.6f} + {imag_part:6f}i")
		else:
			print("No numerical roots found.")
	except Exception as e:
		print("An error occured while calculating numerical roots", e)




if __name__ == '__main__':
	main()
