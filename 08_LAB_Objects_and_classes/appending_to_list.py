class CowsAndBulls:
    def __init__(self, numbers, nums):
        self.numbers = numbers
        self.nums = nums

    def check_win(self):
        pass


my_list = []
my_new_list = []

while True:
    command = input("Choose Star or Stop:...")
    if command == 'stop':
        print(f"GoodBye!!! See you next time!")
        break

    numbers = [int(num) for num in input(f"Computer numbers: ").split()]
    x_nums = [int(x) for x in input(f"Your suggestion: ").split()]
    cows = 0
    bulls = 0
    for i in x_nums:
        if i in numbers:
            if x_nums.index(i) == numbers.index(i):
                bulls += 1
            else:
                cows += 1

    cowAndBulls = CowsAndBulls(numbers, x_nums)

    my_list.append(cowAndBulls)
    my_new_list.append(cowAndBulls)

    print(cowAndBulls.check_win())

#test
