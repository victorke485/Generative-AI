with entry {
    num1 = int(input("Enter the first number: "));
    num2 = int(input("Enter the second number: "));
    operator = input("Enter an operator(+, -, /, *): ");

    if (operator == "+") {
        print(f"{num1} {operator} {num2} = {num1 + num2}");
    } elif (operator == "-") {
        print(f"{num1} {operator} {num2} = {num1 - num2}");
    } elif (operator == "/") {
        if (num2 == 0) {
            print("Math Error");
        } else {
            print(f"{num1} {operator} {num2} = {num1 / num2}");
        }
    } elif (operator == "*") {
        print(f"{num1} {operator} {num2} = {num1 * num2}");
    } else {
        print("Enter valid operator");
    }
}