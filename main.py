class main:
    def __init__(self):

        print("Hello.")
        print("It is a simple calculator that only adds.")
        print("Type 'stop' to shut down the system and view the results.")

        self.calculation_data = 0

        self.addition()

    def addition(self):

        while True:
            indata = input("Enter number or code : ")

            try:
                indata = int(indata)

                self.calculation_data = self.calculation_data + indata

            except ValueError:
                print("Please enter a number!!!")

            if indata == "stop":
                print(f"Total Data : {self.calculation_data}")

                print("Bye")

                break

if __name__ == "__main__":
    main()