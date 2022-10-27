#6510742460 Putthipong Soongsuwan
import math
def final_amount(IP_deposit, IP_rate, IP_years):
    print(f"Final amount: {(IP_deposit)*(pow((1+IP_rate/100),IP_years)):,.2f}")
def main():
    IP_deposit = int(input("Input deposit: "))
    IP_rate = int(input("Interest rate(%): "))
    IP_years = int(input("years: "))
    final_amount(IP_deposit, IP_rate, IP_years)
main()