budget = float(input())
flour_price = float(input())

pack_of_eggs = flour_price * 0.75
one_liter_milk_price = flour_price * 1.25   # only 250 ml milk for bread

one_loaf_price = pack_of_eggs + flour_price + (one_liter_milk_price / 4)

total_amount_for_loaves = budget
loaves_count = 0
colored_eggs = 0

while total_amount_for_loaves >= one_loaf_price:

    total_amount_for_loaves -= one_loaf_price
    loaves_count += 1
    colored_eggs += 3

    if loaves_count != 0 and loaves_count % 3 == 0:
        colored_eggs -= loaves_count - 2

if total_amount_for_loaves <= one_loaf_price:
    print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {total_amount_for_loaves:.2f}BGN left.")

