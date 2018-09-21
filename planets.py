def weight_on_planets():
    user_in = float(input("What do you weigh on earth? "))
    marsweight = user_in * .38
    jupiterweight = user_in * 2.34
    print("\nOn Mars you would weigh " + str(marsweight) + " pounds.\nOn Jupiter you would weigh " + str(
        jupiterweight) + " pounds.")


if __name__ == '__main__':
    weight_on_planets()