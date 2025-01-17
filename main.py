from modules import file_handler as fh, match_result_engine as mre
from modules.sortable_class import Sortable

test_list = fh.load("test")

winner_list = test_list[:2]
print(f"\n - Winners : ")
for test in winner_list:
	test.print()

loser_list = test_list[2:]
print(f"\n - Losers : ")
for test in loser_list:
	test.print()

mre.resolve_match(winner_list,loser_list)

print(f"\n - Updated : ")
for test in test_list:
	test.update()
	test.print()
